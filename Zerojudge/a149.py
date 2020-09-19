def multi(a):
    lst = [int(i) for i in str(a)]
    res = 1
    for i in lst:
        res = res*i
    return res

tmp = []
n = int(input())
for j in range (n):
    y = int(input())
    tmp.append(y)
for l in range (n):
    print(multi(tmp[l]))  

