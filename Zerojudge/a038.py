n = list(input())
n.reverse()
try:
    while n[0] == '0':
        n.remove(n[0])
except:
    print(0)

print("".join(n))