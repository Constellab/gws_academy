from gws_core import JSONDict, TaskRunner, BaseTestCase, JSONImporter, File
from gws_academy.IdToBiomass.id_to_biomass import IdToBiomass

class TestIdToBiomass(BaseTestCase) :

    def test_id_to_biomass_10FTHF5GLUtl(self):
        modele : JSONDict = JSONImporter.call(File("data/model.json"))

        runner = TaskRunner(task_type= IdToBiomass,
            inputs={'input_json' : modele},
            params= {'id' : "10FTHF5GLUtl"})

        output = runner.run()

        json_output = output['output_json']

        expected_json : JSONDict= JSONImporter.call(File("data/IdToBiomass/model_10FTHF5GLUtl.json"))

        self.assert_json(expected_json, json_output)