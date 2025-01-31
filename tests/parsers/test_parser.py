import logging

from nomad.datamodel import EntryArchive

from nomad_damask_parser.parsers.myparser import MyParser


def test_parse_file():
    parser = MyParser()
    archive = EntryArchive()
    parser.parse(
        'tests/data/4grains2x4x3_compressionY.hdf5', archive, logging.getLogger()
    )

    assert archive.results.method.simulation.program_name == 'DAMASK'
