from abc import ABC, abstractmethod

from parsing.parser import Widget


class DataModel(ABC):

    @abstractmethod
    def get_path(self): pass

    @abstractmethod
    def get_menu_list(self): pass

    @abstractmethod
    def deserialize(self, json_response): pass

    @staticmethod
    def dict_to_widgets(response_dict):
        widget_list = list()
        if "widgets" in response_dict:
            widgets = response_dict["widgets"]

            for widget in widgets:
                widget_list.append(Widget(widget["title"], widget["columns"], widget["values"]))

        return widget_list
