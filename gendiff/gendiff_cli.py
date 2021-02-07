#!/usr/bin/env python3

"""Gendiff cli."""

import sys
import argparse


def gendiff():
    """Greeting.

    Returns:
        Returns name of the player
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output')

    args = parser.parse_args()
    sys.stdout.write(args)
