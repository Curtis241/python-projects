import json
import dpath
from abc import abstractmethod, ABC


class NoWidgetsInJsonResponse(Exception):
    pass


class NoWidgetsInDomainModel(Exception):
    pass


class Widget:

    def __init__(self, title, column_list, value_list):
        assert type(title) is str
        assert type(column_list) is list
        assert type(value_list) is list

        self.__title = title
        self.__columns = column_list
        self.__values = value_list

    @property
    def title(self):
        return self.__title

    @property
    def columns(self):
        return self.__columns

    @property
    def values(self):
        return self.__values


# class Parser(ABC):
#
#     def __init__(self): pass
#
#     @abstractmethod
#     def deserialize(self, data): pass



    # def deserialize_json(self, obj, data):
    #     response_dict = json.loads(data)
    #     if "widgets" not in response_dict or len(response_dict["widgets"]) == 0:
    #         raise NoWidgetsInJsonResponse()
    #
    #     if len(self.get_widgets()) == 0:
    #         raise NoWidgetsInDomainModel()
    #
    #     for defined_widget in self.get_widgets():
    #         for retrieved_widget in response_dict["widgets"]:
    #
    #             if defined_widget.title == retrieved_widget["title"]:
    #                 print(defined_widget.title)
    #                 print(retrieved_widget["columns"])



