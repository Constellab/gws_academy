# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task, FloatParam,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam)

import pandas as pd

import plotly.express as px
# from plotly.subplots import make_subplots


@task_decorator("PlotlyHistogram", human_name="Histogram Plotly",
                short_description="Histogram plot from plotly(px)")
class PlotlyHistogram(Task):

    input_specs = InputSpecs({'input_table': InputSpec(Table, human_name="input_table")})
    output_specs = OutputSpecs({'output_plot': OutputSpec(PlotlyResource, human_name="output graph")})

    config_specs = {
        'x': StrParam(
            default_value=None,
            human_name="x-axis",
            short_description="The column name to use for the x-axis."
        ),
        'title': StrParam(
            default_value=None,
            optional=True,
            human_name="Title",
            short_description="The title of the histogram."
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
            short_description="The column name to use for coloring the histogram bars."
        ),
        'hover_data': StrParam(
            default_value=None,
            optional=True,
            human_name="Hover Data",
            short_description="Columns to display when hovering over histogram bars."
        ),
        'facet_col': StrParam(
            default_value=None,
            optional=True,
            human_name="Facet Column",
            short_description="Column to facet the histogram into subplots by columns.",
            visibility="protected",
        ),
        'facet_row': StrParam(
            default_value=None,
            optional=True,
            human_name="Facet Row",
            short_description="Column to facet the histogram into subplots by rows.",
            visibility="protected",
        ),
        'facet_col_wrap': IntParam(
            default_value=None,
            optional=True,
            human_name="Facet Col Wrap",
            short_description="Maximum number of facet columns to display",
            visibility="protected",
        ),
        'height': IntParam(
            default_value=None,
            optional=True,
            human_name="Height",
            short_description="The height of the histogram plot.",
            visibility="protected",
        ),
        'width': IntParam(
            default_value=None,
            optional=True,
            human_name="Width",
            short_description="The width of the histogram plot.",
            visibility="protected",
        ),
        'opacity': FloatParam(
            default_value=None,
            optional=True,
            human_name="Opacity",
            short_description="Opacity of histogram bars (0 to 1).",
            visibility="protected",
        ),
        'histnorm': StrParam(
            default_value=None,
            optional=True,
            human_name="Normalization",
            short_description="Histogram normalization",
            allowed_values=['percent', 'probability', 'density', 'probability density'],
            visibility="protected",
        ),
        'barmode': StrParam(
            default_value=None,
            optional=True,
            human_name="Bar Mode",
            short_description="Bar mode for stacked or grouped histograms",
            allowed_values=['stack', 'group', 'overlay', 'relative'],
            visibility="protected",
        ),
        'log_x': BoolParam(
            default_value=False,
            optional=True,
            human_name="Log X Axis",
            short_description="Set X axis to logarithmic scale.",
            visibility="protected",
        ),
        'log_y': BoolParam(
            default_value=False,
            optional=True,
            human_name="Log Y Axis",
            short_description="Set Y axis to logarithmic scale.",
            visibility="protected",
        )
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        data_frame = pd.DataFrame(inputs['input_table'].get_data())
        for key, i  in params.items() :
            if i == "" :
                params[key]= None
        fig = px.histogram(
            data_frame=data_frame,
            x=params['x'],
            title=params['title'],
            color=params['color'],
            hover_data=params['hover_data'],
            facet_col=params['facet_col'],
            facet_row=params['facet_row'],
            facet_col_wrap=params['facet_col_wrap'],
            height=params['height'],
            width=params['width'],
            opacity=params['opacity'],
            histnorm=params['histnorm'],
            barmode=params['barmode'],
            log_x=params['log_x'],
            log_y=params['log_y']
        )

        return {"output_plot": PlotlyResource(fig)}
