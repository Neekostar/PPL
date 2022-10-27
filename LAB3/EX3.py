class Car:
    brand = ""
    number = ""
    speed = 0

    def enter(self):
        self.brand = input("Введите марку автомобиля\n")
        self.number = input("Введите номер автомобиля\n")
        self.speed = int(input("Введите скорость автомобиля\n"))

    def print(self):
        length = max(len(str(self.speed)), len(self.brand), len(self.number))
        print()
        print("-"*(23+length))
        print("|Марка автомобиля:",self.brand,(21+length-(20+len(self.brand)))*" ","|","\n|Номер автомобиля:",self.number,(21+length-(20+len(self.number)))*" ","|","\n|Скорость автомобиля:",self.speed,(21+length-(23+len(str(self.speed))))*" ","|")
        print("-" * (23 + length))

if __name__=="__main__":
    new_car = Car()
    new_car.enter()
    new_car.print()
