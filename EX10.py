from random import randint

N = int(input('Введите количество городов:\n'))
M = [[randint(0, 1) if i != j else 0 for i in range(N)] for j in range(N)]

for i in range(N):
    s = 1
    for j in range(N):
        if (i > j):
            M[i][j] = M[j][i]
        if (M[i][j] == 1):
            s = 0
    if (s > 0):
        print(f'Город {i + 1} является изолированным')

for i in range(N):
    print(M[i], end='\n')
