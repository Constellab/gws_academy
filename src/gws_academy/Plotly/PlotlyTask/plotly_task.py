from gws_core import (ConfigParams, InputSpec, InputSpecs, PlotlyResource,
                      OutputSpec, OutputSpecs, StrParam, Table, Task, FloatParam, ListParam,
                      TaskInputs, TaskOutputs, task_decorator, IntParam,
                      BoolParam)


# from plotly.subplots import make_subplots


# **PlotlyTAsk.config_specs

@task_decorator("PlotlyTask", human_name="Task Plotly",
                short_description="General Plotly Task")
class PlotlyTask(Task):
    css_colours = [
        "black", "white", "red", "green", "blue", "yellow", "orange", "pink",
        "purple", "brown", "gray", "cyan", "magenta", "lime", "teal", "navy"]
    css_color_range = [
        'aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose',   'balance',
        'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg', 'brwnyl',
        'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl', 'darkmint',
        'deep', 'delta', 'dense', 'earth', 'edge', 'electric', 'emrld', 'fall',
        'geyser', 'gnbu', 'gray', 'greens', 'greys', 'haline', 'hot', 'hsv',
        'ice', 'icefire', 'inferno', 'jet', 'magenta', 'magma', 'matter',
        'mint', 'mrybm', 'mygbm', 'oranges', 'orrd', 'oryel', 'oxy', 'peach',
        'phase', 'picnic', 'pinkyl', 'piyg', 'plasma', 'plotly3', 'portland',
        'prgn', 'pubu', 'pubugn', 'puor', 'purd', 'purp', 'purples', 'purpor',
        'rainbow', 'rdbu', 'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds',
        'solar', 'spectral', 'speed', 'sunset', 'sunsetdark', 'teal',
        'tealgrn', 'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid',
        'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd'
    ]
    input_specs = InputSpecs({'input_table': InputSpec(Table, human_name="input_table")})

    output_specs = OutputSpecs({'output_plot': OutputSpec(PlotlyResource, human_name="output graph")})
    config_specs_facet = {
        # facet params
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
        'facet_row_spacing': FloatParam(
            default_value=None,
            optional=True,
            human_name="Facet row Spacing",
            short_description="Spacing between facet rows, in paper units. Default is 0.03 or 0.0.7 when facet_col_wrap is used.",
            visibility="protected"
        ),
        'facet_col_spacing': FloatParam(
            default_value=None,
            optional=True,
            human_name="Facet col Spacing",
            short_description="Spacing between facet columns, in paper units. Default is 0.03 or 0.0.7 when facet_col_wrap is used.",
            visibility="protected"
        ), }
    config_specs_hover = {
        ## pas dans tous
        'hover_data': StrParam(
            default_value=None,
            optional=True,
            human_name="Hover Data",
            short_description="Column names for additional hover data",
            visibility="protected"
        ),
        # hover params
        'hover_name': StrParam(
            default_value=None,
            optional=True,
            human_name="Hover Name",
            short_description="Column name for hover text",
            visibility="protected"
        ),
    }
    layout = {
        'title': StrParam(
            default_value=None,
            optional=True,
            human_name="Title",
            short_description="Title of the graph"),
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
            allowed_values=[
                "ggplot2", "seaborn", "simple_white", "plotly", "plotly_dark",
                "presentation", "xgridoff", "ygridoff", "gridon", "none"
            ]
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
        ),
        'label_columns': ListParam(
            default_value=None,
            optional=True,
            visibility='protected',
            human_name='columns to label',
            short_description="one column per line, and same line for the text",
        ),
        'label_text': ListParam(
            default_value=None,
            optional=True,
            visibility="protected",
            human_name='text for labelling',
            short_description="text for labels, size should match 'colot to label'"
        ),
        **config_specs_facet,
        **config_specs_hover,
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
        'custom_data': StrParam(
            default_value=None,
            optional=True,
            human_name="Custom Data",
            short_description="Column names for custom data",
            visibility="protected"
        ),
    }
    config_specs_d2 = {
        # base params
        'x': StrParam(
            default_value=None,
            human_name="x-axis",
            short_description="The column name to use for the x-axis."
        ),
        'y': StrParam(
            default_value=None,
            optional=True,
            human_name="y-axis",
            short_description="Column name for the y-axis"),
        'color': StrParam(
            default_value=None,
            optional=True,
            human_name="Color",
            short_description="clomuns for the color"
        ),
        **layout
    }
    errors = { # line, bar, histogram
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
            short_description="Either a name of a column in data_frame, or a pandas Series . Values from this column or array_like are used to size x-axis error bars in the negative direction.",
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
    }
    pattern_shape = { # bar, histogram
        'pattern_shape' : None,
        'pattern_shape_sequence' : None,
        'pattern_shape_map' : None
    }
    color_continuous : { #bar, scatter
        'color_continuous_scale': StrParam(
            default_value=None,
            optional=True,
            human_name="Color Continuous scale",
            short_description="Custom continuous color scale ",
            visibility="protected"
        ),
        'color_continuous_midpoint': StrParam(
            default_value=None,
            optional=True,
            human_name="Color Continuous midpoint",
            short_description="Custom color mapping for discrete colors",
            visibility="protected"
        ),
        #'range_color' : None
    }
    symbol = { #scatter, line
        'symbol': StrParam(
            default_value=None,
            optional=True,
            human_name='symbol',
            short_description="",
        ),
        #symbol_sequence
        #symbol_map
        'text' : StrParam(
            default_value=None,
            optional=True,
            human_name="text labels",
            short_description="Either a name of a column in data_frame, or a pandas Series or array_like object. Values from this column or array_like appear in the figure as text labels."
        ),
        'render_mode': StrParam(
            default_value=None,
            optional=True,
            human_name="Render Mode",
            allowed_values=["svg", "webgl", "auto"],
            short_description="Set the render mode for points (e.g., 'webgl' or 'svg')",
            visibility="protected"
        ),
    }
    trendline = { #line
        'trendline': StrParam(
            default_value=None,
            optional=True,
            human_name="Trendline",
            short_description="Add a trendline to the plot",
            visibility="protected",
            allowed_values=['ols', 'lowess', 'rolling', 'expanding', 'ewm']
        ),
        #trendline_options
        'trendline_color_override' : StrParam(
            default_value=None,
            optional=True,
            visibility='protected',
            human_name="trendline color",
            short_description="color for the trendline",
            allowed_values=None
        ),
        'trendline_scope' : StrParam(
            default_value='trace',
            optional=True,
            visibility="protected",
            human_name='trendline scope',
            short_description=' one trend line per race',
            allowed_values=['trace', 'overall']
        ),
    }
    bar_opt = { #bar, histogram
                'opacity': FloatParam(
            default_value=None,
            optional=True,
            human_name="Opacity",
            short_description="Opacity of histogram bars (0 to 1).",
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
        #text_auto
    }
    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        pass
