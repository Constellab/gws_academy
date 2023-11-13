
from io import StringIO
import pandas as pd
from gws_core import Table, TaskRunner, BaseTestCase, PlotlyResource, ConfigParams
from gws_academy.NcbiGeneToEntrezID.ncbi_gene_to_entrez_id import NCBIGeneToENTREZId


class TestLineplot(BaseTestCase):
    def test_line(self):
        # Créez un DataFrame de test
        data = """DDIT4
VEGFA
THBS1
SLC2A3
G0S2
HIF1A
SLC25A37
GABARAPL1
CEBPB
FOSL2
ZFP36L1
IER3
MAP3K8
JARID2
IRF2BP2
HBB
ARL4C
JUN
LINC01578
CXCR4
NEAT1
HLA-DQA2
OSM
BTG1
THBD"""
        df = pd.read_csv(StringIO(data), header=True)

        runner = TaskRunner(
            task_type=NCBIGeneToENTREZId,
            inputs={'input_table': Table(df)},
            params={

            }
        )

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_output = pd.read_csv(StringIO("""gene_name,gene_id
DDIT4,54541
VEGFA,7422
THBS1,7057
SLC2A3,6515
G0S2,50486
HIF1A,3091
SLC25A37,51312
GABARAPL1,23710
CEBPB,1051
FOSL2,2355
ZFP36L1,677
IER3,8870
MAP3K8,1326
JARID2,3720
IRF2BP2,359948
HBB,3043
ARL4C,10123
JUN,3725
LINC01578,
CXCR4,7852
NEAT1,283131
HLA-DQA2,3118
OSM,5008
BTG1,694
THBD,7056"""), header=True)

        self.assertTrue(table_output.equals(expected_output))

    # Ajoutez d'autres méthodes de test pour tester différentes configurations et paramètres...
