import json

from parsing.data_model import DataModel


class System(DataModel):

    def __init__(self):
        super().__init__()

    def get_path(self):
        return "views/Configuration_System/"

    def get_menu_list(self):
        return ["Configuration", "System"]

    def deserialize(self, json_response):
        response_dict = json.loads(json_response)
        assert type(response_dict) is dict

        widget_list = self.dict_to_widgets(response_dict)
        for widget in widget_list:
            widget.values

        return





