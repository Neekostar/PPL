f1 = open('f1.txt', 'r+')
f2 = open('f2.txt', 'r+')
h = open('h.txt', 'r+')

print(f'Содержимое файла f1: {f1.read()}')
print(f'Содержимое файла f2: {f2.read()}')

f1.seek(0)
h.write(f1.read())
h.seek(0)
f1.close()

f1 = open('f1.txt', 'w+')
f2.seek(0)
f1.write(f2.read())

f2.close()
f2 = open('f2.txt', 'w+')
f2.write(h.read())

f1.seek(0)
f2.seek(0)
result1 = f1.readline()
result2 = f2.readline()
f1.close()
f2.close()
h.close()

print(f'Содержимое файла f1 после обмена значениями: {result1}')
print(f'Содержимое файла f2 после обмена значениями: {result2}')
