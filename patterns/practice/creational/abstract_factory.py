from abc import abstractmethod


class Company(object):

    def __init__(self, factory=None):

        self.factory = factory

    def build(self, count):
        automobile = self.factory.make()
        print("Start building {0} {1} {2} at {3} each".format(
            count,
            automobile.get_color(),
            automobile.get_model(),
            automobile.get_price()))

class Automobile:

    @abstractmethod
    def get_price(self): pass

    @abstractmethod
    def get_color(self): pass

    @abstractmethod
    def get_model(self): pass

class Factory:

    @abstractmethod
    def make(self): pass


class PorscheFactory(Factory):

    def make(self):
        return Porsche()


class FerrariFactory(Factory):

    def make(self):
        return Ferrari()

class FerrariFactory2(Factory):

    def make(self):
        return Ferrari()



class Porsche(Automobile):

    def get_model(self):
        return "Porsche 911 Turbo S"

    def get_color(self):
        return "black"

    def get_price(self):
        return "$160,250"


class Ferrari(Automobile):

    def get_model(self):
        return "Ferrari 488GTB"

    def get_color(self):
        return "red"

    def get_price(self):
        return "$249,150"


if __name__ == "__main__":
    company = Company(PorscheFactory())
    company.build(1000)

    company = Company(FerrariFactory())
    company.build(1500)

