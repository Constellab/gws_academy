
from gws_academy import AcademyTemplateTask
from gws_core import BaseTestCase, Table, TaskRunner
from pandas import DataFrame


class TemplateTest(BaseTestCase):

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
            params={'param1': 'blabla', 'param2': 1},
            inputs={'table': table},
            task_type=AcademyTemplateTask
        )
        outputs = await tester.run()
        result = outputs['result']

        # ...
        # ... Test the result here
        # ...
