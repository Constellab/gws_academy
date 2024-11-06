from gws_core import (OutputTask, ProcessSpec, Protocol,
                      ResourceDownloaderHttp, Table, TableColumnScaler,
                      TableColumnsDeleter, TableImporter, Viewer,
                      protocol_decorator)

from .pca import PCAExample


@protocol_decorator("PCADemo", hide=False)
class PCADemo(Protocol):

    def configure_protocol(self) -> None:
        file_downloader: ProcessSpec = self.add_process(ResourceDownloaderHttp, 'file_downloader', {
            'link': 'https://storage.gra.cloud.ovh.net/v1/AUTH_a0286631d7b24afba3f3cdebed2992aa/opendata/gws_academy/iris.csv',
        })
        table_importer: ProcessSpec = self.add_process(TableImporter, 'table_importer', {
            'format_header_names': True,
            'metadata_columns': [{
                'column': 'species',
                'keep_in_table': True
            }]
        })

        column_deleter: ProcessSpec = self.add_process(TableColumnsDeleter, 'column_deleter', {
            'filters': [{'name': 'species', 'is_regex': False}]
        })

        table_scaler: ProcessSpec = self.add_process(TableColumnScaler, 'table_scaler', {
            'scaling_function': 'standard'
        })

        pca = self.add_process(PCAExample, 'pca', {
            'nb_components': 2
        })

        # define the protocol output
        output_1: ProcessSpec = self.add_process(OutputTask, 'output_1')

        viewer = self.add_process(Viewer, 'viewer',
                                  {
                                      Viewer.resource_config_name: Table.get_typing_name(),
                                      Viewer.view_config_name: {
                                          "config_values": {
                                              "series": [
                                                  {
                                                      "name": "1",
                                                      "y": {
                                                              "type": "columns",
                                                              "selection": [
                                                                  "1"
                                                              ]
                                                      },
                                                      "x": {
                                                          "type": "columns",
                                                          "selection": [
                                                                  "0"
                                                          ]
                                                      }
                                                  }
                                              ],
                                              "x_axis_label": None,
                                              "y_axis_label": None
                                          },
                                          "view_method_name": "view_as_scatter_plot_2d"
                                      }
                                  })

        self.add_connectors([
            (file_downloader >> 'resource', table_importer << 'source'),
            (table_importer >> 'target', column_deleter << 'source'),
            (column_deleter >> 'target', table_scaler << 'source'),
            (table_scaler >> 'target', pca << 'source'),
            (pca >> 'target', output_1 << OutputTask.input_name),
            (pca >> 'target', viewer << Viewer.input_name)
        ])
