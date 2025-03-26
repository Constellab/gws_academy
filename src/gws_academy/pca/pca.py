

from gws_core import (ConfigParams, InputSpec, InputSpecs, IntParam, ConfigSpecs,
                      OutputSpec, OutputSpecs, Table, Task, TaskInputs,
                      TaskOutputs, task_decorator)
from sklearn.decomposition import PCA


@task_decorator("PCAExample", human_name="PCA example",
                short_description="Apply PCA to a table")
class PCAExample(Task):

    input_specs = InputSpecs({'source': InputSpec(Table, human_name="Table",
                                                  short_description="The input table")})
    output_specs = OutputSpecs({'target': OutputSpec(Table, human_name="Result",
                                                     short_description="The output table")})

    config_specs = ConfigSpecs({
        'nb_components': IntParam(default_value=2, min_value=2)
    })

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        """ Run the task """

        table: Table = inputs['source']

        # Specify the number of components you want to retain (e.g., 2 for 2D visualization)
        pca = PCA(n_components=params['nb_components'])

        pca_result = pca.fit_transform(table.get_data())

        # create the output table from the dataframe
        output_table = Table(pca_result)

        # keep the row tags from the input table
        output_table.set_all_row_tags(table.get_row_tags())

        # return the output table
        return {'target': output_table}
