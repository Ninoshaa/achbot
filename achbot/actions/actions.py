from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionWorkResponse(Action):
    def name(self) -> Text:
        return "action_work_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Custom response with a GIF
        dispatcher.utter_message(text="რა ხდება სამსახურში?", image="https://c.tenor.com/tkIbK5fyPPwAAAAC/tenor.gif")
        return []
