import pandas as pd
import numpy as np
from gws_core import Table, TaskRunner, BaseTestCase
from gws_academy.Describe.describe import Describe


class TestDescribe(BaseTestCase):
    def test_describe(self):
        s = pd.Series([1, 2, 3])

        runner = TaskRunner(
            task_type=Describe,
            inputs={'input_table': Table(s)})

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_table = Table(s.describe())
        self.assertTrue(table_output.equals(expected_table))

    def test_describe_1(self):
        s = pd.Series(['a', 'a', 'b', 'c'])

        runner = TaskRunner(
            task_type=Describe,
            inputs={'input_table': Table(s)})

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_table = Table(s.describe())
        self.assertTrue(table_output.equals(expected_table))

    def test_describe_2(self):
        s = pd.Series([
            np.datetime64("2000-01-01"),
            np.datetime64("2010-01-01"),
            np.datetime64("2010-01-01")
        ])

        runner = TaskRunner(
            task_type=Describe,
            inputs={'input_table': Table(s)})

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_table = Table(s.describe())
        self.assertTrue(table_output.equals(expected_table))

    def test_describe_3(self):
        df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                   'numeric': [1, 2, 3],
                   'object': ['a', 'b', 'c']
                  })

        runner = TaskRunner(
            task_type=Describe,
            inputs={'input_table': Table(df)})

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_table = Table(df.describe())
        self.assertTrue(table_output.equals(expected_table))


    def test_describe_4(self):
        df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                   'numeric': [1, 2, 3],
                   'object': ['a', 'b', 'c']
                  })

        runner = TaskRunner(
            task_type=Describe,
            params={'include_NaN' : True},
            inputs={'input_table': Table(df)})

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_table = Table(df.describe(include='all'))
        self.assertTrue(table_output.equals(expected_table))

    def test_describe_5(self):
        df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                   'numeric': [1, 2, 3],
                   'object': ['a', 'b', 'c']
                  })

        runner = TaskRunner(
            task_type=Describe,
            inputs={'input_table': Table(df.numeric)})

        outputs = runner.run()
        table_output = outputs['output_table']
        expected_table = Table(df.numeric.describe())
        self.assertTrue(table_output.equals(expected_table))
