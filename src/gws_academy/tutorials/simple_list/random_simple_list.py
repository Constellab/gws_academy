
import random

from gws_core import (ConfigParams, IntParam, OutputSpec, OutputSpecs, ConfigSpecs,
                      StrParam, Task, TaskInputs, TaskOutputs, task_decorator)

from .simple_list import SimpleList


@task_decorator("RandomSimpleList", human_name="Random simple list",
                short_description="Generate a random simple list")
class RandomSimpleList(Task):
    """
    This is a simple task to generate a random list of float number between 0 and 100
    """

    output_specs = OutputSpecs({'simple_list': OutputSpec(SimpleList, human_name="Result",
                                                          short_description="The output result")})

    config_specs = ConfigSpecs({
        'list_length': IntParam(default_value=100, min_value=1, max_value=10000),
        'description': StrParam()})

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        """ Run the task """

        # retrieve the description
        description = params['description']

        # retrieve the list length
        list_length = params['list_length']

        # create an empty SimpleList
        simple_list = SimpleList()

        # set the description in the resource
        simple_list.description = description

        # force the name of the resource
        simple_list.name = 'My random list'

        # add the numbers to the list
        for i in range(0, list_length):
            simple_list.add_number(random.uniform(1, 100))

        return {'simple_list': simple_list}
