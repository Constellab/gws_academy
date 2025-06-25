
import os

from gws_core import (AppConfig, AppType, ConfigParams, ConfigSpecs, InputSpec,
                      InputSpecs, OutputSpec, OutputSpecs, StreamlitResource,
                      StrParam, Table, Task, TaskInputs, TaskOutputs,
                      app_decorator, task_decorator)


@app_decorator("BiolectorParserStandalone", dashboard_type=AppType.STREAMLIT)
class BiolectorParserStandaloneClass(AppConfig):

    # retrieve the path of the app folder, relative to this file
    # the dashboard code folder starts with a underscore to avoid being loaded when the brick is loaded
    def get_app_folder_path(self):
        return os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "_dashboard_code"
        )


@task_decorator("StreamlitGenerator", human_name="Generate dashboard for table",
                short_description="Task to generate a custom Streamlit dashboard from a table",
                )
class StreamlitGenerator(Task):

    input_specs: InputSpecs = InputSpecs(
        {'table': InputSpec(Table, human_name="Table")})
    output_specs: OutputSpecs = OutputSpecs({
        'streamlit_app': OutputSpec(StreamlitResource, human_name="Streamlit app")
    })
    config_specs: ConfigSpecs = ConfigSpecs({
        'title': StrParam(human_name='App title')
    })

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:

        # build the streamlit resource with the code and the resources
        streamlit_resource = StreamlitResource()

        # set the input in the streamlit resource
        table: Table = inputs.get('table')
        streamlit_resource.add_resource(table)

        # set the param of the streamlit resource
        title = params.get_value('title')
        streamlit_resource.set_param('title', title)

        # set the app dashboard
        streamlit_resource.set_app_config(BiolectorParserStandaloneClass())

        return {'streamlit_app': streamlit_resource}
