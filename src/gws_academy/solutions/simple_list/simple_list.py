
from gws_core import (ConfigParams, ConfigSpecs, ListRField, Resource,
                      ScatterPlot2DView, StrParam, StrRField, Table, TableView,
                      TechnicalInfo, resource_decorator, view)


@resource_decorator("SoSimpleList", human_name="List of floats",
                    short_description="Resource that contanis a list of floats", hide=True)
class SoSimpleList(Resource):
    """
    This is the solution for the tutorial 'Create your first Resource' :
    https://constellab.community/tech-doc/doc/tutorials/create-your-first-resource
    """

    numbers = ListRField(include_in_dict_view=True)

    description = StrRField()

    def __init__(self):
        super().__init__()
        self.numbers = []
        self.description = None

    def add_number(self, value: float) -> None:
        self.numbers.append(value)

    @view(view_type=TableView, human_name='View numbers as table', default_view=True)
    def view_as_table(self, params: ConfigParams) -> TableView:
        table = Table(self.numbers)
        return TableView(table)

    @view(view_type=ScatterPlot2DView, human_name='View numbers as scatter plot',
          short_description='Visualize you data in a great chart',
          specs=ConfigSpecs({'y_label': StrParam(human_name='Name of the y axis')}))
    def view_as_scatter_plot(self, params: ConfigParams) -> ScatterPlot2DView:
        # retrieve the y_name param
        y_label = params['y_label']

        # generate x values for the scatter plot
        x_list = range(1, len(self.numbers) + 1)

        # create the view
        scatter_plot_view = ScatterPlot2DView()

        # set the title to my scatter plot
        scatter_plot_view.set_title('My scatter plot !')

        # set the label of the y axis
        scatter_plot_view.y_label = y_label

        # add 1 serie to the view
        scatter_plot_view.add_series(x=x_list, y=self.numbers)

        # add the technical info
        scatter_plot_view.add_technical_info(TechnicalInfo('description', self.description))

        return scatter_plot_view
