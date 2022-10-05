
from gws_academy import OneWayAnova
from gws_core import BaseTestCase, Table, TaskRunner
from pandas import DataFrame


class TestTableFactor(BaseTestCase):

    async def test_process(self):
        dataframe = DataFrame({'A': [0, 1, 2],'B': [9, 7, 5]})
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
