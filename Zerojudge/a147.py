def printall(n):
    for i in range(1,n):
        if i % 7 != 0:
            print(i , end=" ")
    print('\n')

while(1):
    N = int(input())
    if N == 0:
        break
    else:
        printall(N)