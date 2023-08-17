from subject import ConcreteSubject
from observer import ConcreteObserverA, ConcreteObserverB


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