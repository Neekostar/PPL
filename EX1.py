from math import *

i = 0
end = 1.2
while (i <= end):
    result = sin(i) + sin(i ** 2) ** 2 + sin(i ** 3) ** 3
    print(f'f({round(i, 1)})={result}')
    i += 0.1
