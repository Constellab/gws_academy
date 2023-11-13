
from io import StringIO
import pandas as pd
import math
from gws_core import Table, TaskRunner, BaseTestCase, PlotlyResource, ConfigParams
from gws_academy.NcbiGeneToEntrezID.ncbi_gene_to_entrez_id import NCBIGeneToENTREZId
from numpy import NaN

class TestNCBIGeneToENTREZId(BaseTestCase):
    def test_gene_to_entrez_id(self):
        df = pd.DataFrame({'gene_name' : ['LINC01578','CXCR4']})

        runner = TaskRunner(
            task_type=NCBIGeneToENTREZId,
            inputs={'input_table': Table(df)},
            params={
                'gene_names': 'gene_name',
                'gene_id' : "gene_id"
            }
        )

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_output = Table(pd.DataFrame({
            'gene_name' : ['LINC01578','CXCR4'],
        'gene_id' : [float('nan'),'7852']}))
        #table_output['gene_id'] = table_output['gene_id'].astype(float)

        self.assertTrue(table_output.equals(expected_output))

    # Ajoutez d'autres méthodes de test pour tester différentes configurations et paramètres...
