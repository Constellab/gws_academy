# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam)

from gws_academy.Plotly.PlotlyTask.plotly_task import PlotlyTask
import pandas as pd

import plotly.express as px
# from plotly.subplots import make_subplots


@task_decorator("PlotlyLine", human_name="Line Plotly",
                short_description="line plot from plotly")
class PlotlyLine(PlotlyTask):

    input_specs = PlotlyTask.input_specs

    output_specs = PlotlyTask.output_specs


    config_specs = {
        **PlotlyTask.config_specs_d2,

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
        **PlotlyTask.config_specs_layout
    }



    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
    # Get the data frame from the input
        dataframe = pd.DataFrame(inputs['input_table'].get_data())
        for key, i  in params.items() :
            if i == "" :
                params[key]= None
        if params['label_columns'] is not None :
            labels = dict(params['label_columns'], params['label_text'])
        else:
            labels = None


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
            labels=labels
        )

        # Update axis titles
        fig.update_xaxes(title=params['x_axis_name'])
        fig.update_yaxes(title=params['y_axis_name'])

        return {"output_plot": PlotlyResource(fig)}
