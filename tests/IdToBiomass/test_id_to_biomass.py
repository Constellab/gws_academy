from gws_core import JSONDict, TaskRunner, BaseTestCase, JSONImporter, File
from gws_academy.IdToBiomass.id_to_biomass import IdToBiomass


class TestIdToBiomass(BaseTestCase):

    def test_id_to_biomass_CYOOm3i(self):
        modele: JSONDict = JSONImporter.call(File("data/truncated_model_2.json"))

        runner = TaskRunner(task_type=IdToBiomass,
                            inputs={'input_json': modele},
                            params={'id': "CYOOm3i"})

        output = runner.run()

        json_output = output['output_json']

        expected_json: JSONDict = JSONImporter.call(File("data/IdToBiomass/model_CYOOm3i.json"))

        self.assertTrue(expected_json.equals(json_output))

    def test_id_to_biomass_eee(self):
        modele: JSONDict = JSONImporter.call(File("data/truncated_model_2.json"))

        runner = TaskRunner(task_type=IdToBiomass,
                            inputs={'input_json': modele},
                            params={'id': "eee"})

        # Utiliser assertRaises pour vérifier qu'une exception est levée
        with self.assertRaises(Exception) :
            output = runner.run()
