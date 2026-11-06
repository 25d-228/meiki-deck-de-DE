"""Basic completion check for one German text stage and its coverage."""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [200, 600, 900, 1200, 1400, 1600, 1800, 1000]
REQUIRED = {'schema_version', 'id', 'locale', 'sentence', 'cloze', 'answer',
            'accepted_answers', 'lemma', 'meaning', 'part_of_speech'}
SUPPORT = {'noun', 'verb', 'grammar', 'pronunciation', 'usage', 'recognition'}


def words(text):
    return len(re.findall(r"[^\W_]+(?:['’][^\W_]+)*", unicodedata.normalize('NFC', text)))


def characters(text):
    return sum(not ch.isspace() for ch in unicodedata.normalize('NFC', text))


def check_card(card, stage):
    """Return inexpensive field, normalization, alignment and length defects."""
    errors = []
    if not isinstance(card, dict) or set(card) != {'common', 'language_specific'}:
        return ['record must contain exactly common and language_specific']
    c, support = card['common'], card['language_specific']
    if not isinstance(c, dict) or not REQUIRED <= c.keys() or c.keys() - REQUIRED - {'register', 'note'}:
        return ['incorrect common fields']
    if type(c['schema_version']) is not int or c['schema_version'] != 2 or c['locale'] != 'de-DE':
        errors.append('incorrect schema_version or locale')
    for key in c.keys() - {'schema_version', 'accepted_answers'}:
        if not isinstance(c[key], str) or not c[key].strip():
            errors.append(f'{key} must be a nonempty string')
    if not isinstance(c['accepted_answers'], list) or any(not isinstance(a, str) or not a.strip() for a in c['accepted_answers']):
        errors.append('invalid accepted_answers')
        return errors
    if errors:
        return errors
    for key, value in c.items():
        for item in value if isinstance(value, list) else [value]:
            if isinstance(item, str) and unicodedata.normalize('NFC', item) != item:
                errors.append(f'{key} is not NFC')
    if c['cloze'] != c['answer'] or c['sentence'].count(c['cloze']) != 1:
        errors.append('cloze/answer mismatch or cloze does not occur exactly once')
    limits = (12, 90) if int(stage) <= 1 else (16, 120) if int(stage) == 2 else (20, 150)
    if words(c['sentence']) > limits[0] or characters(c['sentence']) > limits[1]:
        errors.append('sentence exceeds cap')
    for span in [c['cloze'], c['answer'], *c['accepted_answers']]:
        if words(span) > 5 or characters(span) > 40:
            errors.append('cloze/answer/variant exceeds cap')
    if len(set(c['accepted_answers'])) != len(c['accepted_answers']) or c['answer'] in c['accepted_answers']:
        errors.append('redundant accepted answer')
    if not isinstance(support, dict) or support.keys() - SUPPORT:
        errors.append('incorrect language_specific fields')
        return errors
    for key, value in support.items():
        if key == 'noun':
            if not isinstance(value, dict) or not {'article', 'plural'} <= value.keys() or value.keys() - {'article', 'plural', 'genitive'}:
                errors.append('incorrect noun support fields')
            elif value['article'] not in {'der', 'die', 'das'} or any(not isinstance(v, str) or not v.strip() for v in value.values()):
                errors.append('invalid noun support')
        elif key == 'verb':
            if not isinstance(value, dict) or set(value) != {'present_3sg', 'preterite_3sg', 'participle', 'auxiliary', 'separable'}:
                errors.append('incorrect verb support fields')
            elif type(value['separable']) is not bool or any(not isinstance(v, str) or not v.strip() for k, v in value.items() if k != 'separable'):
                errors.append('invalid verb support')
        elif not isinstance(value, str) or not value.strip():
            errors.append(f'invalid {key} support')
        if unicodedata.normalize('NFC', json.dumps(value, ensure_ascii=False)) != json.dumps(value, ensure_ascii=False):
            errors.append(f'{key} support is not NFC')
    return errors


def main(stage):
    cards = json.loads((ROOT / f'cards/de-DE/{stage}.json').read_text())
    expected = [f'de-{stage}-{i:04d}' for i in range(1, COUNTS[int(stage)] + 1)]
    errors = []
    if not isinstance(cards, list) or [c.get('common', {}).get('id') for c in cards] != expected:
        errors.append('incorrect stage count or ordered IDs')
    for card in cards:
        errors.extend(f"{card.get('common', {}).get('id', '?')}: {e}" for e in check_card(card, stage))
    coverage = (ROOT / f'coverage/de-DE/{stage}.md').read_text()
    block_text, card_text = coverage.split('## Cards', 1)
    rows = [line.split('|')[1:-1] for line in card_text.splitlines() if line.startswith(f'| de-{stage}-')]
    if [r[0].strip() for r in rows] != expected:
        errors.append('coverage must contain one ordered row per card')
    allocated = {}
    for line in block_text.splitlines():
        if not line.startswith(f'| {stage}.'):
            continue
        row = [v.strip() for v in line.split('|')[1:-1]]
        ids = re.findall(rf'de-{stage}-(\d{{4}})', row[4])
        if len(ids) != 2 or int(row[3]) != int(ids[1]) - int(ids[0]) + 1:
            errors.append('invalid coverage block allocation')
            continue
        for index in range(int(ids[0]), int(ids[1]) + 1):
            cid = f'de-{stage}-{index:04d}'
            if cid in allocated:
                errors.append(f'{cid}: overlapping blocks')
            allocated[cid] = row[0]
    if set(allocated) != set(expected):
        errors.append('coverage blocks do not allocate every ID exactly once')
    for row in rows:
        if len(row) != 3 or allocated.get(row[0].strip()) != row[1].strip() or not row[2].strip():
            errors.append(f'{row[0].strip()}: missing or inconsistent coverage')
    seen_ids, seen_sentences = set(), {}
    for path in sorted((ROOT / 'cards/de-DE').glob('*.json')):
        if not path.stem.isdigit() or int(path.stem) > int(stage):
            continue
        for card in json.loads(path.read_text()):
            c = card['common']
            sentence = ' '.join(unicodedata.normalize('NFC', c['sentence']).split())
            if c['id'] in seen_ids:
                errors.append(f"duplicate ID: {c['id']}")
            if sentence in seen_sentences:
                errors.append(f"duplicate sentence: {c['id']} and {seen_sentences[sentence]}")
            seen_ids.add(c['id'])
            seen_sentences[sentence] = c['id']
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: stage {stage}, {len(cards)} cards, complete coverage, fields/alignment/caps/duplicates checked.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
