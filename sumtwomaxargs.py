def my_func(**kwargs):
    linearg = list()
    for key in kwargs:
        linearg.append(kwargs.get(key))
    linearg.sort()
    return linearg[-1] + linearg[-2]


a, b, c = input('Enter three numbers : ').split()
try:
    print(my_func(arg1=int(a), arg2=int(b), arg3=int(c)))
except ValueError:
    print(" Error assigning a value to a variable")
