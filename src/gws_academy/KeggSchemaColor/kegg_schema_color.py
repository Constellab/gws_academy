# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs,
                      OutputSpec, OutputSpecs, Table, Task, BoolParam, StrParam,
                      TaskInputs, TaskOutputs, task_decorator, File, FileDownloader, TaskFileDownloader)


import requests
import os


@task_decorator("kegg_schema_color", human_name='kegg schema_color', short_description="Kegg pathway visualiser")
class KeggSchema(Task):
    """
    # LICENCE
    KEGG is a database resource for understanding high-level functions and
    utilities of the biological system. Kanehisa Laboratories owns and controls
    the rights to KEGG. Although the KEGG database is made freely available for
    academic use via the website, it is not in the public domain. All
    commercial use of KEGG requires a license. Please ensure that you have
    licence to use KEGG database."""
    input_specs = InputSpecs({})

    output_specs = OutputSpecs({
        'output_file' : OutputSpec(File, human_name="output scheme")
    })

    config_specs = {
        specie : StrParam(
            default_value=None,
            optional=True,
            human_name='species',
            short_description=""
        ),
        'pathway_id' : StrParam(
            default_value=None,
            optional=True,
            human_name='pathway id',
            short_description='replace with the pathway id you want to explore (map00010 for example), None, not known',
        ),
        'type_gene_id' : StrParam(
            default_value=None,
            optional=True,
            human_name="Type gene id",
            short_description=" i.e : Glycolysis, if you don't know the pathway ID, fill this with the name"
        ),
        'column_gene_id' : StrParam(
            default_value=None,
            optional=True,
            human_name='column gene id',
            short_description=""
        ),
        'column_control' : StrParam(
            default_value=None,
            optional=True,
            human_name='column control',
            short_description=""
        ),
        'column_wild' : StrParam(
            default_value=None,
            optional=True,
            human_name='column wild',
            short_description=""
        ),

    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        with open("bricks/gws_academy/src/gws_academy/KeggSchemaColor/kegg_schema_color.r", 'r'):
            