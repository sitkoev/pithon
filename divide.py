def div(*args):

    try:
        return int(args[0]) / int(args[1])
    except ZeroDivisionError:
        return "ZeroDivisionError"
    except ValueError:
        return "ValueError"


a, b = input('Enter two numbers in string - ').split()
print(div(a, b))
