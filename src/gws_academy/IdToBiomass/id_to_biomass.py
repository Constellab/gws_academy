# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs,
                      OutputSpec, OutputSpecs, StrParam, Task, JSONDict,
                      TaskInputs, TaskOutputs, task_decorator)


@task_decorator("IdToBiomass", human_name="Id to Biomass",
    short_description="Change the 'id' of the biomass reaction into 'biomass'")
class IdToBiomass(Task):
    input_specs = InputSpecs({'input_json': InputSpec(JSONDict, human_name="input model")})
    output_specs = OutputSpecs({'output_json' : OutputSpec(JSONDict, human_name = "output model")})

    config_specs= {
        "id" : StrParam(
            default_value=None,
            human_name="id to change",
            short_description="exact id of the biomass reaction"
        )
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        organism =inputs['input_json'].get_data()

        for i in range(len(organism['reactions'])) :
            if organism['reactions'][i]["id"] == params["id"] :
                organism['reactions'][i]["id"] = "Biomass"

        return {'output_json' : organism}
