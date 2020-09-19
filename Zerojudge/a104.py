def easysort(M):
    lst = M.split()
    lst = list(map(int, lst))
    lst.sort()
    lst = list(map(str, lst))
    ans = ' '.join(str(e) for e in lst)
    return ans

while(1):
    try:
        n = int(input())
        m = input()
        print(easysort(m))
    except:
        break
