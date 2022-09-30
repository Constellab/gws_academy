import os

from gws_academy import OneWayAnova
from gws_core import (BaseTestCase, ConfigParams, Dataset, File, Settings,
                      TableImporter, TaskRunner, ViewTester)
from pandas import DataFrame


class OneWayAnovaTest(BaseTestCase):

    async def test_process(self):
        settings = Settings.retrieve()
        path = settings.get_variable("gws_academy:testdata_dir")  # see settings.josn file

        table = TableImporter.call(File(path=os.path.join(path, "data.csv")), {
            "delimiter": ",",
            "header": 0,
        })

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
