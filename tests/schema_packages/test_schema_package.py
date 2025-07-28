import os.path

from nomad.client import parse


def test_schema():
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]

    assert entry_archive.data.code_version == '3.0.1'
