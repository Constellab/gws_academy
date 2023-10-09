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
    input_specs = InputSpecs({'input_json': InputSpec(JSONDict, human_name="model")})
    output_specs = OutputSpecs({'output_json' : OutputSpec(JSONDict, human_name = "model output")})

    config_specs= {
        "id" : StrParam(
            default_value=None,
            human_name="id to change",
            short_description="exact id of the biomass reaction"
        )
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        organism = inputs['input_json']
        for i in organism['reaction'] :
            if i["id"] == [params["id"]] :
                i["id"] = "Biomass"

        return {'output_json' : organism}
