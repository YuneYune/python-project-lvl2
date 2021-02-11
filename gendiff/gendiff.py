#!/usr/bin/env python3

"""Gendiff cli."""

import argparse
import json


def generate_diff(first_file=None, second_file=None):
    """Greeting.

    Returns:
        Returns difference of the player
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output')

    if first_file is None and second_file is None:
        args = parser.parse_args()
        first_file = args.first_file
        second_file = args.second_file
    diff = get_diff(first_file, second_file)
    return json.dumps(diff, indent=2, sort_keys=False)


def get_diff(first, second):
    first = json.load(open(first))
    second = json.load(open(second))
    first = dict(sorted(first.items()))
    second = dict(sorted(second.items()))
    result = {}
    for k in first.keys():
        if k in second.keys():
            if first[k] == second[k]:
                result['  {0}'.format(k)] = first[k]
            else:
                key_of_removed = '- {0}'.format(k)
                result[key_of_removed] = first[k]
                key_of_exist = '+ {0}'.format(k)
                result[key_of_exist] = second[k]
        else:
            key_of_removed = '- {0}'.format(k)
            result[key_of_removed] = first[k]
    for k in second.keys():
        if k not in result.keys():
            key_of_added = '+ {0}'.format(k)
            result[key_of_added] = second[k]
    return result
