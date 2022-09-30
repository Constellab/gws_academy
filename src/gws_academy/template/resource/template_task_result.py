# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com

from gws_core import (ConfigParams, ResourceSet, ScatterPlot2DView,
                      resource_decorator, view)

# *****************************************************************************
#
# AnovaResult
#
# *****************************************************************************


@resource_decorator("AcademyTemplateTaskResult", human_name="Result of academy template task",
                    short_description="Result of academy template task", hide=True)
class AcademyTemplateTaskResult(ResourceSet):
    """
    Result of academy template task

    Describe your resource using Markdown (https://www.markdownguide.org/)
    """

    # ...
    # ... def custom_methods():
    # ...

    @view(view_type=ScatterPlot2DView, human_name='Template scatter plot', short_description='Template scatter plot')
    def view_scatter_plot(self, params: ConfigParams) -> dict:
        """
        View 2D score plot
        """

        view_ = ScatterPlot2DView()

        view_.add_series(
            x=[0, 1, 2, 3, 4],
            y=[0, 1, 2, 3, 4],
        )
        view_.x_label = 'time'
        view_.y_label = 'distance'

        return view_
