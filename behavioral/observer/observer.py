from abc import ABC, abstractmethod


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject) -> None:
        """
        Receive update from subject.
        """
        pass


class ConcreteObserverA(Observer):
    """
    Adding << Single Pattern >>
    If instance already exists, it will return the existing one
    Create new one otherwise and return the new one
    """
    def __new__(cls) -> any:
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConcreteObserverA, cls).__new__(cls)
        return cls.instance

    def update(self, subject) -> None:
        if subject._state < 4:
            print("ConcreteObserver <<A>> responded ...\n")


class ConcreteObserverB(Observer):
    """
    Adding << Single Pattern >>
    If instance already exists, it will return the existing one
    Create new one otherwise and return the new one
    """
    def __new__(cls) -> any:
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConcreteObserverB, cls).__new__(cls)
        return cls.instance
    
    def update(self, subject) -> None:
        if subject._state >= 4:
            print("ConcreteObserver <<B>> responded ...\n")
 