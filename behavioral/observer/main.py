from abc import ABC, abstractmethod
from random import randrange
from typing import List

from subject import Subject, ConcreteSubject
from observer import Observer, ConcreteObserverA, ConcreteObserverB


if __name__ == '__main__':
    subject = ConcreteSubject()
    
    observerA = ConcreteObserverA()
    subject.registerObserver(observerA)

    observerB = ConcreteObserverB()
    subject.registerObserver(observerB)

    subject.setState()
    subject.setState()

    subject.removeObserver(observerA)
    subject.setState()