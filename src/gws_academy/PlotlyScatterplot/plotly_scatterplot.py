# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam, ListParam)
from gws_academy.PlotlyTask.plotly_task import PlotlyTask
import pandas as pd

import plotly.express as px
# from plotly.subplots import make_subplots


@task_decorator("PlotlyScatterplot", human_name="Scatterplot Plotly",
                short_description="Scatter plot from plotly(px)")
class PlotlyScatterplot(PlotlyTask):

    input_specs = super.input_specs
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
        'colour': StrParam(
            default_value=None,
            optional=True,
            human_name="colour",
            short_description="can be a css color, one color per line"
        ),
        'symbol': StrParam(
            default_value=None,
            optional=True,
            human_name='symbol',
            short_description="",
        ),
        'size': StrParam(
            default_value=None,
            optional=True,
            human_name="columns for the size",
            short_description=""
        ),
        'y_axis_name': StrParam(
            default_value=None,
            optional=True,
            human_name="y axis name",
            short_description="",
        ),
        'x_axis_name': StrParam(
            default_value=None,
            optional=True,
            human_name="x axis name",
            short_description="",
        ),
        'title': StrParam(
            default_value=None,
            optional=True,
            human_name="Title of the graph ",
            short_description="",
        ),
        'hover_data': StrParam(
            default_value=None,
            optional=True,
            human_name="Hover Data",
            short_description="Columns to display when hovering over data points",
        ),
        'custom_data' : ListParam (
            default_value=None,
            optional=True,
            visibility='protected',
            human_name= 'extra data',
            short_description=' Values from these columns are extra data, to be used in widgets or Dash callbacks for example',
        ),
        'text' : StrParam(
            default_value=None,
            optional=True,
            human_name="text labels",
            short_description="Either a name of a column in data_frame, or a pandas Series or array_like object. Values from this column or array_like appear in the figure as text labels."
        ),
        'facet_col': StrParam(
            default_value=None,
            optional=True,
            human_name="Facet Column",
            short_description="Column to facet the plot into subplots by",
        ),
        'facet_row': StrParam(
            default_value=None,
            optional=True,
            human_name="Facet Row",
            short_description="Column to facet the plot into subplots by (rows)",
        ),
        'facet_col_wrap': IntParam(
            default_value=None,
            optional=True,
            human_name="Facet Col Wrap",
            short_description="Maximum number of facet columns to display",
            visibility="protected",
        ),
        'facet_row_spacing' : FloatParam(
            default_value=None,
            optional=True,
            human_name="Facet row Spacing",
            short_description="Spacing between facet rows, in paper units. Default is 0.03 or 0.0.7 when facet_col_wrap is used.",
            visibility="protected"
        ),
        'facet_col_spacing' : FloatParam(
            default_value=None,
            optional=True,
            human_name="Facet col Spacing",
            short_description="Spacing between facet columns, in paper units. Default is 0.03 or 0.0.7 when facet_col_wrap is used.",
            visibility="protected"
        ),
        'error_x' : StrParam(
            default_value=None,
            optional= True,
            human_name="x error",
            short_description="Either a name of a column in data_frame, or a pandas Series or array_like object. Values from this column or array_like are used to size x-axis error bars",
            visibility='protected'
        ),
        'error_x_minus' : StrParam(
            default_value=None,
            optional=True,
            human_name="min X error",
            short_description=" Either a name of a column in data_frame, or a pandas Series or array_like object. Values from this column or array_like are used to size x-axis error bars in the negative direction.",
            visibility='protected'
        ),
        'error_y' : StrParam(
            default_value=None,
            optional=True,
            human_name="y error",
            short_description="Either a name of a column in data_frame, or a pandas Series or array_like object. Values from this column or array_like are used to size y-axis error bars",
            visibility='protected'
        ),
        'error_y_minus' : StrParam(
            default_value=None,
            optional=True,
            human_name= "min y error",
            short_description=" Either a name of a column in data_frame, or a pandas Series or array_like object. Values from this column or array_like are used to size x-axis error bars in the negative direction.",
            visibility='protected'
        ),
        'animation_frame': StrParam(
            default_value=None,
            optional=True,
            human_name="Animation Frame",
            short_description="Column for animation frame",
            visibility="protected",
        ),
        'animation_group': StrParam(
            default_value=None,
            optional=True,
            human_name="Animation Group",
            short_description="Column for grouping data points in animations",
            visibility="protected",
        ),
        #'category_order_keys'
        #'category_orders_vals'
        'labels_keys' : ListParam(
            default_value=None,
            optional=True,
            visibility='protected',
            human_name='labels keys',
            short_description=" The keys of this dict should correspond to column names, and the values should correspond to the desired label to be displayed."
        ),
        'labels_vals' : ListParam(
            default_value=None,
            optional=True,
            visibility='protected',
            human_name="labels values",
            short_description="",
        ),
        'orientation' : StrParam(
            default_value='v',
            optional=True,
            human_name="orientation",
            visibility='protected',
            short_description="set the orientation of the graph",
            allowed_values=['v', 'h']
        ),
        #color_discrete #color_discrete_map #color_continuous_scale
            #range_color #color_continuous_midpoint
            #symbol_sequence #symbol_map
        'opacity' : FloatParam(
            default_value=None,
            visibility='protected',
            human_name="opacity",
            short_description="opacity of the marks"
            optional = True
        ),
        'size_max' : IntParam(
            default_value=20,
            optional=True,
            visibility='protected',
            short_description= "maximum size of the marks",
            human_name="mark opacity"
        ),
        'marginal_x': StrParam(
            default_value=None,
            optional=True,
            human_name="Marginal X",
            short_description="If set, a horizontal subplot is drawn above the main plot, visualizing the x-distribution.",
            visibility="protected",
            allowed_values=['rug', 'box', 'violin','histogram']
        ),
        'marginal_y': StrParam(
            default_value=None,
            optional=True,
            human_name="Marginal Y",
            short_description="If set, a vertical subplot is drawn to the right of the main plot, visualizing the y-distribution.",
            visibility="protected",
            allowed_values=['rug', 'box', 'violin','histogram']
        ),
        'trendline': StrParam(
            default_value='ols',
            optional=True,
            human_name="Trendline",
            short_description="Add a trendline to the plot",
            visibility="protected",
            allowed_values=['ols', 'lowess', 'rolling', 'expanding', 'ewm']
        ),
        'trendline_color_override' : StrParam(
            default_value=None,
            optional=True,
            visibility='protected',
            human_name="trendline color",
            short_description="color for the trendline",
            allowed_values=
        ),
        'trendline_scope' : StrParam(
            default_value='trace',
            optional=True,
            visibility="protected",
            human_name='trendline scope',
            short_description=' one trend line per race',
            allowed_values=['trace', 'overall']
        ),
        'log_x': BoolParam(
            default_value=False,
            optional=True,
            human_name="Log X Axis",
            short_description="Set X axis to logarithmic scale",
            visibility="protected",
        ),
        'log_y': BoolParam(
            default_value=False,
            optional=True,
            human_name="Log Y Axis",
            short_description="Set Y axis to logarithmic scale",
            visibility="protected",
        ),
        #range_x #range_y
        'render_mode': StrParam(
            default_value=None,
            optional=True,
            human_name="Render Mode",
            allowed_values=["svg", "webgl", "auto"],
            short_description="Set the render mode for points (e.g., 'webgl' or 'svg')",
            visibility="protected",
        ),
        'height': IntParam(
            default_value=None,
            optional=True,
            human_name="Height",
            short_description="Set the height of the graph",
            visibility="protected",
        ),
        'width': IntParam(
            default_value=None,
            optional=True,
            human_name="Width",
            short_description="Set the width of the graph",
            visibility="protected",
        )
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        dataframe = pd.DataFrame(inputs['input_table'].get_data())

        fig = px.scatter(
            data_frame=dataframe,
            x=params['x'],
            y=params['y'],
            title=params['title'],
            color=params['colour'],
            size=params["size"],
            symbol=params["symbol"],
            hover_name=params["hover_name"],
            hover_data=params["hover_data"],
            custom_data=params['custom_data'],
            text=params['text'],
            facet_col=params["facet_col"],
            facet_row=params["facet_row"],
            facet_col_wrap=params["facet_col_wrap"],
            error_x=params['error_x'],
            error_x_minus= params['error_x_minus'],
            error_y= params['error_y'],
            error_y_minus=params['error_y_minus'],
            animation_frame=params["animation_frame"],
            animation_group=params["animation_group"],
            #category_orders
            labels=dict(zip(params['label_columns'], params['label_text'])),
            orientation=params['orientation'],
            #color_discrete #color_discrete_map #color_continuous_scale
            #range_color #color_continuous_midpoint
            #symbol_sequence #symbol_map
            opacity=params['opacity'],
            size_max=params['size_max'],
            marginal_x=params["marginal_x"],
            marginal_y=params["marginal_y"],
            trendline=params["trendline"],
            trendline_color_override=params["trendline_color_override"],
            trendline_scope=params['trendline_scope'],
            log_x=params["log_x"],
            log_y=params["log_y"],
            #range_x #range_y
            render_mode=params["render_mode"],
            template=params['template'],
            height=params["height"],
            width=params["width"]
        )

        fig.update_xaxes(title=params["x_axis_name"])
        fig.update_yaxes(title=params['y_axis_name'])
        return {"output_plot": PlotlyResource(fig)}
