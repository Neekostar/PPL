from threading import Thread

import random as rnd
from time import sleep

totalGold = 1000
countOfGold = 0


class Unit(Thread):
    def __init__(self, number):
        Thread.__init__(self)
        self.number = number

    def exractGold(self):
        global countOfGold
        global totalGold
        while (countOfGold <= 950):
            print(f"Юнит №{self.number + 1} пошел за золотом в пещеру")
            delay = rnd.randint(0, 5)
            print(f"Юнит №{self.number + 1} задержался на {delay} секунд")
            sleep(delay)
            gold = 10
            countOfGold += gold
            totalGold -= gold
            print(f"Юнит №{self.number + 1} принес {gold} золота из пещеры")
            print(f"Собранное золото: {countOfGold}")

    def run(self):
        self.exractGold()


n = int(input("Введите, сколько юнитов пойдут за золотом: "))
listOfUnits = [Unit(i) for i in range(n)]
for i in listOfUnits:
    i.start()
