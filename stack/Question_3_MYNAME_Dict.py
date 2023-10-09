def MYSTACK(d):
    MYNAME = []
    for name in d.values():
        if 's' in name.lower():
            MYNAME.append(name)
    return MYNAME

def POPSTACK(MYNAME):
    while len(MYNAME) > 0:
        print(MYNAME.pop())
    print("Stack Empty")

d = {1: 'Sunil', 2: 'Naman', 3: 'Anish'}

MYNAME = MYSTACK(d)

print("MYNAME:", MYNAME)

print("Output of POPSTACK() function:")
POPSTACK(MYNAME)
