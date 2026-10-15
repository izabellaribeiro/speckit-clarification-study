"""Build an unpublished, sanitized release candidate without changing source records.

Requires openpyxl. Output always goes to a new directory; manual disclosure review
is still required before publication. Run from any directory with Python 3.7+.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent
DEST = ROOT / 'release_candidate'


def clean(text):
    text = re.sub(r'(?i)\b[A-Z]:[\\/][^\s\x00\"<>|]*', '[LOCAL_PATH]', text)
    text = re.sub(r'/(?:home|Users|mnt/c/Users)/[^\s\"<>]*', '[LOCAL_PATH]', text)
    text = re.sub(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', '[EMAIL]', text)
    text = re.sub(r'(?i)\b(?:[RESEARCHER]|[RESEARCHER])\b', '[RESEARCHER]', text)
    return text


def clean_json(value):
    if isinstance(value, str):
        return clean(value)
    if isinstance(value, list):
        return [clean_json(x) for x in value]
    if isinstance(value, dict):
        return {clean(k): clean_json(v) for k, v in value.items()}
    return value


def export(source):
    target = DEST / source.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix == '.xlsx':
        book = openpyxl.load_workbook(source)
        book.properties.creator = 'Anonymous'
        book.properties.lastModifiedBy = 'Anonymous'
        for sheet in book:
            for row in sheet:
                for cell in row:
                    if isinstance(cell.value, str):
                        cell.value = clean(cell.value)
                    if cell.comment:
                        cell.comment.text = clean(cell.comment.text)
                        cell.comment.author = 'Anonymous'
                    if cell.hyperlink:
                        cell.hyperlink = None
        book.save(target)
    else:
        text = source.read_text(encoding='utf-8-sig')
        if source.suffix == '.json':
            text = json.dumps(clean_json(json.loads(text)), ensure_ascii=False, indent=2)
        elif source.suffix == '.jsonl':
            text = '\n'.join(json.dumps(clean_json(json.loads(line)), ensure_ascii=False)
                             for line in text.splitlines() if line.strip()) + '\n'
        else:
            text = clean(text)
        target.write_text(text, encoding='utf-8')


def main():
    runs = sorted(p for p in (ROOT / 'results_new').iterdir() if p.is_dir())
    expected = {'US_{:03d}_{}'.format(i, c) for i in range(1, 46)
                for c in ('baseline', 'syntactic', 'semantic', 'pragmatic')}
    if {p.name for p in runs} != expected:
        raise ValueError('Expected exactly 180 matched run directories')
    if DEST.exists():
        raise FileExistsError('Preserving existing release candidate: {}'.format(DEST))
    sources = []
    for folder in ('inputs', 'speckit_codex'):
        sources.extend(p for p in (ROOT / folder).rglob('*') if p.is_file()
                       and not any(x in p.parts for x in ('.git', '__pycache__', 'pilot_results')))
    for run in runs:
        for name in ('completed.json', 'metadata.json', 'events.jsonl', 'final_response.md', 'stderr.txt'):
            p = run / name
            if not p.exists():
                raise FileNotFoundError(str(p))
            sources.append(p)
    sources.extend(ROOT / name for name in (
        'run_replication.py', 'extract_markers.py', 'prepare_release.py',
        'mutation_manifest_SAC_2027_clean.csv', 'REPLICATION_STATUS.md',
        'reference/constitution.md', 'reference/speckit.clarify.md',
        'reference/final_audit_documented.xlsx', 'reference/dataset_mutants.xlsx',
        'reference/story_provenance.csv'))
    sources.extend(ROOT / 'reference' / name for name in (
        'dataset_themes.md', 'legacy_history.csv', 'legacy_archive_record.json'))
    sources.extend((ROOT / 'reference/legacy_baselines').glob('*.md'))
    sources.append(ROOT / 'reference/legacy_source_comparison.csv')
    sources.extend(p for p in (ROOT / 'reference/source_datasets').iterdir() if p.is_file())
    for source in sorted(set(sources)):
        export(source)
    book = openpyxl.load_workbook(DEST / 'reference/final_audit_documented.xlsx', data_only=True)
    with (DEST / 'reference/final_classification.csv').open('w', encoding='utf-8', newline='') as f:
        csv.writer(f).writerows(book['Final'].values)
    files = sorted(p for p in DEST.rglob('*') if p.is_file())
    manifest = {p.relative_to(DEST).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (DEST / 'release_manifest.json').write_text(json.dumps({
        'status': 'UNPUBLISHED; manual disclosure review required',
        'run_count': len(runs),
        'redactions': ['absolute Windows/user-home paths', 'email addresses', 'known researcher account/name'],
        'limitations': 'Automated redaction cannot certify removal of every identity, secret, or contextual identifier. Original configuration hashes refer to private original files; release hashes describe sanitized files.',
        'sha256': manifest,
    }, indent=2), encoding='utf-8')
    print('Prepared {} executions and {} files; not published.'.format(len(runs), len(files)))


if __name__ == '__main__':
    main()
