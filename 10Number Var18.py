import datetime as DT


def main(book):
    minValue = -1
    isNo = False
    dates = []
    index = []
    values = []
    letters = []
    newBook = []
    for i in range(0, len(book)):
        if book[i][1] is None:
            index.append(i)
        else:
            book[i].pop(2)
            book[i].pop(0)
    book.pop(index[1])
    book.pop(index[0])
    for i in range(0, len(book)):
        book[i].pop(1)
        if(book[i][1].find('нет') != -1):
            isNo = True
        indexOfLine = book[i][1].find('|')
        values.append(book[i][1][indexOfLine + 1])
        values[i] += book[i][1][indexOfLine + 2]
        values[i] += book[i][1][indexOfLine + 3]
        values[i] += book[i][1][indexOfLine + 4]
        book[i][1] = values[i]
        book[i][1] += '0'
        book[i][1] += '0'
        values[i] = book[i][1]
        date = DT.datetime.strptime(book[i][2], '%d-%m-%Y').date()
        book[i][2] = date.strftime('%Y/%m/%d')
        indexOfSlash = book[i][2].find('/')
        book[i][2] = book[i][2][indexOfSlash - 2:len(book[i][2])]
        dates.append(book[i][2])
        spaceIndex = book[i][0].find(' ')
        word1 = book[i][0][:int(spaceIndex + 1)]
        word2 = book[i][0][int(spaceIndex):]
        book[i][0] = word2 + ' ' + word1
        book[i][0] = book[i][0][:-1]
        book[i][0] = book[i][0][1:]
        letters.append(book[i][0][0])
        if isNo is True:
            book[i].insert(2, 'N')
        else:
            book[i].insert(2, 'Y')
        isNo = False
    letters = sorted(letters)
    for i in range(0, len(letters)):
        for j in range(0, len(book)):
            if letters[i] == book[j][0][0]:
                newBook.append(book[j])
    return newBook
