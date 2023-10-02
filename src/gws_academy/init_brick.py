

from gws_core import (CurrentUserService, Experiment, ExperimentService,
                      Logger, QueueService, User)
from gws_core.app import app

from .pca.pca_protocol import PCADemo


@app.on_event("startup")
async def startup_event():

    try:
        if Experiment.select().count() > 0:
            return

        CurrentUserService.set_current_user(User.get_sysuser())

        experiment = ExperimentService.create_experiment_from_protocol_type(PCADemo, title='PCA demo')

        QueueService.add_experiment_to_queue(experiment_id=experiment.id)
        CurrentUserService.set_current_user(None)

    except Exception as err:
        Logger.error(f"Error while creating the gws academy demo experiment. Error: {err}")
