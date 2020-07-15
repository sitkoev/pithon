def int_func(latword):
    minindex = ord('a')
    maxindex = ord('z')
    for simbol in latword:
        if ord(simbol) < minindex or ord(simbol) > maxindex:
            return True
    return latword.capitalize()


finderror = False
while finderror == False:
    ''' Цикл прервется в случае ошибки при вводе '''
    newStr = ""
    inpstr = list(input().split())
    for word in inpstr:
        res = int_func(word)
        if res == True:
            finderror = True
            newStr = "error in word: " + word
            break
        else:
            newStr += res + ' '
    print(newStr)
