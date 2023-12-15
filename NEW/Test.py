from abc import ABC


class Viacol(ABC):

    def bip(self, text):
        print(text)


class Car(Viacol):
    def bip(self):
        print("rewrw")


car = Car()
car.bip()
