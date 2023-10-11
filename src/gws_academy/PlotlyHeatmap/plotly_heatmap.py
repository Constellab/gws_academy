# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task,
                      TaskInputs, TaskOutputs, task_decorator,
                      ListParam)

import pandas as pd

import plotly.express as px

@task_decorator(unique_name="PlotlyHeatmap", human_name="Heatmap Plot",
short_description="Heatmap with Plotly")

class PlotlyHeatmap(Task):
    input_specs = InputSpecs({'input_table': InputSpec(Table, human_name="input_table")})

    output_specs = OutputSpecs({'output_plot': OutputSpec(PlotlyResource, human_name="output graph")})

    config_specs = {
        'x' : ListParam(
            default_value=None,
            human_name="x labels",
            optional=True,
            short_description="labels for the x axis"
        ),
        'y' : ListParam(
            default_value=None,
            human_name="y labels",
            optional=True,
            short_description="labels for the y axis"
        ),
        'title': StrParam(
            default_value=None,
            optional=True,
            human_name="Title",
            short_description="Title of the graph"
        ),
        'y_axis_name': StrParam(
            default_value=None,
            optional=True,
            human_name="Y Axis Name",
            short_description=""
        ),
        'x_axis_name': StrParam(
            default_value=None,
            optional=True,
            human_name="X Axis Name",
            short_description=""
        ),
        'color_range_name': StrParam(
            default_value=None,
            optional=True,
            human_name="color scale name",
            short_description=""
        ),
        "color_scale" : StrParam(
            default_value=None,
            optional=True,
            allowed_values= ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance','blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg', 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl', 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric', 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys', 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet', 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges', 'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd'],
            human_name="color scale",
            short_description="Determine the color scale"
        ),
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        dataframe = pd.DataFrame(inputs['input_table'].get_data())

        fig = px.imshow(
            img=dataframe,
            labels=dict(
                x=params["x_axis_name"],
                y=params['y_axis_name'],
                color=params['color_range_name']),
            title=params['title'],
            color_continuous_scale=params["color_scale"]
        )


        return {"output_plot": PlotlyResource(fig)}
