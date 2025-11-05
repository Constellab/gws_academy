

from gws_core import (AuthenticateUser, Logger, Scenario, ScenarioCreationType,
                      ScenarioProxy)
from gws_core.app import app

from .pca.pca_protocol import PCADemo
from .solutions.blast.blast_protocol import BlastProtocolDemo


@app.on_event("startup")
async def startup_event():

    try:
        if Scenario.select().count() > 0:
            return

        with AuthenticateUser.system_user():

            # Execute simple PCA
            scenario_proxy = ScenarioProxy(protocol_type=PCADemo, title='PCA demo',
                                           creation_type=ScenarioCreationType.MANUAL)
            scenario_proxy.add_to_queue()

            # Execute blast
            scenario_proxy_2 = ScenarioProxy(
                protocol_type=BlastProtocolDemo, title='Blast demo',
                creation_type=ScenarioCreationType.MANUAL)
            scenario_proxy_2.add_to_queue()

    except Exception as err:
        Logger.error(
            f"Error while creating the gws academy demo scenario. Error: {err}")
