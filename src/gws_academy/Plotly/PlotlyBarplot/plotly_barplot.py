# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams,  PlotlyResource,
                      StrParam,
                      TaskInputs, TaskOutputs, task_decorator,)

from gws_academy.Plotly.PlotlyTask.plotly_task import PlotlyTask
import pandas as pd

import plotly.express as px


@task_decorator(unique_name="PlotlyBarplot", human_name="Barplot Plotly",
                short_description="Bar plot and Stack bar plot from plotly")
class PlotlyBarplot(PlotlyTask):
    input_specs = PlotlyTask.input_specs

    output_specs = PlotlyTask.output_specs

    config_specs = {
        **PlotlyTask.config_specs_d2,
        #base params
        **PlotlyTask.bar_box_violin,
        'barmode': StrParam(
            default_value='relative',
            optional=True,
            human_name="Box Mode",
            allowed_values=["relative", 'group','overlay'],
            short_description="In 'relative' mode, bars are stacked above zero for positive values and below zero for negative values. In 'overlay' mode, bars are drawn on top of one another. In 'group' mode, bars are placed beside each other.",
            visibility="protected"
        ),
        **PlotlyTask.config_specs_layout,
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        dataframe = pd.DataFrame(inputs['input_table'].get_data())
        for key, i  in params.items() :
            if i == "" :
                params[key]= None
        if params['label_columns'] is not None :
            labels = dict(params['label_columns'], params['label_text'])
        else:
            labels = None

        # Créez le graphique à l'aide de px.box
        fig = px.bar(
            data_frame=dataframe,
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
            custom_data=params['custom_data'],
            animation_frame=params['animation_frame'],
            animation_group=params['animation_group'],
            category_orders=params['category_orders'],
            labels = labels,
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
