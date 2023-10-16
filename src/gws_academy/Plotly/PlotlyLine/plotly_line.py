# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam)

import pandas as pd

import plotly.express as px
# from plotly.subplots import make_subplots


@task_decorator("PlotlyLine", human_name="Line Plotly",
                short_description="line plot from plotly(px)")
class PlotlyLine(Task):

    input_specs = InputSpecs({'input_table': InputSpec(Table, human_name="input_table")})
    output_specs = OutputSpecs({'output_plot': OutputSpec(PlotlyResource, human_name="output graph")})

    config_specs = {
        'x': StrParam(
            default_value=None,
            human_name="x-axis",
            short_description="Indicate the name of the Serie for the x-axis"
        ),
        'y': StrParam(
            default_value=None,
            human_name="y-axis",
            short_description="Indicate the Series to plot"
        ),
        'title': StrParam(
            default_value=None,
            optional=True,
            human_name="Title of the graph",
            short_description=""
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
        'color': StrParam(
            default_value=None,
            optional=True,
            human_name="Color",
            short_description="clomuns for the color"
        ),
        'symbol': StrParam(
            default_value=None,
            optional=True,
            human_name="Symbol",
            short_description=""
        ),
        'line_group' : StrParam(
            default_value=None,
            optional=True,
            human_name=" Group by line",
            short_description="group rows by line"
        ),
        'hover_data': StrParam(
            default_value=None,
            optional=True,
            human_name="Hover Data",
            short_description="Columns to display when hovering over data points"
        ),
        'text' : StrParam(
            default_value=None,
            optional=True,
            human_name="Text tag",
            short_description="",
        ),
        'markers' : BoolParam(
            default_value=False,
            human_name="Marker",
            optional=True,
            short_description="if ticked, markers are shown on line"
        ),
        'facet_col': StrParam(
            default_value=None,
            optional=True,
            human_name="Facet Column",
            short_description="Column to facet the plot into subplots by",
            visibility="protected"
        ),
        'facet_row': StrParam(
            default_value=None,
            optional=True,
            human_name="Facet Row",
            short_description="Column to facet plot into subplots by (rows)",
            visibility="protected"
        ),
        'facet_col_wrap': IntParam(
            default_value=None,
            optional=True,
            human_name="Facet Col Wrap",
            short_description="Maximum number of facet columns to display",
            visibility="protected"
        ),
        'log_x': BoolParam(
            default_value=False,
            optional=True,
            human_name="Log X Axis",
            short_description="Set X axis to logarithmic scale",
            visibility="protected"
        ),
        'log_y': BoolParam(
            default_value=False,
            optional=True,
            human_name="Log Y Axis",
            short_description="Set Y axis to logarithmic scale",
            visibility="protected"
        ),
        'animation_frame': StrParam(
            default_value=None,
            optional=True,
            human_name="Animation Frame",
            short_description="Column for animation frame",
            visibility="protected"
        ),
        'animation_group': StrParam(
            default_value=None,
            optional=True,
            human_name="Animation Group",
            short_description="Column for grouping data points in animations",
            visibility="protected"
        ),
        'line_shape' : StrParam(
            default_value=None,
            optional=True,
            human_name="line shape",
            allowed_values=["linear", "spline"],
            visibility="protected",
            short_description=""
            ),
        'render_mode': StrParam(
            default_value=None,
            optional=True,
            human_name="Render Mode",
            allowed_values=["svg", "webgl", "auto"],
            short_description="Set the render mode for points (e.g., 'webgl' or 'svg')",
            visibility="protected"
        ),
        'height': IntParam(
            default_value=None,
            optional=True,
            human_name="Height",
            short_description="Set the height of the graph",
            visibility="protected"
        ),
        'width': IntParam(
            default_value=None,
            optional=True,
            human_name="Width",
            short_description="Set the width of the graph",
            visibility="protected"
        )
    }



    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
    # Get the data frame from the input
        dataframe = pd.DataFrame(inputs['input_table'].get_data())

        # Create the line plot using Plotly Express
        fig = px.line(
            data_frame=dataframe,
            x=params['x'],
            y=params['y'],
            title=params['title'],
            color=params['color'],
            symbol=params["symbol"],
            line_group=params['line_group'],
            hover_data=params["hover_data"],
            markers=params["markers"],
            text=params["text"],
            facet_col=params["facet_col"],
            facet_row=params["facet_row"],
            facet_col_wrap=params["facet_col_wrap"],
            log_x=params["log_x"],
            log_y=params["log_y"],
            animation_frame=params["animation_frame"],
            animation_group=params["animation_group"],
            line_shape=params['line_shape'],
            render_mode=params["render_mode"],
            height=params["height"],
            width=params["width"],
        )

        # Update axis titles
        fig.update_xaxes(title=params['x_axis_name'])
        fig.update_yaxes(title=params['y_axis_name'])

        return {"output_plot": PlotlyResource(fig)}
