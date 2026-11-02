"""Read-only product availability check. No device operations."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', required=True)
    parser.parse_args()
    catalog = json.loads(Path(__file__).with_name('releases.json').read_text())
    if catalog != {'schema_version': 1, 'releases': []}:
        raise SystemExit('Unsupported release catalog: no installation implementation available.')
    print('No validated releases available. No device was accessed.')


if __name__ == '__main__':
    main()
