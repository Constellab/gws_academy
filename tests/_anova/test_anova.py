
from gws_academy import OneWayAnova
from gws_core import BaseTestCase, Table, TaskRunner
from pandas import DataFrame


class OneWayAnovaTest(BaseTestCase):

    async def test_process(self):
        dataframe = DataFrame(
            {'col1': [0, 1, 2, 2],
             'col2': [0, 0, 2, 5],
             'col3': [1, 0, 2, 4],
             'col4': [0.1, 0.9, 6.2, 11.9],
             'col5': [-0.2, 1.1, 5.9, 12.3]})
        table = Table(dataframe)

        # run trainer
        tester = TaskRunner(
            params={},
            inputs={'table': table},
            task_type=OneWayAnova
        )
        outputs = await tester.run()
        result = outputs['result']

        table = result.get_stats_table()
        print(table)

        data: DataFrame = table.get_data()

        self.assertAlmostEqual(data.iat[0, 0], 0.868247, 3)  # compare with 3 digits
        self.assertAlmostEqual(data.iat[0, 1], 0.50545, 3)
