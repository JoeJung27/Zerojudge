def Score(n):
    if n <= 10:
        return n*6
    elif n > 10 and n <= 20:
        return 60 + ((n-10)*2)
    elif n > 20 and n <= 40:
        return 80 + (n-20)
    else:
        return 100

while(1):
    try:
        N = int(input())
        print(Score(N))
    except:
        break