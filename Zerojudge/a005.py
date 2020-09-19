n=int(input())

for i in range(n):

    a,b,c,d = map(int,input().split())

    if b-a ==c-b:

        print(a,b,c,d,int(d+(b-a)))

    else:

        print(a,b,c,d,int(d*(b/a)))