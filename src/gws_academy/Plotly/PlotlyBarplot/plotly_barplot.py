# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam, FloatParam, ListParam)

import pandas as pd

import plotly.express as px


@task_decorator(unique_name="PlotlyBarplot", human_name="Barplot Plotly",
                short_description="")
class PlotlyBarplot(Task):
    input_specs = InputSpecs({'input_table': InputSpec(Table, human_name="input_table")})

    output_specs = OutputSpecs({'output_plot': OutputSpec(PlotlyResource, human_name="output graph")})

    config_specs = {
        #base params
        'x': StrParam(
            default_value=None,
            human_name="x-axis",
            short_description="The column name to use for the x-axis."
        ),
        'y_bar': StrParam(
            default_value=None,
            optional=True,
            human_name="y-axis",
            short_description="Column name for the y-axis"
        ),
        'y_stackbar' : ListParam(
            default_value=None,
            optional=True,
            human_name="y stackbar",
            short_description="list of y to stack"
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
        'color': StrParam(
            default_value=None,
            optional=True,
            human_name="Color",
            short_description="Column name for color encoding",
            visibility="protected"
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
        'color_discrete_sequence': StrParam(
            default_value=None,
            optional=True,
            human_name="Color Discrete Sequence",
            short_description="Custom color sequence for discrete colors",
            visibility="protected"
        ),
        'color_discrete_map': StrParam(
            default_value=None,
            optional=True,
            human_name="Color Discrete Map",
            short_description="Custom color mapping for discrete colors",
            visibility="protected"
        ),
        'orientation': StrParam(
            default_value='v',
            optional=True,
            human_name="Orientation",
            short_description="Orientation of the box plot ('v' for vertical, 'h' for horizontal)",
            allowed_values=['v', 'h'],
            visibility="protected"
        ),
        'barmode': StrParam(
            default_value='relative',
            optional=True,
            human_name="Box Mode",
            allowed_values=["relative", 'group','overlay'],
            short_description="Box mode ('group' or 'overlay')",
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
        'template': StrParam(
            default_value=None,
            optional=True,
            human_name="Template",
            short_description="Plotly template to use",
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
        )
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        dataframe = pd.DataFrame(inputs['input_table'].get_data())

        # Créez le graphique à l'aide de px.box
        fig = px.bar(
            data_frame=dataframe,
            x=params['x'],
            y=params['y_stackbar'],
            title=params['title'],
            color=params['color'],
            #facet params
            facet_row=params['facet_row'],
            facet_col=params['facet_col'],
            facet_col_wrap=params['facet_col_wrap'],
            facet_row_spacing=params['facet_row_spacing'],
            facet_col_spacing=params['facet_col_spacing'],
            #hover params
            hover_name=params['hover_name'],
            hover_data=params['hover_data'],
            custom_data=params['custom_data'],
            animation_frame=params['animation_frame'],
            animation_group=params['animation_group'],
            category_orders=params['category_orders'],
            color_discrete_sequence=params['color_discrete_sequence'],
            color_discrete_map=params['color_discrete_map'],
            orientation=params['orientation'],
            barmode=params['barmode'],
            log_x=params['log_x'],
            log_y=params['log_y'],
            range_x=params['range_x'],
            range_y=params['range_y'],
            template=params['template'],
            width=params['width'],
            height=params['height']
        )

        # Mise à jour des axes
        fig.update_xaxes(title=params['x_axis_name'])
        fig.update_yaxes(title=params['y_axis_name'])

        return {"output_plot": PlotlyResource(fig)}
