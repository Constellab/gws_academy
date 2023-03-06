# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, IntParam, OutputSpec, StrParam,
                      Table, Task, TaskInputs, TaskOutputs, task_decorator)

from ..resource.template_task_result import AcademyTemplateTaskResult


@task_decorator("AcademyTemplateTask", human_name="Academy template task",
                short_description="Academy template task")
class AcademyTemplateTask(Task):
    """
    Academy template task

    Describe your task using Markdown (https://www.markdownguide.org/)
    """

    input_specs = {'table': InputSpec(Table, human_name="Table", short_description="The input table")}
    output_specs = {'result': OutputSpec(AcademyTemplateTaskResult, human_name="Result",
                                         short_description="The output result")}

    config_specs = {
        "param1":
        StrParam(
            default_value=None, human_name="Text parameter",
            short_description="Text parameter"),
        "param2":
        IntParam(
            default_value=None, optional=True, human_name="Interger parameter",
            visibility=IntParam.PROTECTED_VISIBILITY,
            short_description="My first parameter"),
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        """ Run the task """

        result = AcademyTemplateTaskResult()

        # ... do something
        # ...
        # ... result.add_resource( ... )
        # ...

        return {'result': result}
