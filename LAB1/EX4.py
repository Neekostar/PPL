str = input('Введите текст: \n')
str = str.split()
count = 0
for i in str:
    if (i.startswith('A')):
        count += 1
        print(i)

if (count != 0):
    print(f'Найдено {count} слов(-а)\n')
else:
    print('Таких слов не найдено в тексте\n')
