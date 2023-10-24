# LICENCE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com

import os

from gws_core import (CondaShellProxy, ConfigParams, File, InputSpec,
                      MessageDispatcher, OutputSpec, PipShellProxy, Task,
                      TaskFileDownloader, TaskInputs, TaskOutputs,
                      task_decorator, TableExporter, TableImporter)
from gws_core.config.param.param_spec import IntParam, StrParam
from gws_core.impl.shell.shell_proxy import ShellProxy

class KeggSchemaColorEnvHelper():
    CONDA_ENV_DIR_NAME = "KeggSchemaColorCondaEnv"
    PIP_ENV_DIR_NAME = "KeggSchemaColorPipEnv"
    CONDA_ENV_FILE_PATH = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "kegg_schema_color_conda.yml")
    PIP_ENV_FILE_PATH = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "kegg_schema_color_pipenv.txt")

    @classmethod
    def create_conda_proxy(cls, message_dispatcher: MessageDispatcher = None) -> CondaShellProxy:
        return CondaShellProxy(cls.CONDA_ENV_DIR_NAME, cls.CONDA_ENV_FILE_PATH, message_dispatcher=message_dispatcher)

    @classmethod
    def create_pip_proxy(cls, message_dispatcher: MessageDispatcher = None) -> PipShellProxy:
        return PipShellProxy(cls.PIP_ENV_DIR_NAME, cls.PIP_ENV_FILE_PATH, message_dispatcher=message_dispatcher)


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
    input_specs = InputSpecs({
        "input_table" : InputSpec(Table, human_name="input Table")
    })

    output_specs = OutputSpecs({
        'output_schema' : OutputSpec(File, human_name="output scheme"),
        'output_table' : OutputSpec(Table, human_name="output table")
    })

    config_specs = {
        'specie' : StrParam(
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

    shell_proxy: ShellProxy = None

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:



        with open("bricks/gws_academy/src/gws_academy/KeggSchemaColor/kegg_schema_color.r", 'r+') as file:
            original_contents = file.read()

            file.seek(0)
            file.write(f"""
            specie = "{params['species']}" \n
            pathway_id = "{params['pathway_id']}" \n
            type_gene_id = "{params['type_gene_id']}" \n
            column_gene_id = "{params['column_gene_id']}" \n
            column_control = "{param['column_contro'l]}" \n
            column_wild = "{params['column_wild']}" \n
            """)
            file.write(original_contents)

        TableExporter.call(source =inputs['input_table'], params = {'file_name' : 'input_table'})

        ############### Create the shell proxy ################
        shell_proxy = BlastEnvHelper.create_conda_proxy(
            self.message_dispatcher)
        # store the shell_proxy in the class to be able to use it in the run_after_task method
        self.shell_proxy = shell_proxy

        result = shell_proxy.run("Rscript kegg_schema_color.r")

        if result != 0:
            raise Exception('Error during the process')


        output_file_name = "result.csv"
        # get the absolute path of the output
        output_file_path = os.path.join(
            shell_proxy.working_dir, output_file_name)
        # create the output Resource (File)
        output_file = File(output_file_path)

        return {'output_table' : TableImporter.call(File('result.csv')),
                'output_schema' : output_file}



     def run_after_task(self) -> None:
        # use to delete the temp folder once the task is done and output resources saved
        # this is safe to do it here becase the output resource was move to the Resource location
        if self.shell_proxy:
            self.shell_proxy.clean_working_dir()