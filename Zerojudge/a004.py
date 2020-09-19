while 1:
    try:
        n = int(input())
    except:
        break
    if n % 4 == 0 and n%100 != 0 or n%400 == 0:
        print("閏年")
    else:
        print("平年")