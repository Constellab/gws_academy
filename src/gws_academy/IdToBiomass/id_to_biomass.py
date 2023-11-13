# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com
import simplejson as json
from cobra.io import model_from_dict, to_json
from gws_core import (ConfigParams, InputSpec, InputSpecs,
                      OutputSpec, OutputSpecs, StrParam, Task, JSONDict,
                      TaskInputs, TaskOutputs, task_decorator)


@task_decorator("IdToBiomass", human_name="Id to Biomass",
                short_description="Change the 'id' of the biomass reaction into 'biomass'")
class IdToBiomass(Task):
    """
    ## Specs
    input : JSONDict
    output : JSONDict
    params :
    - `id to change` : str: exact id of the reaction corresponding to the biomass reaction
    ## Use

    This task will return a model where the reaction with the `id to change ` has as its new ID : "biomass"

    """
    input_specs = InputSpecs({'input_json': InputSpec(JSONDict, human_name="input model")})
    output_specs = OutputSpecs({'output_json': OutputSpec(JSONDict, human_name="output model")})

    config_specs = {
        "id": StrParam(
            default_value=None,
            human_name="id to change",
            short_description="exact id of the biomass reaction"
        )
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        organism = model_from_dict(inputs["input_json"].get_data())
        # Obtenir une liste de tous les IDs de réaction dans le modèle
        reaction_ids = [reaction.id for reaction in organism.reactions]

        if params["id"] not in reaction_ids :
            raise Exception(f"id {params['id']} not in reactions")
        to_modify = organism.reactions.get_by_id(params["id"])
        to_modify.id = "Biomass"
        return {'output_json': JSONDict(json.loads(to_json(organism)))}
