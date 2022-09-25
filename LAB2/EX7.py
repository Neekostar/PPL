Paul_friends = set()
Marie_friends = set()

print('Введите знакомых Пола:')
while True:
    Paul_friends.add(input())
    if ('' in Paul_friends):  # считывание, пока не будет введен пустой элемент
        Paul_friends.remove('')
        break

print('Введите знакомых Мари:')
while True:
    Marie_friends.add(input())
    if ('' in Marie_friends):  # считывание, пока не будет введен пустой элемент
        Marie_friends.remove('')
        break

common_friends = Paul_friends.intersection(Marie_friends)
print(f'Общие знакомые:\n{common_friends}')

only_Paul_friends = Paul_friends.difference(common_friends)
print(f'Знакомые только Пола:\n{only_Paul_friends}')

only_Marie_friends = Paul_friends.difference(common_friends)
print(f'Знакомые только Пола:\n{only_Marie_friends}')

union_friends = Paul_friends.union(Marie_friends)
print(f'Знакомые хотя бы для одного из них:\n{union_friends}')
