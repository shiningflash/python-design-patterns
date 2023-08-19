from component import Bevarage, Espresso
from decorator import Mocha, Milk


if __name__ == "__main__":
    bevarage: Bevarage = Espresso()
    bevarage = Mocha(bevarage)
    bevarage = Milk(bevarage)

    print(bevarage.getDescription() + "\t$" + str(round(bevarage.cost(), 2)))