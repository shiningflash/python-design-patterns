from abc import ABC, abstractmethod
from random import randrange
from typing import List, Set

from observer import Observer


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def registerObserver(self, observer: Observer) -> None:
        """
        Register an observer to the subject.
        """
        pass

    @abstractmethod
    def removeObserver(self, observer: Observer) -> None:
        """
        Remove an observer to the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = 0
    _observers: List[Observer] = []

    def registerObserver(self, observer: Observer) -> None:
        print('Subject: Registered an observer ...')
        # Check duplicates
        if observer not in self._observers:
            self._observers.append(observer)
    
    def removeObserver(self, observer: Observer) -> None:
        print('Subject: Removed an observer ...')
        self._observers.remove(observer)
    
    def notify(self) -> None:
        print('Subject: Notifying observers ...')
        for observer in self._observers:
            observer.update(self)

    def setState(self) -> None:
        print('\nSubject: I am doing something important ...')

        self._state = randrange(0, 10)
        print(f'Subject: State has just changed to {self._state}')
        self.notify()
