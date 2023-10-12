from gws_core import BaseTestCase, TaskRunner, JSONDict, File, JSONImporter
from gws_academy.GeneRemoveVersion.gene_remove_version import GeneRemoveVersion
import simplejson as json
from cobra.io import model_to_dict, model_from_dict, from_json


class TestGeneRemoveVersion(BaseTestCase):
    def test_gene_remove_version(self):
        model : JSONDict = JSONImporter.call(File("data/truncated_model.json"))
        runner= TaskRunner(task_type=GeneRemoveVersion,
            params=None,
            inputs={'input_json' : model})

        outputs = runner.run()
        json_output = outputs['output_json']
        expected_model = open('data/GeneRemoveVersion/without_gene_version_truncated_model.json', 'r', encoding = 'UTF-8')
        expected_json : JSONDict = JSONImporter.call(File("data/GeneRemoveVersion/without_gene_version_truncated_model.json"))
        self.assert_json(json_output,expected_json)
