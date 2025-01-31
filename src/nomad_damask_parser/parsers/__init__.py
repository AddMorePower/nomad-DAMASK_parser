from nomad.config.models.plugins import ParserEntryPoint


class MyParserEntryPoint(ParserEntryPoint):
    def load(self):
        from nomad_damask_parser.parsers.myparser import MyParser

        return MyParser(**self.dict())


myparser = MyParserEntryPoint(
    name='MyParser',
    description='Parser defined using the new plugin mechanism.',
    mainfile_name_re='.*\.hdf5',
    mainfile_contents_dict={'__has_all_keys': ['cell_to', 'geometry', 'setup']},
)
