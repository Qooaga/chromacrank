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
    print('No supported installation releases available. No device was accessed.')
    print('Experimental V3.1: https://github.com/Qooaga/chromacrank/releases/tag/v3.1-experimental')


if __name__ == '__main__':
    main()
