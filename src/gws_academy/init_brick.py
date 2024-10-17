

from gws_core import (CurrentUserService, Logger, QueueService, Scenario,
                      ScenarioService, User)
from gws_core.app import app

from .pca.pca_protocol import PCADemo
from .solutions.blast.blast_protocol import BlastProtocolDemo


@app.on_event("startup")
async def startup_event():

    try:
        # if Scenario.select().count() > 0:
        #     return

        CurrentUserService.set_current_user(User.get_sysuser())

        # Execute simple PCA
        scenario = ScenarioService.create_scenario_from_protocol_type(
            PCADemo, title='PCA demo')
        QueueService.add_scenario_to_queue(scenario_id=scenario.id)

        # Execute blast
        scenario_2 = ScenarioService.create_scenario_from_protocol_type(
            BlastProtocolDemo, title='Blast demo')
        QueueService.add_scenario_to_queue(scenario_id=scenario_2.id)

        CurrentUserService.set_current_user(None)

    except Exception as err:
        Logger.error(
            f"Error while creating the gws academy demo scenario. Error: {err}")
