
import os

from gws_core import (CondaShellProxy, ConfigParams, File, InputSpec,
                      InputSpecs, IntParam, MessageDispatcher, OutputSpec,
                      OutputSpecs, PipShellProxy, ShellProxy, StrParam, Task,
                      TaskFileDownloader, TaskInputs, TaskOutputs,
                      task_decorator)


class BlastEnvHelper():
    CONDA_ENV_DIR_NAME = "BlastCondaEnv"
    PIP_ENV_DIR_NAME = "BlastPipEnv"
    CONDA_ENV_FILE_PATH = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "blast_conda.yml")
    PIP_ENV_FILE_PATH = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "blast_pipenv.txt")

    @classmethod
    def create_conda_proxy(cls, message_dispatcher: MessageDispatcher = None) -> CondaShellProxy:
        return CondaShellProxy(cls.CONDA_ENV_DIR_NAME, cls.CONDA_ENV_FILE_PATH, message_dispatcher=message_dispatcher)

    @classmethod
    def create_pip_proxy(cls, message_dispatcher: MessageDispatcher = None) -> PipShellProxy:
        return PipShellProxy(cls.PIP_ENV_DIR_NAME, cls.PIP_ENV_FILE_PATH, message_dispatcher=message_dispatcher)


@task_decorator("Blast", human_name="Blast")
class Blast(Task):

    # zebra_fish_db_url = "https://storage.gra.cloud.ovh.net/v1/AUTH_a0286631d7b24afba3f3cdebed2992aa/opendata/gws_academy/zebrafish.1.protein.faa.gz"
    # INPUT DATA PATH = "https://storage.gra.cloud.ovh.net/v1/AUTH_a0286631d7b24afba3f3cdebed2992aa/opendata/gws_academy/mouse.1.protein.faa.gz"

    input_specs = InputSpecs({'input_file': InputSpec(File, human_name="Compressed fasta file",
                                                      short_description="The fasta.gz file to compare with db"),
                              })
    output_specs = OutputSpecs({'blast_result': OutputSpec(File, human_name="Blast result file",
                                                           short_description="Result file generated by the blast command")})

    config_specs = {
        'db_path': StrParam(
            default_value="https://storage.gra.cloud.ovh.net/v1/AUTH_a0286631d7b24afba3f3cdebed2992aa/opendata/gws_academy/zebrafish.1.protein.faa.gz",
            human_name="Database path", short_description="Must be a .faa.gz file"),
        'head': IntParam(default_value=0, human_name="Limit input file read",
                         short_description="Number of line in the input file to compare. 0 for all lines")}

    shell_proxy: ShellProxy = None

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        """ Run the task """

        ############################ Download the database ############################
        # retrieve the db url from the param
        db_url: str = params['db_path']

        # extract the filename from the url
        db_file_name = db_url.split('/')[-1]

        # create the file downloader using the current task brick name,
        # by passing the brick name of the Task, the file will be downloaded in a specific location for the brick
        # also pass the message_dispatcher to log downlod progress in the task messag
        file_downloader = TaskFileDownloader(Blast.get_brick_name(), self.message_dispatcher)

        # download the db and retrieve the path of the downloaded file
        zebra_zipped_db = file_downloader.download_file_if_missing(db_url, db_file_name)

        ############################ Create the shell proxy ############################
        shell_proxy = BlastEnvHelper.create_conda_proxy(
            self.message_dispatcher)
        # store the shell_proxy in the class to be able to use it in the run_after_task method
        self.shell_proxy = shell_proxy

        ############################ Prepare the DB ############################

        zebra_db = "zebra_fish_db.faa"
        # Unzip db file in the working directory and verify the result
        result = shell_proxy.run([f"gunzip -c {zebra_zipped_db} > {zebra_db}"])
        if result != 0:
            raise Exception('Error during the unzip of database .gz file')

        # Create the blast db in the working directory and check the result
        # all the shell command are executed in the virtual environment, so the makeblastdb is available
        result = shell_proxy.run([f"makeblastdb -in {zebra_db} -dbtype prot -out {zebra_db}"])
        if result != 0:
            raise Exception('Error during the creation of the blast db')

        ############################ Prepare the input file ############################
        # retrive the input table
        file: File = inputs['input_file']

        # Unzip the input file in the working directory and verify the result
        input_file_unzipped = "input.faa"
        result = shell_proxy.run([f"gunzip -c {file.path} > {input_file_unzipped}"])
        if result != 0:
            raise Exception('Error during the unzip of .gz file')

        # Limit the number of lines to compare if needed
        head: int = params['head']

        file_to_compare: str = None
        # limit the number of lines
        if head > 0:
            # use the head command to limit the number of lines
            sub_file = 'sub_input_file.faa'
            result = shell_proxy.run([f"head -n {head} {input_file_unzipped} > {sub_file}"])

            if result != 0:
                raise Exception('Error during the head command')
            file_to_compare = sub_file
        else:
            # no need to limit the number of line
            file_to_compare = input_file_unzipped

        ############################ Run the blast and retrieve reulst ############################
        output_file_name = 'output.txt'
        # run the blast
        result = shell_proxy.run([f"blastp -query {file_to_compare} -db {zebra_db} -out {output_file_name}"])

        if result != 0:
            raise Exception('Error during the blast')

        # get the absolute path of the output
        output_file_path = os.path.join(
            shell_proxy.working_dir, output_file_name)
        # create the output Resource (File)
        output_file = File(output_file_path)

        # return the output table
        return {'blast_result': output_file}

    def run_after_task(self) -> None:
        # use to delete the temp folder once the task is done and output resources saved
        # this is safe to do it here becase the output resource was move to the Resource location
        if self.shell_proxy:
            self.shell_proxy.clean_working_dir()
