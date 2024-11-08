from gws_core import (OutputTask, ProcessSpec, Protocol,
                      ResourceDownloaderHttp, protocol_decorator)

from .blast import SoBlast


@protocol_decorator("BlastProtocolDemo", hide=True)
class BlastProtocolDemo(Protocol):

    def configure_protocol(self) -> None:
        file_downloader: ProcessSpec = self.add_process(ResourceDownloaderHttp, 'file_downloader', {
            'link': 'https://storage.gra.cloud.ovh.net/v1/AUTH_a0286631d7b24afba3f3cdebed2992aa/opendata/gws_academy/mouse.1.protein.faa.gz',
            'uncompress': 'no'
        })

        blast = self.add_process(SoBlast, 'blast', {
            'head': 11
        })

        # define the protocol output
        output_1: ProcessSpec = self.add_process(OutputTask, 'output_1')

        self.add_connectors([
            (file_downloader >> 'resource', blast << 'input_file'),
            (blast >> 'blast_result', output_1 << OutputTask.input_name),
        ])
