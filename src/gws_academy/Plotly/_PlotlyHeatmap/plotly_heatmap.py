# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task,
                      TaskInputs, TaskOutputs, task_decorator, BoolParam,
                      ListParam)

import plotly.graph_objects as go
import plotly.figure_factory as ff
from scipy.spatial.distance import pdist, squareform
import pandas as pd
import numpy as np

@task_decorator(unique_name="PlotlyHeatmap", human_name="Heatmap Plot",
short_description="Heatmap with Plotly")

class PlotlyHeatmap(Task):
    input_specs = InputSpecs({'input_table': InputSpec(Table, human_name="input_table")})

    output_specs = OutputSpecs({'output_plot': OutputSpec(PlotlyResource, human_name="output graph")})

    config_specs = {
        'x' : ListParam(
            default_value=None,
            human_name="x labels",
            optional=True,
            short_description="labels for the x axis"
        ),
        'y' : ListParam(
            default_value=None,
            human_name="y labels",
            optional=True,
            short_description="labels for the y axis"
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
        'color_range_name': StrParam(
            default_value=None,
            optional=True,
            human_name="color scale name",
            short_description=""
        ),
        "color_scale" : StrParam(
            default_value=None,
            optional=True,
            allowed_values= ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance','blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg', 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl', 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric', 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys', 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet', 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges', 'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd'],
            human_name="color scale",
            short_description="Determine the color scale"
        ),
        'upper_dendrogram' : BoolParam()
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        df = pd.DataFrame(inputs['input_table'].get_data())

        # Filter out non-numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
        labels = numeric_df.columns.tolist()

        # Initialize figure by creating upper dendrogram
        fig = ff.create_dendrogram(numeric_df.values.transpose(), orientation='bottom', labels=labels)
        for i in range(len(fig['data'])):
            fig['data'][i]['yaxis'] = 'y2'

        # Create Side Dendrogram if needed
        if params['side_dendro']:
            dendro_side = ff.create_dendrogram(numeric_df.values.transpose(), orientation='right')
            for i in range(len(dendro_side['data'])):
                dendro_side['data'][i]['xaxis'] = 'x2'

            # Add Side Dendrogram Data to Figure
            for data in dendro_side['data']:
                fig.add_trace(data)

        # Create Heatmap
        if params['side_dendro']:
            dendro_leaves = dendro_side['layout']['yaxis']['ticktext']
            dendro_leaves = list(map(int, dendro_leaves))
        else:
            dendro_leaves = list(range(len(labels)))

        data_dist = pdist(numeric_df.values.transpose())
        heat_data = squareform(data_dist)
        heat_data = heat_data[dendro_leaves, :]
        heat_data = heat_data[:, dendro_leaves]

        heatmap = [
            go.Heatmap(
                x=dendro_leaves,
                y=dendro_leaves,
                z=heat_data,
                colorscale='Blues'
            )
        ]

        heatmap[0]['x'] = fig['layout']['xaxis']['tickvals']
        heatmap[0]['y'] = dendro_side['layout']['yaxis']['tickvals'] if side_dendro else dendro_leaves

        # Add Heatmap Data to Figure
        for data in heatmap:
            fig.add_trace(data)

        # Edit Layout
        fig.update_layout(width=800, height=800, showlegend=False, hovermode='closest')

        # Edit xaxis
        fig.update_layout(xaxis={'domain': [.15, 1],
                                'mirror': False,
                                'showgrid': False,
                                'showline': False,
                                'zeroline': False,
                                'ticks': ""})

        # Edit xaxis2
        fig.update_layout(xaxis2={'domain': [0, .15],
                                'mirror': False,
                                'showgrid': False,
                                'showline': False,
                                'zeroline': False,
                                'showticklabels': False,
                                'ticks': ""})

        # Edit yaxis
        fig.update_layout(yaxis={'domain': [0, .85],
                                'mirror': False,
                                'showgrid': False,
                                'showline': False,
                                'zeroline': False,
                                'showticklabels': False,
                                'ticks': ""
                                })

        # Edit yaxis2
        fig.update_layout(yaxis2={'domain': [.825, .975],
                                'mirror': False,
                                'showgrid': False,
                                'showline': False,
                                'zeroline': False,
                                'showticklabels': False,
                                'ticks': ""})


        return {"output_plot": PlotlyResource(fig)}
