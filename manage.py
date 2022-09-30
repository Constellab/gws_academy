# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com
import importlib.util
import os
import sys

gws_core_package = 'gws_core'

# if the gws_core package is already listed in the modules, do nothing
if gws_core_package in sys.modules:
    print(f"{gws_core_package} already in sys.modules")

# try to install in from the pip package
elif (spec := importlib.util.find_spec(gws_core_package)) is not None:
    # If you choose to perform the actual import ...
    module = importlib.util.module_from_spec(spec)
    sys.modules[gws_core_package] = module
    spec.loader.exec_module(module)
    print(f"{gws_core_package} has been imported from pip packages")

# try to install it from the bricks folder
else:
    core_lib_path = "/lab/user/bricks/gws_core/src"
    if not os.path.exists(core_lib_path):
        core_lib_path = "/lab/user/bricks/.lib/gws_core/src"
        if not os.path.exists(core_lib_path):
            raise Exception("Cannot find gws_core brick")
    sys.path.insert(0, core_lib_path)
    print(f"{gws_core_package} has been imported path '{core_lib_path}'")


if __name__ == "__main__":
    from gws_core import manage, runner
    __cdir__ = os.path.dirname(os.path.abspath(__file__))
    manage.load_settings(__cdir__)
    runner.run()
