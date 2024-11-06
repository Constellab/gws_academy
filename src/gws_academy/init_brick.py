

from gws_core import (CurrentUserService, Logger, Scenario,
                      ScenarioCreationType, ScenarioProxy, User)
from gws_core.app import app

from .pca.pca_protocol import PCADemo
from .solutions.blast.blast_protocol import BlastProtocolDemo


@app.on_event("startup")
async def startup_event():

    try:
        if Scenario.select().count() > 0:
            return

        CurrentUserService.set_current_user(User.get_sysuser())

        # Execute simple PCA
        scenario_proxy = ScenarioProxy(protocol_type=PCADemo, title='PCA demo',
                                       creation_type=ScenarioCreationType.MANUAL)
        scenario_proxy.add_to_queue()

        # Execute blast
        scenario_proxy_2 = ScenarioProxy(
            protocol_type=BlastProtocolDemo, title='Blast demo',
            creation_type=ScenarioCreationType.MANUAL)
        scenario_proxy_2.add_to_queue()

        CurrentUserService.set_current_user(None)

    except Exception as err:
        Logger.error(
            f"Error while creating the gws academy demo scenario. Error: {err}")
        CurrentUserService.set_current_user(None)
