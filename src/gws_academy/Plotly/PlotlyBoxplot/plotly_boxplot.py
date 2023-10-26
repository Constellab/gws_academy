# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam, FloatParam, ListParam)

from gws_academy.Plotly.PlotlyTask.plotly_task import PlotlyTask

import pandas as pd

import plotly.express as px


@task_decorator(unique_name="PlotlyBoxplot", human_name="Boxplot Plotly",
                short_description="Boxplot from Plotly")
class PlotlyBoxplot(PlotlyTask):
    input_specs = PlotlyTask.input_specs

    output_specs = PlotlyTask.output_specs

    config_specs = {
        **PlotlyTask.config_specs_d2,
        #base params
        'boxmode': StrParam(
            default_value='group',
            optional=True,
            human_name="Box Mode",
            allowed_values=['group','overlay'],
            short_description="Box mode ('group' or 'overlay')",
        ),
        'points' : StrParam(
            default_value='outliers',
            optional=True,
            human_name= "points",
            short_description="shows outliers",
            allowed_values=["outliers", 'suspectoutliers', 'all', False]
        ),
        'notched' : BoolParam(
            default_value=False,
            optional=True,
            human_name="notches",
            short_description="if True, boxes are drawn with notches"
        ),
    }


    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        dataframe = pd.DataFrame(inputs['input_table'].get_data())
        for key, i  in params.items() :
            if i == "" :
                params[key]= None
        if params['label_columns'] is not None :
            labels = dict(zip(params['label_columns'], params['label_text']))
        else:
            labels = None


        # Créez le graphique à l'aide de px.box
        fig = px.box(
            data_frame=dataframe,
            #base params
            x=params['x'],
            y=params['y'],
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
            #animation params
            animation_frame=params['animation_frame'],
            animation_group=params['animation_group'],
            #layout params
            labels = labels,
            category_orders=params['category_orders'],
            color_discrete_sequence=params['color_discrete_sequence'],
            color_discrete_map=params['color_discrete_map'],
            orientation=params['orientation'],
            log_x=params['log_x'],
            log_y=params['log_y'],
            range_x=params['range_x'],
            range_y=params['range_y'],
            template=params['template'],
            width=params['width'],
            height=params['height'],
            #specific params
            boxmode=params['boxmode'],
            custom_data=params['custom_data'],
            notched=params['notched'],
            points=params['points'],
        )

        # Mise à jour des axes
        fig.update_xaxes(title=params['x_axis_name'])
        fig.update_yaxes(title=params['y_axis_name'])

        return {"output_plot": PlotlyResource(fig)}
