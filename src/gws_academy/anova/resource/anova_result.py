# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com

import pandas
from gws_core import (ConfigParams, ResourceSet, ScatterPlot2DView, Table,
                      resource_decorator, view)

# *****************************************************************************
#
# AnovaResult
#
# *****************************************************************************


@resource_decorator("OneWayAnovaResult", human_name="Result of one way anova",
                    short_description="Result of one way anova", hide=True)
class OneWayAnovaResult(ResourceSet):
    """
    Result of one way anova

    Describe your resource using Markdown (https://www.markdownguide.org/)
    """

    STATS_RESULT_NANE = "Anova statistics"

    def __init__(self, stat_result=None):
        super().__init__()
        if stat_result is not None:
            data = pandas.DataFrame([[stat_result.statistic, stat_result.pvalue]], columns=["statistics", "name"])
            table = Table(data=data)
            table.name = self.STATS_RESULT_NANE
            self.add_resource(table)

    def get_stats_table(self):
        return self.get_resource(self.STATS_RESULT_NANE)
