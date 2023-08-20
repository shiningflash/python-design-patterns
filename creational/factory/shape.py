from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Shape Interface
    """

    @abstractmethod
    def draw(self) -> str:
        pass


class Square(Shape):
    """
    Concrete Class : Square
    """

    def draw(self) -> str:
        return "Inside Square :: draw() method"


class Circle(Shape):
    """
    Concrete Class ; Circle
    """

    def draw(self) -> str:
        return "Inside Circle :: draw() method"