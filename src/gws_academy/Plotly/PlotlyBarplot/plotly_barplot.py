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
    """
    Plotly Bar plot
    plotly.express.bar()

    please check : [https://plotly.com/python-api-reference/generated/plotly.express.bar.html]

    """
    input_specs = PlotlyTask.input_specs

    output_specs = PlotlyTask.output_specs

    config_specs = {
        **PlotlyTask.config_specs_d2,
        #specific params
        'base' : StrParam(
            default_value=None,
            optional=True,
            human_name="base",
            visibility="protected",
            short_description="Values from this column are used to position the base of the bar."
        ),
        **PlotlyTask.bar_opt,
        **PlotlyTask.errors,
        **PlotlyTask.color_continuous,
        **PlotlyTask.pattern_shape,
        **PlotlyTask.custom_data,
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
        fig = px.bar(
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
            base=params['base'],
            custom_data=params['custom_data'],
            #bar opt
            opacity=params['opacity'],
            barmode=params['barmode'],
            text_auto=params['text_auto'],
            #color continuous
            color_continuous_scale= params['color_continuous_scale'],
            color_continuous_midpoint= params['color_continuous_midpoint'],
            range_color=params['range_color'],
            #errors
            error_x=params['error_x'],
            error_x_minus=params['error_x_minus'],
            error_y=params['error_y'],
            error_y_minus=params['error_y_minus'],
            text=params['text'],
            #pattern shape
            pattern_shape= params['pattern_shape'],
            pattern_shape_map=params['pattern_shape_map'],
            pattern_shape_sequence=params['pattern_shape_sequence']
        )

        # Mise à jour des axes
        fig.update_xaxes(title=params['x_axis_name'])
        fig.update_yaxes(title=params['y_axis_name'])

        return {"output_plot": PlotlyResource(fig)}
