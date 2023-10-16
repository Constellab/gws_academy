from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task, FloatParam,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam)

import pandas as pd

import plotly.express as px
# from plotly.subplots import make_subplots


@task_decorator("PlotlyTask", human_name="Task Plotly",
                short_description="General Plotly Task")
class PlotlyTask(Task):
    valid_css_colours =[
        "black", "white", "red", "green", "blue", "yellow", "orange", "pink",
        "purple", "brown", "gray", "cyan", "magenta", "lime","teal", "navy" ]
    input_specs = InputSpecs({'input_table': InputSpec(Table, human_name="input_table")})

    output_specs = OutputSpecs({'output_plot': OutputSpec(PlotlyResource, human_name="output graph")})
    config_specs = {
        #base params
        'x': StrParam(
            default_value=None,
            human_name="x-axis",
            short_description="The column name to use for the x-axis."
        ),
        'y': StrParam(
            default_value=None,
            optional=True,
            human_name="y-axis",
            short_description="Column name for the y-axis"
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
        'template': StrParam(
            default_value=None,
            optional=True,
            human_name="Template",
            short_description="Plotly template to use",
            visibility="protected",
            allowed_values = [
                "ggplot2",
                "seaborn",
                "simple_white",
                "plotly",
                "plotly_dark",
                "presentation",
                "xgridoff",
                "ygridoff",
                "gridon",
                "none"
            ]
        ),
        #facet params
        'facet_row': StrParam(
            default_value=None,
            optional=True,
            human_name="Facet Row",
            short_description="Column name for row facetting",
            visibility="protected"
        ),
        'facet_col': StrParam(
            default_value=None,
            optional=True,
            human_name="Facet Column",
            short_description="Column name for column facetting",
            visibility="protected"
        ),
        'facet_col_wrap': IntParam(
            default_value=0,
            optional=True,
            human_name="Facet Col Wrap",
            short_description="Maximum number of facet columns to display",
            visibility="protected"
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
        #hover params
        'hover_name': StrParam(
            default_value=None,
            optional=True,
            human_name="Hover Name",
            short_description="Column name for hover text",
            visibility="protected"
        ),
        'hover_data': StrParam(
            default_value=None,
            optional=True,
            human_name="Hover Data",
            short_description="Column names for additional hover data",
            visibility="protected"
        ),
        'custom_data': StrParam(
            default_value=None,
            optional=True,
            human_name="Custom Data",
            short_description="Column names for custom data",
            visibility="protected"
        ),
        'animation_frame': StrParam(
            default_value=None,
            optional=True,
            human_name="Animation Frame",
            short_description="Column name for animation frame",
            visibility="protected"
        ),
        'animation_group': StrParam(
            default_value=None,
            optional=True,
            human_name="Animation Group",
            short_description="Column name for grouping data points in animations",
            visibility="protected"
        ),
        'category_orders': StrParam(
            default_value=None,
            optional=True,
            human_name="Category Orders",
            short_description="Ordering of categories for X and Y axes",
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
        'range_x': StrParam(
            default_value=None,
            optional=True,
            human_name="X Axis Range",
            short_description="Set the range of the X axis",
            visibility="protected"
        ),
        'range_y': StrParam(
            default_value=None,
            optional=True,
            human_name="Y Axis Range",
            short_description="Set the range of the Y axis",
            visibility="protected"
        ),
        'width': IntParam(
            default_value=None,
            optional=True,
            human_name="Width",
            short_description="Width of the graph",
            visibility="protected"
        ),
        'height': IntParam(
            default_value=None,
            optional=True,
            human_name="Height",
            short_description="Height of the graph",
            visibility="protected"
        ),}

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        pass