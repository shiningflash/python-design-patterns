from abc import abstractmethod

from component import Bevarage


class CondimentDecorator(Bevarage):
    """
    Decorator Abstract Class
    """

    @abstractmethod
    def getDescription(self) -> any:
        pass


class Mocha(CondimentDecorator):
    """
    Decorator Class: Mocha
    """

    bevarage: Bevarage = None;

    def __init__(self, bevarage: Bevarage):
        self.bevarage = bevarage
    
    def getDescription(self) -> str:
        return self.bevarage.getDescription() + ", Mocha"
    
    def cost(self) -> float:
        return self.bevarage.cost() + .10


class Milk(CondimentDecorator):
    """
    Decorator Class: Milk
    """

    bevarage: Bevarage = None

    def __init__(self, bevarage: Bevarage):
        self.bevarage = bevarage

    def getDescription(self) -> str:
        return self.bevarage.getDescription() + ", Milk"

    def cost(self) -> float:
        return self.bevarage.cost() + .05