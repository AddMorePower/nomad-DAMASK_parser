from nomad.config.models.plugins import SchemaPackageEntryPoint


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_damask_parser.schema_packages.mypackage import m_package

        return m_package


mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)
