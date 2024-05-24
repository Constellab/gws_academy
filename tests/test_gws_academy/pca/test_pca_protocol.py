from gws_academy.pca.pca_protocol import PCADemo
from gws_core import BaseTestCase, IExperiment, Table


# test_pca_protocol
class TestPCAProtocol(BaseTestCase):

    def test_pca_protocol(self):
        # create the input table
        experiment = IExperiment(PCADemo)

        experiment.run()

        self.assertTrue(experiment.is_success())

        # get the output table
        result_table: Table = experiment.get_protocol().get_process('sink_1').get_input('resource')

        self.assertEqual(len(result_table.column_names), 2)
