class PizzaInterface:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def create(self) -> str:
        print("Create a pizza ...")
    
    def delivery(self) -> str:
        print("Delivering the pizza ...")


class DominosPizza:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def make(self) -> str:
        print("Dominos: Making your pizza ...")
    
    def send(self) -> str:
        print("Dominos: Sending your pizza ...")


class DominosPizzaAdapter(PizzaInterface, DominosPizza):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def __init__(self, dominosPizza) -> None:
        self.dominosPizza = dominosPizza

    def create(self) -> None:
        self.dominosPizza.make()
    
    def delivery(self) -> None:
        self.dominosPizza.send()


if __name__ == "__main__":
    pizzaInterface = PizzaInterface()
    dominosPizza = DominosPizza()
    dominosPizzaAdapter = DominosPizzaAdapter(dominosPizza)

    dominosPizzaAdapter.create()
    dominosPizzaAdapter.delivery()
