# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com

import pandas
from gws_core import (ConfigParams, InputSpec, IntParam, OutputSpec, StrParam,
                      Table, Task, TaskInputs, TaskOutputs, task_decorator)
from scipy.stats import f_oneway

from ..resource.anova_result import OneWayAnovaResult


@task_decorator("OneWayAnova", human_name="One way anova",
                short_description="One way anova")
class OneWayAnova(Task):
    """
    Compute the one-way ANOVA test for multiple samples.

    The one-way ANOVA tests the null hypothesis that two or more groups have the same population mean.
    The test is applied to samples from two or more groups, possibly with differing sizes. It is a parametric
    version of the Kruskal-Wallis test.

    The ANOVA has important assumptions that must be satisfied in order for the associated p-value to be valid:
    * The samples are independent.
    * Each sample is from a normally distributed population.
    * The population standard deviations of the groups are all equal.This property is known as homoscedasticity.
    If these assumptions are not true for a given set of data, it may still be possible to use the Kruskal-Wallis H-test
    or the Alexander-Govern test although with some loss of power.

    * Input: a table containing the sample measurements, with the name of the samples.
    * Output: a table listing the correlation coefficient, and its associated p-value for each pairwise comparison testing.
    * Config Parameters:
      - `preselected_column_names`: List of columns to pre-select for pairwise comparisons. By default a maximum pre-defined number of columns are selected (see configuration).
      - `row_tag_key`: If give, this parameter is used for group-wise comparisons along row tags (see example below).

    ---

    # Example 1: Direct column comparisons

    Let's say you have the following table.

    | A | B | C |
    |---|---|---|
    | 1 | 5 | 3 |
    | 2 | 6 | 8 |
    | 3 | 7 | 5 |
    | 4 | 8 | 4 |

    This task performs population comparison of almost all the columns of the table
    (the first `500` columns are pre-selected by default).

    # Example 2: Advanced comparisons along row tags using `row_tag_key` parameter

    In general, the table rows represent real-world observations (e.g. measured samples) and columns correspond to
    descriptors (a.k.a features or variables).
    Theses rows (samples) may therefore be related to metadata information given by row tags as follows:

    | row_tags                 | A | B | C |
    |--------------------------|---|---|---|
    | Gender : M <br> Age : 10 | 1 | 5 | 3 |
    | Gender : F <br> Age : 10 | 2 | 6 | 8 |
    | Gender : F <br> Age : 10 | 8 | 7 | 5 |
    | Gender : X <br> Age : 20 | 4 | 8 | 4 |
    | Gender : X <br> Age : 10 | 2 | 7 | 5 |
    | Gender : M <br> Age : 20 | 4 | 1 | 4 |

    Actually, the column ```row_tags``` does not really exist in the table. It is just to show here the tags of the rows
    Here, the first row correspond to 10-years old male individuals.
    In this this case, we may be interested in only comparing several columns along row metadata tags.
    For instance, to compare gender populations `M`, `F`, `X` for each columns separately, you can therefore use the advance parameter `row_tag_key`=`Gender`.

    ---

    For more details, see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html
    """

    input_specs = {'table': InputSpec(Table, human_name="Table", short_description="The input table")}
    output_specs = {'result': OutputSpec(OneWayAnovaResult, human_name="Result",
                                         short_description="The output result")}

    config_specs = {}

    _is_nan_warning_shown = False

    async def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        """ Run the task """

        table = inputs['table']
        data = table.get_data()
        data = data.apply(pandas.to_numeric, errors='coerce')  # convert every value numeric if possible
        array_has_nan = data.isnull().sum().sum()
        data = data.to_numpy().T
        if array_has_nan:
            data = [[x for x in y if not np.isnan(x)] for y in data]  # remove nan values
            if not self._is_nan_warning_shown:
                self.log_warning_message("Data contain NaN values. NaN values are omitted.")
                self._is_nan_warning_shown = True

        stat_result = f_oneway(*data)
        result = OneWayAnovaResult(stat_result=stat_result)

        return {'result': result}
