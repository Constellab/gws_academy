# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com

from typing import List

from gws_core import (ConfigParams, ListRField, Resource, ScatterPlot2DView,
                      StrParam, StrRField, Table, TableView, TechnicalInfo,
                      resource_decorator, view)


@resource_decorator("SimpleList", human_name="List of floats",
                    short_description="Resource that contanis a list of floats", hide=True)
class SimpleList(Resource):
    """
    This is the solution for the tutorial 'Create your first Resource' :
    https://hub.gencovery.com/bricks/gws_academy/latest/doc/create-your-first-resource
    """

    numbers: List[float] = ListRField(include_in_dict_view=True)

    description: str = StrRField()

    def add_number(self, value: float) -> None:
        self.numbers.append(value)

    @view(view_type=TableView, human_name='View numbers as table', default_view=True)
    def view_as_table(self, params: ConfigParams) -> TableView:
        table = Table(self.numbers)
        return TableView(table)

    @view(view_type=ScatterPlot2DView, human_name='View numbers as scatter plot',
          short_description='Visualize you data in a great chart',
          specs={'y_label': StrParam(human_name='Name of the y axis')})
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
