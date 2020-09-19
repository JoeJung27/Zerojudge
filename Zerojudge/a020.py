Alph = ['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','X','Y','W','Z','I','O']

while 1:
    try:
        user_ID = input()
        l = list(user_ID)
        a = []
        n = 8
        num = 0

        for i in range(26):
            if l[0] == Alph[i]:
                num = (((10 + i) % 10) * 9) + int((10 + i) / 10)
                break

        for j in range(1, 9):
            a.append((int(l[j])) * n)
            n -= 1

        semi = num + sum(a) + int(l[-1])

        if semi % 10 == 0:
            print("real")
        else:
            print("fake")
    except:
        break