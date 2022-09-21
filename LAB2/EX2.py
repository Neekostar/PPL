f1 = open('f1.txt', 'r+')
f2 = open('f2.txt', 'r+')
g = open('g.txt', 'r+')

print(f'Содержимое файла f1: {f1.read()}')
print(f'Содержимое файла f2: {f2.read()}')

f1.seek(0)
g.write(f1.read())
g.seek(0)
f1.close()

f1 = open('f1.txt', 'w')
f2.seek(0)
f1.write(f2.read())
f1.close()

f2.close()
f2 = open('f2.txt', 'w')
f2.write(g.read())
f2.close()

with open('f1.txt') as f1:
    result1 = f1.readline()

with open('f2.txt') as f2:
    result2 = f2.readline()

print(f'Содержимое файла f1 после обмена значениями: {result1}')
print(f'Содержимое файла f2 после обмена значениями: {result2}')
