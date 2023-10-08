def wordsep():
    f = open("School/XII_A.txt", "r")
    while True:
        line = f.readline()
        if line == '':
            break
        else:
            words = line.split()
            for i in words:
                print(i + '#', end='')
            print()
    f.close()
wordsep()