def DISPLAYWORDS():
    c = 0
    file = open('School/XII_A.txt', 'r')
    line = file.read()
    word = line.split()
    for w in word:
        if len(w) < 4:
               print(w)
               c += 1
    file.close()
    print(c)

DISPLAYWORDS()