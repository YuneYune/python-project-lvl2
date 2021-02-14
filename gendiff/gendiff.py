#!/usr/bin/env python3

"""Gendiff cli."""

import argparse
import json


def generate_diff(first_file=None, second_file=None):
    """CLI command.

    Args:
        first_file (str): Path to first dictionary.
        second_file (str): Path to second dictionary.

    Returns:
        diff (json): Dictionary of differences.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', metavar='FORMAT', help='set format of output',
    )

    if first_file is None and second_file is None:
        args = parser.parse_args()
        first_file = args.first_file
        second_file = args.second_file
    diff = get_diff(*sort_dicts(*open_dicts(first_file, second_file)))
    return json.dumps(diff, indent=2, sort_keys=False)


def open_dicts(first_path, second_path):
    """Open two dicts.

    Args:
        first_path (str): The path to the first dictionary.
        second_path (str): The path to the second dictionary.

    Returns:
        first_dict (dict): First dictionary.
        second_dict (dict): Second dictionary.
    """
    with open(first_path) as first_dict:
        with open(second_path) as second_dict:
            first_dict = json.load(first_dict)
            second_dict = json.load(second_dict)
            return first_dict, second_dict


def sort_dicts(first_dict, second_dict):
    """Sort two dicts.

    Args:
        first_dict (dict): The first dictionary.
        second_dict (dict): The second dictionary.

    Returns:
        sorted_first (dict): First soterd dictionary.
        sorted_second (dict): Second soterd dictionary.
    """
    sorted_first = dict(sorted(first_dict.items()))
    sorted_second = dict(sorted(second_dict.items()))
    return sorted_first, sorted_second


def get_diff(first_dict, second_dict):
    """Return difference of two dicts.

    Args:
        first_dict (dict): The first dictionary.
        second_dict (dict): The second dictionary.

    Returns:
        diff (dict): Dictionary of differences.
    """
    diff = {}
    for key in first_dict.keys():
        value_of_key = first_dict[key]
        if key in second_dict.keys():
            if first_dict[key] == second_dict[key]:
                diff['  {0}'.format(key)] = value_of_key
            else:
                diff['- {0}'.format(key)] = value_of_key
                diff['+ {0}'.format(key)] = value_of_key
        else:
            diff['- {0}'.format(key)] = value_of_key
    for sec_key in second_dict.keys():
        if sec_key not in diff.keys():
            diff['+ {0}'.format(sec_key)] = second_dict[sec_key]
    return diff
