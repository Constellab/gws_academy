from gws_core import (ProcessSpec, Protocol, ResourceDownloaderHttp, Sink,
                      TableColumnScaler, TableColumnsDeleter, TableImporter,
                      protocol_decorator)

from .pca import PCAExample


@protocol_decorator("PCADemo", hide=True)
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
        sink_1: ProcessSpec = self.add_process(Sink, 'sink_1')

        self.add_connectors([
            (file_downloader >> 'resource', table_importer << 'source'),
            (table_importer >> 'target', column_deleter << 'source'),
            (column_deleter >> 'target', table_scaler << 'source'),
            (table_scaler >> 'target', pca << 'source'),
            (pca >> 'target', sink_1 << Sink.input_name),
        ])
