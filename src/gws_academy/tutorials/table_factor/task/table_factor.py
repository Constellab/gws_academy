"""
ceci est un tuto
"""
from gws_core import ConfigParams, IntParam, InputSpec, OutputSpec, Task, TaskInputs, TaskOutputs, task_decorator, Table
from pandas import DataFrame


@task_decorator("TableFactor", human_name="Factor Table")
class TableFactor(Task):
    input_specs = {'input_table': InputSpec(Table)}
    output_specs = {'output_table': OutputSpec(Table)}
    config_specs = {'factor': IntParam(default_value= 2)}


    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        df = inputs['input_table'].get_data()
        factor = params['factor']
        return {'output_table': Table(factor*df) }
