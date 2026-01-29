

from gws_core import (AuthenticateUser, Logger, Scenario, ScenarioCreationType,
                      ScenarioProxy, event_listener, EventListener, Event)
from gws_core.app import app
from gws_core.model.event.event_listener import

from .pca.pca_protocol import PCADemo
from .solutions.blast.blast_protocol import BlastProtocolDemo


@event_listener
class GwsAcademyListener(EventListener):
    """Listener to create a demo scenario on startup if no scenario exists."""

    def handle(self, event: Event) -> None:
        if event.type == "system" and event.action == "started":
            self._create_demo_scenario_if_none_exists()

    def _create_demo_scenario_if_none_exists(self) -> None:
        """Create a demo scenario if no scenario exists yet."""
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
