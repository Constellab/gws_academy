import pandas as pd

from gws_core import Table, TaskRunner, BaseTestCase
from gws_academy.Melt.melt import Melt


class TestMelt(BaseTestCase):

    def test_melt(self):
        df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                           'B': {0: 1, 1: 3, 2: 5},
                           'C': {0: 2, 1: 4, 2: 6}})

        runner = TaskRunner(task_type=Melt,
            params={
                'id_vars': ['A'],
                'value_vars': ['B'],
                'var_name': "myVarname",
                'value_name': 'myValname'
            },
            inputs={'input_table': Table(df)})

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_dataframe = Table(pd.melt(df, id_vars=['A'], value_vars=['B'],
                                           var_name='myVarname', value_name='myValname'))
        self.assertTrue(table_output.equals(expected_dataframe))
