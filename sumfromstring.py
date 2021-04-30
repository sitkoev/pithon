
sm = 0
nextinput = True
while nextinput:
    st = list(input('Введите строку чисел : ').split())
    for n in st:
        try:
            sm += int(n)
        except ValueError:
            nextinput = False
            break
    print('Сумма составила : ', sm)
