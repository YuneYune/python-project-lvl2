#!/usr/bin/env python3

"""Test."""

import argparse
import sys


def main():
    """Algorithm."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    sys.stdout.write(args)


if __name__ == '__main__':
    main()
