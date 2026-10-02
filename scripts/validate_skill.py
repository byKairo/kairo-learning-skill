#!/usr/bin/env python3
"""Check the learning skill package using only the Python standard library."""
import argparse
import re
from pathlib import Path


def validate(root):
    errors = []
    entry = root / 'SKILL.md'
    if not entry.is_file():
        return ['SKILL.md is missing']
    text = entry.read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not front:
        return ['Invalid frontmatter']
    fields = dict(re.findall(r'^(name|description):\s*(.+)$', front.group(1), re.M))
    name = fields.get('name', '')
    if name != 'kairo-learning' or not fields.get('description'):
        errors.append('Expected kairo-learning name and a description')
    ui = root / 'agents/openai.yaml'
    if not ui.is_file():
        errors.append('Missing UI metadata')
    else:
        body = ui.read_text(encoding='utf-8')
        if 'display_name: "kairo-learning"' not in body or '$kairo-learning' not in body:
            errors.append('UI metadata does not match invocation name')
    for path in root.rglob('*'):
        if path.is_symlink():
            errors.append(f'Unexpected package symlink: {path.relative_to(root)}')
        if not path.is_file() or path.suffix not in {'.md', '.yaml', '.json'}:
            continue
        body = path.read_text(encoding='utf-8')
        if re.search(r'/Users/[^/\s]+/|/home/[^/\s]+/', body):
            errors.append(f'Local user path: {path.relative_to(root)}')
        if path.suffix == '.md':
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', body):
                target = target.split('#', 1)[0].strip('<>')
                if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(f'Invalid reference: {path.relative_to(root)} -> {target}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path,
                        default=Path(__file__).resolve().parents[1] / 'skills/kairo-learning-skill')
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print('ERROR:', error)
    print('Structure check failed.' if errors else 'Structure check passed; teaching behavior is not evaluated.')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
