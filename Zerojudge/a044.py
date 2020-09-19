def space(number):
    a=2
    b=2
    for i in range(2,number):
        a+=b
        b+=i
    return a+b

while(1):
    try:
        n = int(input())
        if n == 1:
            print(2)
        elif n == 2:
            print(4)
        else:
            print(space(n))
    except:
        break