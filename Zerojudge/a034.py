def sum(num):
    tmp = []
    tmp2 = []

    while num != 1:
        tmp.append(num%2)
        num = int(num/2)

    tmp.append(1)

    for i in range(len(tmp)):
        tmp2.append(tmp[-1])
        tmp.pop()

    s = [str(j) for j in tmp2] 
    res = int("".join(s))
    return res


while(1):
    try:
        n = int(input())
        print(sum(n))
    except:
        break