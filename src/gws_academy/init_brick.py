

from datetime import datetime, timedelta

from gws_core import (CurrentUserService, Experiment, FileDownloaderTask,
                      IExperiment, ProcessSpec, Protocol, Sink, TableImporter,
                      User, protocol_decorator)
from gws_core.app import app


@app.on_event("startup")
async def startup_event():
    if Experiment.select().count() > 0:
        return

    # check duration of the experiment
    start_date: datetime = datetime.now()

    CurrentUserService.set_current_user(User.get_sysuser())
    experiment: IExperiment = IExperiment(IrisDemo, title="Iris demo")

    experiment.run()
    CurrentUserService.set_current_user(None)

    end_date: datetime = datetime.now()
    duration: timedelta = end_date - start_date
    print(f"Duration: {duration}")


@protocol_decorator("IrisDemo", hide=True)
class IrisDemo(Protocol):

    def configure_protocol(self) -> None:
        file_downloader: ProcessSpec = self.add_process(FileDownloaderTask, 'file_downloader', {
            'file_url': 'https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv',
            'filename': 'iris.csv'
        })
        table_importer: ProcessSpec = self.add_process(TableImporter, 'table_importer', {
            'format_header_names': True,
            'metadata_columns': [{
                'column': 'species',
                'keep_in_table': True
            }]
        })

        # define the protocol output
        sink_1: ProcessSpec = self.add_process(Sink, 'sink_1')

        self.add_connectors([
            (file_downloader >> 'fs_node', table_importer << 'source'),
            (table_importer >> 'target', sink_1 << Sink.input_name),
        ])
