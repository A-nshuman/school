def countVCUL():
    f = open("School/XII_A.txt", "r")
    V=C=U=L=0
    data = f.read()
    for i in data:
        if i.isalpha():
            if i.isupper():
                U += 1
            if i.islower():
                L += 1
            if i in 'aeiouAEIOU':
                V += 1
            else:
                C += 1
    print("Vowels : ",V)
    print("Consonents : ",C)
    print("Upper Case : ",U)
    print("Lower Case : ",L)
countVCUL()