from gws_core import Table, TaskRunner, BaseTestCase
from pandas import DataFrame
from gws_academy.tutorials.table_factor.task.table_factor import TableFactor


class TestTableFactor(BaseTestCase):
    def test_table_factor(self):
        dataframe : Table = Table(DataFrame({'A': [0, 1, 2],'B': [9, 7, 5]}))

        runner = TaskRunner(task_type=TableFactor,
            params={'factor':2},
            inputs = {'input_table' : dataframe})

        outputs = runner.run()

        table_output = outputs['output_table']

        expected_table = Table(DataFrame({'A': [0, 2, 4],'B': [18, 14, 10]}))

        self.assertTrue(table_output.equals( expected_table))