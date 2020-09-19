def ming(n):
    x = n.split()
    start = int(x[0])
    end = int(x[1])
    summ = start
    ind = 1
    while summ <= end:
        summ = summ + (start + ind)
        ind += 1
    return ind

while 1:
    try:
        num = input()
        print(ming(num))
    except:
        break