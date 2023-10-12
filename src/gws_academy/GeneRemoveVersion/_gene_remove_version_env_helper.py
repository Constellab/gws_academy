class GeneRemoveVersionEnvHelper():
   # define the name of the virtual environment, it must be unique
    CONDA_ENV_DIR_NAME = "GeneRemoveVersionCondaEnv"

   # path of the yaml environment file. The file blast_conda.yml must be in the same folder as this file﻿
    CONDA_ENV_FILE_PATH = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "gene_remove_version_conda.yml")

    # method to create the conda shell proxy.
    # we pass the MessageDispatcher so that the output of the command line will be logged in the Task
    @classmethod
    def create_conda_proxy(cls, message_dispatcher: MessageDispatcher = None) -> CondaShellProxy:
        return CondaShellProxy(cls.CONDA_ENV_DIR_NAME, cls.CONDA_ENV_FILE_PATH, message_dispatcher=message_dispatcher)