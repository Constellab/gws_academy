# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams,  PlotlyResource,
                      StrParam,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                     FloatParam)

from gws_academy.Plotly.PlotlyTask.plotly_task import PlotlyTask
import pandas as pd

import plotly.express as px
# from plotly.subplots import make_subplots


@task_decorator("PlotlyScatterplot", human_name="Scatterplot Plotly",
                short_description="Scatter plot from plotly(px)")
class PlotlyScatterplot(PlotlyTask):

    input_specs = PlotlyTask.input_specs

    output_specs = PlotlyTask.output_specs


    config_specs ={
        **PlotlyTask.config_specs_d2,
        'size': StrParam(
            default_value=None,
            optional=True,
            human_name="size",
            short_description=" Values from this column are used to assign mark sizes"
        ),
        'opacity' : FloatParam(
            default_value=None,
            visibility='protected',
            human_name="opacity",
            short_description="float: opacity of the marks",
            optional = True
        ),
        'size_max' : IntParam(
            default_value=20,
            optional=True,
            visibility='protected',
            short_description= "int: maximum size of the marks",
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
        **PlotlyTask.symbol,
        **PlotlyTask.color_continuous,
        **PlotlyTask.trendline,
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


        fig = px.scatter(
            data_frame=dataframe,
            x=params['x'],
            y=params['y'],
            title=params['title'],
            color=params['color'],
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
            labels=labels,
            orientation=params['orientation'],
            #color_discrete #color_discrete_map #color_continuous_scale
            #range_color #color_continuous_midpoint
            #symbol_sequence #symbol_map
            opacity=params['opacity'],
            size_max=params['size_max'],
            marginal_x=params["marginal_x"],
            marginal_y=params["marginal_y"],
            #trendline=params["trendline"],
            #trendline_color_override=params["trendline_color_override"],
            #trendline_scope=params['trendline_scope'],
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
