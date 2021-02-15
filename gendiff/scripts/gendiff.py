#!/usr/bin/env python3

"""Generate diff."""

import sys

from gendiff.gendiff import generate_diff


def main():
    """CLI command."""
    diff = generate_diff()
    sys.stdout.write(diff)


if __name__ == '__main__':
    main()
