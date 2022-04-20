def order(sentence):
    lis = sentence.split(' ')
    lis1 = []

    for i in lis:
        for j in i:
            if j.isdigit():
                lis1.append(j)

    x = zip(lis, lis1)

    x2 = sorted(x, key=lambda tup: tup[1])

    return ' '.join([x[0] for x in x2])
