book = [[None,None,None,None],
['zomikak42@yandex.ru', None,None,'22.05.2004!+7 579 673-5556'],
['georgij98@gmail.com', None,None,'10.09.2002!+7 936 066-8730'],
['aleksej31@rambler.ru', None,None,'22.07.2001!+7 158 419-1348'],
['georgij98@gmail.com', None,None,'10.09.2002!+7 936 066-8730']
    ]


def main(book):
    index = 0
    for i in range(0, len(book)):
        if book[i][0] is None:
            index = i
        else:
            book[i].pop(2)
            book[i].pop(1)
            
    book.pop(index)
    return book
print(main(book))