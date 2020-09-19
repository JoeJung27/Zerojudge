def gcd(a,b):
    while b:
        r = a%b
        a = b
        b = r
    return a

while 1:
    try:
        numbers = input()
        tmpn1 = int(numbers.split()[0])
        tmpn2 = int(numbers.split()[1])
        print(gcd(tmpn1,tmpn2))
    except:
        break