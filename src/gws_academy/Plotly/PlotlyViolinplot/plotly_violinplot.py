# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam, FloatParam, ListParam)

from gws_academy.Plotly.PlotlyTask.PlotlyTask import PlotlyTask

import pandas as pd

import plotly.express as px


@task_decorator(unique_name="PlotlyViolinplot", human_name="Violinplot Plotly",
                short_description="")
class PlotlyViolinplot(Task):
    input_specs = PlotlyTask.input_specs

    output_specs = PlotlyTask.output_specs

    config_specs = {
        #base params
        'color': StrParam(
            default_value=None,
            optional=True,
            human_name="Color",
            short_description="Column name for color encoding",
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
        'violinmode': StrParam(
            default_value='group',
            optional=True,
            human_name="Violin Mode",
            allowed_values=['group','overlay'],
            short_description="violin mode ('group' or 'overlay')",
        ),
        'points' : StrParam(
            default_value='outliers',
            optional=True,
            human_name= "points",
            short_description="shows outliers",
            allowed_values=["outliers", 'suspectoutliers', 'all', False]
        ),
        'box' : BoolParam(
            default_value=False,
            optional=True,
            human_name="notches",
            short_description="if True, boxes are drawn with notches"

        ),
    }


    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        def is_empty(self, params : ConfigParams) -> ConfigParams :
            for key, i in params.items() :
                if i == "" :
                    params[key] = None
            return params
        dataframe = pd.DataFrame(inputs['input_table'].get_data())
        params = is_empty(self, params)
        # Créez le graphique à l'aide de px.box
        fig = px.violin(
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
            labels = dict(zip(params['label_columns'], params['label_text'])),
            #animation params
            animation_frame=params['animation_frame'],
            animation_group=params['animation_group'],
            category_orders=params['category_orders'],
            color_discrete_sequence=params['color_discrete_sequence'],
            color_discrete_map=params['color_discrete_map'],
            orientation=params['orientation'],
            violinmode=params['violinmode'],
            log_x=params['log_x'],
            log_y=params['log_y'],
            range_x=params['range_x'],
            range_y=params['range_y'],
            points=params['points'],
            box=params["box"],
            template=params['template'],
            width=params['width'],
            height=params['height']
        )

        # Mise à jour des axes
        fig.update_xaxes(title=params['x_axis_name'])
        fig.update_yaxes(title=params['y_axis_name'])

        return {"output_plot": PlotlyResource(fig)}
