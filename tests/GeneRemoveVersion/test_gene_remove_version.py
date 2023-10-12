from gws_core import BaseTestCase, TaskRunner, JSONDict, File, JSONImporter
from gws_academy.GeneRemoveVersion.gene_remove_version import GeneRemoveVersion



class TestGeneRemoveVersion(BaseTestCase):
    def test_gene_remove_version(self):
        model : JSONDict = JSONImporter.call(File("data/truncated_model_2.json"))
        runner= TaskRunner(task_type=GeneRemoveVersion,
            params=None,
            inputs={'input_json' : model})

        outputs = runner.run()
        json_output : JSONDict = outputs['output_json']
        expected_json : JSONDict = JSONImporter.call(File("data/GeneRemoveVersion/without_gene_version_truncated_model_2.json"))
        self.assert_json(json_output, expected_json)
