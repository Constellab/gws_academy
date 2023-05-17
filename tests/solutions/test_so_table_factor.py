
from gws_core import BaseTestCase, Table, TaskRunner
from pandas import DataFrame

from gws_academy.tutorials.table_factor.task.table_factor import TableFactor


class TestSoTableFactor(BaseTestCase):
    """This is the solution for the test of the tutorial 'Create your first task' :
      https://constellab.community/tech-doc/doc/tutorials/create-your-first-task

      This test needs to be run to check that your task was correctly implemented
    """

    def test_table_factor(self):
        # create the input table
        dataframe = DataFrame({'A': [0, 1, 2], 'B': [9, 7, 5]})
        table = Table(dataframe)

        # create and configure task runner
        tester = TaskRunner(
            task_type=TableFactor,
            inputs={'input_table': table},
            params={'factor': 2},
        )

        # run the task and retrieve the outputs
        outputs = tester.run()

        # get the output table
        result_table: Table = outputs['output_table']

        # create the expected table
        expected_dataframe = DataFrame({'A': [0, 2, 4], 'B': [18, 14, 10]})
        expected_table = Table(expected_dataframe)

        # compare the output table with the expected table
        self.assertTrue(result_table.equals(expected_table))
