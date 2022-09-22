def read_file(file_name):
    file = open(file_name)
    file.seek(0)
    lst = file.readlines()
    lst = [i.strip('\n') for i in lst]
    file.close()
    return lst


def write_file(file_name, data):
    file = open(file_name, 'w+')
    for i in data:
        file.write(i + '\n')
    file.close()


first_file_data = read_file('persons1.txt')
print(f'Данные из первого файла:\n{first_file_data}\n')

first_file_data = sorted(first_file_data, reverse=True)

write_file('persons2.txt', first_file_data)
second_file_data = read_file('persons2.txt')
print(f'Данные из второго файла:\n{second_file_data}\n')
