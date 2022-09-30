import os

from gws_academy import AcademyTemplateTask
from gws_core import (BaseTestCase, ConfigParams, Dataset, File, Settings,
                      TableImporter, TaskRunner, ViewTester)


class TemplateTest(BaseTestCase):

    async def test_process(self):
        settings = Settings.retrieve()
        path = settings.get_variable("gws_academy:testdata_dir")  # see settings.josn file

        table = TableImporter.call(File(path=os.path.join(path, "data.csv")), {
            "delimiter": ",",
            "header": 0,
        })

        # run trainer
        tester = TaskRunner(
            params={'param1': 'blabla', 'param2': 1},
            inputs={'table': table},
            task_type=AcademyTemplateTask
        )
        outputs = await tester.run()
        result = outputs['result']
    s
        # ...
        # ... Test the result here
        # ...
