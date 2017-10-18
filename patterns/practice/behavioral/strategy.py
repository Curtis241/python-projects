from __future__ import print_function
import types


class ResponseParser:

    def __init__(self, func=None):
        self.data = {}
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self): pass


def make_parser(self):
    print ("Parser: Make parser")
    print("Condition: Picking all Ford cars")
    print ("-------------------")
    for car in self.data["response"]["cars"]:
        make = car.get("make")
        if make == "Ford":
            print("{0} {1} {2}".format(car.get("year"), make, car.get("model")))
    print("-------------------")


def year_parser(self):
    print("Parser: Year parser")
    print("Condition: Picking all cars newer than 2001")
    print("-------------------")
    for car in self.data["response"]["cars"]:
        year = car.get("year")
        if year > 2001:
            print("{0} {1} {2}".format(year, car.get("make"), car.get("model")))
    print("-------------------")

if __name__ == '__main__':

    response = {"response": {
        "cars": [
            {"make": "Ford", "model": "Mustang", "color": "Black", "year": 2017},
            {"make": "Porsche", "model": "Porsche 911 GT3 RS", "color": "Red", "year": 2007},
            {"make": "Toyota", "model": "Supra Turbo", "color": "Blue", "year": 1993},
            {"make": "Plymouth", "model": "Superbird", "color": "Red", "year": 1970},
            {"make": "Ford", "model": "Bronco", "color": "Yellow", "year": 1966},
            {"make": "Ferrari", "model": "Enzo", "color": "Red", "year": 2003},
            {"make": "Dodge", "model": "Viper", "color": "Black", "year": 2006},
            {"make": "Dodge", "model": "Charger", "color": "White", "year": 1968},
            {"make": "Dodge", "model": "Challenger", "color": "Purple", "year": 1971},
            {"make": "Chevrolet", "model": "Corvette", "color": "Silver", "year": 2004}
        ]
    }}

    parser1 = ResponseParser(make_parser)
    parser1.data = response

    parser2 = ResponseParser(year_parser)
    parser2.data = response

    parser1.execute()
    parser2.execute()
