def fiophone(**recs):
    lst = list()
    for key in recs:
        lst.append(recs.get(key))
    return lst


users = (['Иванов', 'Иван', '1970', 'Москва', 'ivanov@mail.ru', '8(888) 888 88 88'],
         ['Петров', 'Петр', '1980', 'Berlin', 'petrov@mail.ru', '7(777) 777 77 77'],
         ['Григорадзе', 'Чингачгук', '1990', 'Kazan', 'grigoradze@yandex.ru', '8(925)134 56 78'],
         ['Кучкина', 'Изольда', '1985', 'Samara', 'kuchkinaI@gmail.com', '8(917)555 14 73'],
         ['Кучкина', 'Варвара', '1985', 'Samara', 'kuchkinaV@gmail.com', '8(917)555 14 74'])

for record in users:
    print(*fiophone(name=record[0], family=record[1], yearofborn=record[2], city=record[3], email=record[4],
                    phone=record[5]), sep='; ')
