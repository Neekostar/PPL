import csv
from xml.etree import ElementTree as ET
import json
import os


def write_data_into_csv():
    cls()
    name = input("Введите имя:\n")
    surname = input("Введите фамилию:\n")
    date_of_born = input("Введите дату рождения:\n")
    city = input("Введите город проживания:\n")

    with open("/home/neekostar/PycharmProjects/PPL/PRACTICE/output.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", 'surname', "date of born", "city"],
                                quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerow({"name": name, "surname": surname, "date of born": date_of_born, "city": city})
    print("Данные успешно записаны!")


def rewrite_data_into_csv():
    cls()
    new_name = input("Введите новое имя:\n")
    new_surname = input("Введите новую фамилию:\n")
    new_date_of_born = input("Введите новую дату рождения:\n")
    new_city = input("Введите новый город проживания:\n")

    with open("/home/neekostar/PycharmProjects/PPL/PRACTICE/output.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", 'surname', "date of born", "city"],
                                quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerow({"name": new_name, "surname": new_surname, "date of born": new_date_of_born, "city": new_city})
    print("Данные успешно перезаписаны!")


def append_new_data_into_csv():
    cls()
    appending_name = input("Введите имя:\n")
    appending_surname = input("Введите фамилию:\n")
    appending_date_of_born = input("Введите дату рождения:\n")
    appending_city = input("Введите город проживания:\n")

    with open("/home/neekostar/PycharmProjects/PPL/PRACTICE/output.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", 'surname', "date of born", "city"],
                                quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow({"name": appending_name, "surname": appending_surname, "date of born": appending_date_of_born,
                         "city": appending_city})
    print("Данные успешно добавлены!")


def print_data_from_csv():
    cls()
    with open("/home/neekostar/PycharmProjects/PPL/PRACTICE/output.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            print(
                f'Name: {row["name"]}\nSurname: {row["surname"]}\nDate of born: {row["date of born"]}\nCity: {row["city"]}\n')


def convert_csv_to_xml():
    cls()
    xml_data_list = []
    with open("/home/neekostar/PycharmProjects/PPL/PRACTICE/output.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            xml_data_list.append(row.copy())

        root = ET.Element("root")
        for i, item in enumerate(xml_data_list, 1):
            person = ET.SubElement(root, "person" + str(i))
            ET.SubElement(person, "Name").text = item["name"]
            ET.SubElement(person, "Surname").text = item["surname"]
            ET.SubElement(person, "DateOfBorn").text = item["date of born"]
            ET.SubElement(person, "City").text = item["city"]

        tree = ET.ElementTree(root)
        tree.write("/home/neekostar/PycharmProjects/PPL/PRACTICE/output.xml")
    print("Данные успешно конвертированы!")


def convert_csv_to_json():
    cls()
    json_data_list = []
    with open("/home/neekostar/PycharmProjects/PPL/PRACTICE/output.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            json_data_list.append(row.copy())

    with open("/home/neekostar/PycharmProjects/PPL/PRACTICE/output.json", "w") as file:
        str = json.dumps(json_data_list, indent=4)
        file.write(str)
    print("Данные успешно конвертированы!")


def go_back():
    choise = input('Чтобы вернуться, назад нажмите "z"\n')
    if choise == 'z':
        cls()
        menu()
    else:
        print('Неверная команда!')
        go_back()


def cls():
    os.system("clear")


def menu():
    print("Выберите пункт меню:\n")
    print(
        "1. Считать данные в CSV-файл\n2. Добавить запись в CSV-файл\n3. Перезаписать CSV-файл\n4. Вывести содержимое CSV-файла\n5. Конвертировать CSV-файл в XML-файл\n6. Конвертировать CSV-файл в JSON-файл\n0. Выход\n")
    command = int(input("Введите номер пункта: "))
    if command == 1:
        write_data_into_csv()
        go_back()
    elif command == 2:
        append_new_data_into_csv()
        go_back()
    elif command == 3:
        rewrite_data_into_csv()
        go_back()
    elif command == 4:
        print_data_from_csv()
        go_back()
    elif command == 5:
        convert_csv_to_xml()
        go_back()
    elif command == 6:
        convert_csv_to_json()
        go_back()
    elif command == 0:
        print("Выход из программы!")
        exit(0)
    else:
        print("Ошибка! Неверная команда!")


if __name__ == "__main__":
    menu()
