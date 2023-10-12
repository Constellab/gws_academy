# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com

import re
from collections import OrderedDict
from cobra.io import model_from_dict, model_to_dict
import simplejson as json

from gws_core import  JSONDict

json_dict: JSONDict = JSONImporter.call(File("data/model.json"))


json_model = model_from_dict(json_dict)

print(json_model)
