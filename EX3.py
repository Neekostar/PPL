def first_check(number):
    return number % 154 == 0

def second_check(number):
    a = number % 10
    b = (number // 10) % 10
    c = (number // 100) % 10
    d = number // 1000
    return ((a == b and c == d) or (a == c and b == d) or (a == d and b == c)) and (a + b + c + d == 30)

def third_check(number):
    a = number % 10
    b = (number // 10) % 10
    c = (number // 100) % 10
    d = number // 1000
    return (a + b + c + d == 30)


for i in range(10000):
    if (first_check(i) and second_check(i) and third_check(i)):
        print(f'Номер нарушителя: {i}\n')
