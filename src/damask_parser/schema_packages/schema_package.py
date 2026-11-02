# from typing import (
#     TYPE_CHECKING,
# )

# if TYPE_CHECKING:
#     from nomad.datamodel.datamodel import (
#         EntryArchive,
#     )
#     from structlog.stdlib import (
#         BoundLogger,
#     )

from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.metainfo import MEnum, MSection, Quantity, SchemaPackage, SubSection

configuration = config.get_plugin_entry_point(
    'nomad_damask_parser.schema_packages:mypackage'
)

m_package = SchemaPackage()


class CompoundDataset1D(MSection):
    dim0 = Quantity(type=int, description='1st dimension')
    name = Quantity(type=str, description='Name of the dataset')
    unit = Quantity(type=str, description='Unit of the data in this dataset')
    description = Quantity(
        type=str, description='Information about the nature of the dataset'
    )


class CompoundDataset2D(MSection):
    dim0 = Quantity(type=int, description='1st dimension')
    dim1 = Quantity(type=int, description='2nd dimension')
    name = Quantity(type=str, description='Name of the dataset')
    unit = Quantity(type=str, description='Unit of the data in this dataset')
    description = Quantity(
        type=str, description='Information about the nature of the dataset'
    )


class Dataset1D(MSection):
    dim0 = Quantity(type=int, description='1st dimension')
    name = Quantity(type=str, description='Name of the dataset')
    unit = Quantity(type=str, description='Unit of the data in this dataset')
    description = Quantity(
        type=str, description='Information about the nature of the dataset'
    )


class Dataset2D(MSection):
    dim0 = Quantity(type=int, description='1st dimension')
    dim1 = Quantity(type=int, description='2nd dimension')
    name = Quantity(type=str, description='Name of the dataset')
    unit = Quantity(type=str, description='Unit of the data in this dataset')
    description = Quantity(
        type=str, description='Information about the nature of the dataset'
    )


class Dataset3D(MSection):
    dim0 = Quantity(type=int, description='1st dimension')
    dim1 = Quantity(type=int, description='2nd dimension')
    dim2 = Quantity(type=int, description='3rd dimension')
    name = Quantity(type=str, description='Name of the dataset')
    unit = Quantity(type=str, description='Unit of the data in this dataset')
    description = Quantity(
        type=str, description='Information about the nature of the dataset'
    )


###############################################################################
class PhaseField(MSection):
    name = Quantity(type=MEnum('mechanical', 'damage', 'thermal'))
    datasets1D = SubSection(sub_section=Dataset1D.m_def, repeats=True)
    datasets2D = SubSection(sub_section=Dataset2D.m_def, repeats=True)
    datasets3D = SubSection(sub_section=Dataset3D.m_def, repeats=True)


class PhaseName(MSection):
    name = Quantity(type=str, description='User defined name of the phase')
    fields = SubSection(sub_section=PhaseField.m_def, repeats=True)


class HomogenizationField(MSection):
    name = Quantity(type=MEnum('mechanical', 'damage', 'thermal'))
    datasets1D = SubSection(sub_section=Dataset1D.m_def, repeats=True)
    datasets2D = SubSection(sub_section=Dataset2D.m_def, repeats=True)
    datasets3D = SubSection(sub_section=Dataset3D.m_def, repeats=True)


class HomogenizationName(MSection):
    name = Quantity(type=str, description='User defined name of the homogenization')
    fields = SubSection(sub_section=HomogenizationField.m_def, repeats=True)


class GeometryDataset(MSection):
    datasets1D = SubSection(sub_section=Dataset1D.m_def, repeats=True)
    datasets2D = SubSection(sub_section=Dataset2D.m_def, repeats=True)
    datasets3D = SubSection(sub_section=Dataset3D.m_def, repeats=True)


class Increment(MSection):
    name = Quantity(type=str, description='Name of the increment')
    geometry = SubSection(sub_section=GeometryDataset.m_def, repeats=False)
    homogenization = SubSection(sub_section=HomogenizationName.m_def, repeats=True)
    phase = SubSection(sub_section=PhaseName.m_def, repeats=True)


###############################################################################
class SetupFile(MSection):
    name = Quantity(type=str, description='Name of the setup file')


class Setup(MSection):
    description = Quantity(type=str, description='Information about the setup section')
    filenames = SubSection(sub_section=SetupFile.m_def, repeats=True)


###############################################################################
class Geometry(MSection):
    cells = Quantity(
        type=int, shape=[3], description='Values corresponding to the cells'
    )
    origin = Quantity(
        type=float, shape=[3], description='Values corresponding to the origin'
    )
    size = Quantity(
        type=float, shape=[3], description='Values corresponding to the size'
    )


###############################################################################
class CellTo(MSection):
    description = Quantity(
        type=str, description='Information about the cell_to section'
    )
    datasets1D = SubSection(sub_section=CompoundDataset1D.m_def, repeats=True)
    datasets2D = SubSection(sub_section=CompoundDataset2D.m_def, repeats=True)
    # phase = Quantity(type=HDF5Reference)


###############################################################################
###############################################################################
class DAMASKOutput(Schema):
    code_version = Quantity(
        type=str,
        description='Version of DAMASK used to produce the results of this simulation',
    )
    number_increments = Quantity(
        type=int, shape=[], description='Number of increments in the simulation'
    )
    phase_names = Quantity(
        type=str,
        shape=['*'],
        description='Unique names of the different phases used in the simulation',
    )
    homogenization_names = Quantity(
        type=str,
        shape=['*'],
        description="""
        Unique names of the different homogenizations used in the simulation
        """,
    )
    points_number = Quantity(
        type=int, shape=[], description='Number of points in the simulation'
    )
    solver_name = Quantity(
        type=str, description='Name of the solver used for the simulation'
    )
    cell_to = SubSection(sub_section=CellTo.m_def, repeats=False)
    geometry = SubSection(sub_section=Geometry.m_def, repeats=False)
    increments = SubSection(sub_section=Increment.m_def, repeats=True)
    setup = SubSection(sub_section=Setup.m_def, repeats=False)


m_package.__init_metainfo__()
