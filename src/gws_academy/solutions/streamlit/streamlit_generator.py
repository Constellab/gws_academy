
import os

from gws_core import (ConfigParams, ConfigSpecs, Dashboard, DashboardType,
                      InputSpec, InputSpecs, OutputSpec, OutputSpecs,
                      StreamlitResource, StrParam, Table, Task, TaskInputs,
                      TaskOutputs, dashboard_decorator, task_decorator)


@dashboard_decorator("BiolectorParserStandalone", dashboard_type=DashboardType.STREAMLIT)
class BiolectorParserStandaloneClass(Dashboard):

    # retrieve the path of the app folder, relative to this file
    # the dashboard code folder starts with a underscore to avoid being loaded when the brick is loaded
    def get_folder_path(self):
        return os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "_dashboard_code"
        )


@task_decorator("StreamlitGenerator", human_name="Generate dashboard for table",
                short_description="Task to generate a custom Streamlit dashboard from a table",
                )
class StreamlitGenerator(Task):

    input_specs: InputSpecs = InputSpecs({'table': InputSpec(Table, human_name="Table")})
    output_specs: OutputSpecs = OutputSpecs({
        'streamlit_app': OutputSpec(StreamlitResource, human_name="Streamlit app")
    })
    config_specs: ConfigSpecs = {
        'title': StrParam(human_name='Dashboard title')
    }

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
        streamlit_resource.set_dashboard(BiolectorParserStandaloneClass())

        return {'streamlit_app': streamlit_resource}
