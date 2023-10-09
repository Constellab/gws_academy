import pandas as pd
from gws_core import Table, TaskRunner, BaseTestCase, PlotlyResource
# Assurez-vous d'importer correctement votre classe PlotlyLine
from gws_academy.PlotlyScatterplot.plotly_scatterplot import PlotlyScatterplot


class TestPlotlyScatterplot(BaseTestCase):
    def test_plotly_line(self):
        # Créez un DataFrame de test
        df = pd.DataFrame({
            'x': [1, 2, 3, 4, 5],
            'y': [10, 20, 30, 40, 50],
            'colour': ['red', 'blue', 'green', 'yellow', 'purple'],
            'size': [5, 10, 15, 20, 25],
            'title': 'Scatter Plot Example',
            'x_axis_name': 'X-Axis',
            'y_axis_name': 'Y-Axis',
            'log_x': True,  # Exemple de paramètre log_x défini sur True
            'log_y': False,  # Exemple de paramètre log_y défini sur False
            # Autres paramètres...
        })

        runner = TaskRunner(
            task_type=PlotlyScatterplot,
            inputs={'input_table': Table(df)},
            params={
                'x': 'x',
                'y': 'y',
                'colour': 'colour',
                'size': 'size',
                'title': 'title',
                'x_axis_name': 'x_axis_name',
                'y_axis_name': 'y_axis_name',
                'log_x': 'log_x',
                'log_y': 'log_y',
                # Autres paramètres...
            }
        )

        outputs = runner.run()
        plot_output = outputs['output_plot']

        # Ajoutez des assertions pour vérifier que la sortie du graphique est correcte
        # Par exemple, vous pouvez vérifier les propriétés du graphique, la présence de points de données, etc.
        # Exemple d'assertion (vous devrez adapter cela en fonction de votre logique) :
        self.assertTrue(isinstance(plot_output, PlotlyResource))
        self.assertEqual(plot_output.figure.data[0].x, [1, 2, 3, 4, 5])
        self.assertEqual(plot_output.figure.data[0].y, [10, 20, 30, 40, 50])

    # Ajoutez d'autres méthodes de test pour tester différentes configurations et paramètres...
