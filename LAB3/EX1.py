class SunSystem:
    Diameters = {"Меркурий": 2439, "Венера": 6050, "Земля": 6371, "Марс": 3389, "Юпитер": 69911, "Сатурн": 58232,
                 "Уран": 25362, "Нептун": 24622}
    Satellites = {"Меркурий": None, "Венера": None, "Земля": "Луна", "Марс": ["Фобос", "Деймос"],
                  "Юпитер": ["Метида", "Адрастея", "Амальтея", "Теба", "Ио", "Европа", "Ганимед", "Каллисто"],
                  "Сатурн": ["Мимас", "Энцелад", "Тефия", "Диона", "Рея", "Титан", "Гиперион", "Калипсо"],
                  "Уран": ["Титания", "Оберон", "Ариэль", "Умбриэль", "Миранда", "Калибан", "Франциско"],
                  "Нептун": ["Тритон", "Нереида", "Наяда", "Таласса", "Деспина", "Галатея", "Ларисса", "Протей"]}

    def __init__(self, diameter, name):
        self.diameter = diameter
        self.name = name


class Planet(SunSystem):
    def __init__(self, name):
        self.name = name

    def getPlanet(self):
        print(f"Планета: {self.name}")
        for key in self.Diameters:
            if self.name == key:
                print(f"Диаметр планеты: {self.Diameters[key]}")
        for i in self.Satellites:
            if self.name == i:
                s = self.Satellites[i]
                print("Спутники планеты:", *s)


class Satellite(SunSystem):
    def __init__(self, name):
        self.name = name

    def PrintInfo(self):
        print(f"\nСпутник: {self.name}")
        for key, value in self.Satellites.items():
            if (isinstance(value, list) and self.name in value) or self.name == value:
                print(f"{self.name} является спутником планеты {key}")


if __name__ == "__main__":
    Earth = Planet("Сатурн")
    Earth.getPlanet()

    sputnik = Satellite("Миранда")
    sputnik.PrintInfo()
