from abc import abstractmethod


class Bevarage:
    """
    Component Class
    """
    
    description: str = "Unknown Bevarage"

    def getDescription(self) -> str:
        return self.description
    
    @abstractmethod
    def cost(self) -> float:
        pass


class Espresso(Bevarage):
    """
    Concrete Components Class
    """

    def __init__(self) -> any:
        self.description = "Espresso Coffee"
    
    def cost(self) -> float:
        return .99