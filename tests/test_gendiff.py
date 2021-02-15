#!/usr/bin/env python3
"""Tests."""

import json

from gendiff.gendiff import generate_diff


def test_generate_diff():
    """Tests of generate_diff function.

    Returns answer of assert.
    """
    first_path = 'tests/fixtures/file1.json'
    second_path = 'tests/fixtures/file2.json'
    diff = generate_diff(first_path, second_path)
    expected_answer = {
        '- follow': False,
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ host': 'hexlet.io',
        '+ verbose': True,
    }
    assert diff == json.dumps(expected_answer, indent=2, sort_keys=False)
