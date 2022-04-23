import datetime as DT


def main(book):
    indexForNotEmpty = -1
    index = []
    index1 = -1
    secondUpper = 1
    upperLeters = []
    for i in range(0, len(book)):
        if book[i][0] is None:
            index.append(i)
    book.pop(index[1])
    book.pop(index[0])
    for i in range(0, len(book)):
        for j in range(0, len(book)):
            if book[i] == book[j] and i != j:
                index1 = j
        book[i].pop(3)
        date = DT.datetime.strptime(book[i][3], '%Y.%m.%d').date()
        book[i][3] = date.strftime('%d.%m.%Y')
        book[i][2] = book[i][2].replace('%', '', 1)
        number = round(int(book[i][2]) / 100, 1)
        book[i][2] = str(number)
        book[i][1] = book[i][1].replace(' ', '', 1)
        book[i][0] = book[i][0].replace('@', '[at]')
        book[i][1] = book[i][1].replace('.', '')
        spaceIndex = book[i][1].find(' ')
        word1 = book[i][1][:int(spaceIndex + 1)]
        word2 = book[i][1][int(spaceIndex):]
        book[i][1] = word2 + ' ' + word1
        book[i][1] = book[i][1][1:-1]
        book[i][1] = book[i][1][:-1]
    book.pop(index1)
    return book
