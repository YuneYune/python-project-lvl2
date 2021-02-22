#!/usr/bin/env python3
"""Tests."""

from gendiff.gendiff import generate_diff


def test_json_diff():
    """Tests of generate_diff function.

    Returns answer of assert.
    """
    first_path = 'tests/fixtures/file1.json'
    second_path = 'tests/fixtures/file2.json'
    diff = generate_diff(first_path, second_path)
    expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
"""
    assert diff == expected


def test_yaml_diff():
    """Tests of generate_diff function.

    Returns answer of assert.
    """
    first_path = 'tests/fixtures/file1.yml'
    second_path = 'tests/fixtures/file2.yml'
    diff = generate_diff(first_path, second_path)
    expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
"""
    assert diff == expected
