def splits(s):
    return list(s)
while 1:
    try:
        a = input()
    except:
        break
    b = splitshit(a)
    d = []
    for i in range(len(b)):
        c = chr(ord(b[0]) - 7)
        d.append(c)
        b.remove(b[0])
    print ("".join(d))