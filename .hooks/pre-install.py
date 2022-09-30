# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com

import os

from utils._requests import Requests
from utils._settings import Settings
from utils._zip import Zip

# **********************************************************
#
# /!\ DO NOT ALTER THIS SECTION
#
# **********************************************************

__cdir__ = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = "/data"


def current_brick_path() -> str:
    return os.path.abspath(os.path.join(__cdir__, '../../'))


def current_brick_name() -> str:
    return read_settings()["name"]


def read_settings() -> dict:
    """ Read the settings file of the current brick """
    return Settings.read()


def unzip(zipfile_path, output_path: str = None) -> str:
    """ Unzip a file and return the destination path """
    return Zip.unzip(zipfile_path, output_path)


def download(url: str, dest_path: str) -> str:
    """ Download a file from a remote url """
    return Requests.download(url, dest_path)


# **********************************************************
#
# UPDATE FUNCTION call_hook() TO ADD YOUR HOOK
#
# **********************************************************
def call_hook():
    # SAMPLE CODE TO DOWNLOAD AND UNZIP REMOTE FILE

    # settings = read_settings()
    # url = settings["variables"][ "MY_VARIABLE" ]
    # dest_path = settings["variables"][ "MY_VARIABLE" ]
    # download(url, dest_path + ".zip")
    # if unzip(dest_path + ".zip"):
    #     os.remove(dest_path + ".zip")

    pass


if __name__ == "__main__":
    call_hook()
