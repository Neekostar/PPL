from abc import ABC, abstractmethod
from random import randint


class Base(ABC):
    @abstractmethod
    def rowFibonacci(self):
        pass

    @abstractmethod
    def generateList(self):
        pass

    @abstractmethod
    def calculateFibonacciIncluding(self):
        pass


class MyClass(Base):
    list = []
    fibonacci = []
    my_range = 0

    def generateList(self):
        self.my_range = int(input("Введите диапазон:\n"))
        self.list = [randint(0, 100) for i in range(self.my_range)]
        print(f'Сгенерированный список: {self.list}')

    def rowFibonacci(self):
        fib1 = 1
        fib2 = 1
        for i in range(2, self.my_range):
            fib1, fib2 = fib2, fib1 + fib2
            self.fibonacci.append(fib2)
        print(f"Числа Фибоначчи: {self.fibonacci}\n")

    def calculateFibonacciIncluding(self):
        for i in self.list:
            if i in self.fibonacci:
                print(f"Число {i} из сгенерированного списка является числом Фибоначчи")
            else:
                print(f"Число {i} из сгенерированного списка не является числом Фибоначчи")

if __name__=="__main":
    a = MyClass()
    a.generateList()
    a.rowFibonacci()
    a.calculateFibonacciIncluding()
