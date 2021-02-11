#!/usr/bin/env python3

"""Test."""

from gendiff.gendiff import generate_diff


def main():
    """CLI command."""
    diff = generate_diff()
    print(diff)


if __name__ == '__main__':
    main()
