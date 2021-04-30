def my_func(foot, degree):
    if degree == 0:
        return 1
    elif degree > 0:
        return foot ** degree
    elif degree < 0:
        foot = 1 / foot
        degree = abs(degree)
        for i in range(degree):
            foot *= foot
        return foot


x, y = float(input('Введите действительное положительное число  : ')), int(input('Ввведите целое число : '))
print(' Результат возведения в степень : ', (my_func(x, y)))
