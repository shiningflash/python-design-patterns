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
    def update(self, subject) -> None:
        if subject._state < 4:
            print("ConcreteObserver <<A>> responded ...\n")


class ConcreteObserverB(Observer):
    def update(self, subject) -> None:
        if subject._state >= 4:
            print("ConcreteObserver <<B>> responded ...\n")
