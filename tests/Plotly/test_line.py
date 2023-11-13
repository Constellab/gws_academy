import pandas as pd
from gws_core import Table, TaskRunner, BaseTestCase, PlotlyResource, ConfigParams
from gws_academy.Plotly.PlotlyLine.plotly_line import PlotlyLine
import plotly.express as px


class TestLineplot(BaseTestCase):
    def test_line(self):
        # Créez un DataFrame de test
        df = pd.DataFrame({
            'x': [1],
            'y': [10],
            'z': [5.5],
            'a': ['b'],
            'c': ['d'],
            'e': ['f']
        })

        runner = TaskRunner(
            task_type=PlotlyLine,
            inputs={'input_table': Table(df)},
            params={
                'x': 'x',
                'y': 'y',
                'colour': 'z',
                'title': 'title',
                'x_axis_name': 'x_axis_name',
                'y_axis_name': 'y_axis_name',
                'log_x': True,
                'log_y': False,
                # Autres paramètres...
            }
        )

        outputs = runner.run()
        plot_output = outputs['output_plot']
        expected_output = px.line(data_frame=df, x='x', y='y', color='z',
                                     title='title', log_x=True, log_y=False)
        expected_output.update_yaxes(title='y_axis_name')
        expected_output.update_xaxes(title='x_axis_name')
        expected_output = PlotlyResource(expected_output)
        self.assertIsNotNone(plot_output.default_view(ConfigParams()).to_dict(ConfigParams()))

    # Ajoutez d'autres méthodes de test pour tester différentes configurations et paramètres...
