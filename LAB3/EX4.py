from random import randint
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def generate_satiety(self):
        pass


class Cat(Animal):
    satiety = 0

    def __init__(self, satiety):
        self.satiety = satiety

    def eat(self):
        if self.satiety >= 100:
            print("Кошка сыта. Покормите в следующий раз")
        else:
            self.satiety += 75
        if self.satiety > 100:
            self.satiety = 100
            print(f"Мяу!\nСытость: {self.satiety}")

    def info(self):
        print(f"Животное: кошка\nСытость: {self.satiety}")

    def generate_satiety(self):
        self.satiety = randint(0, 100)


class Dog(Animal):
    satiety = 0

    def __init__(self, satiety):
        self.satiety = satiety

    def eat(self):
        if self.satiety >= 100:
            print("Собака сыта. Покормите в следующий раз")
        else:
            self.satiety += 75
        if self.satiety > 100:
            self.satiety = 100
            print(f"Гав!\nСытость: {self.satiety}")

    def info(self):
        print(f"Животное: собака\nСытость: {self.satiety}")

    def generate_satiety(self):
        self.satiety = randint(0, 100)

if __name__=="__main__":
    list1 = []
    for i in range(3):
        s = randint(0, 100)
        animal = Cat(s)
        list1.append(animal)

    for i in range(2):
        s = randint(0, 100)
        animal = Dog(s)
        list1.append(animal)

    print("Животные до кормления")
    for i in list1:
        i.info()

    print("\nЖивотные после кормления")
    for i in list1:
        i.eat()
