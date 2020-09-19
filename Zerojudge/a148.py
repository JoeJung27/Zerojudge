def can_pass(a):
    scores = [int(i)for i in (a.split())]
    scores.remove(scores[0])
    a = 0
    for j in range(len(scores)):
        a += scores[j]
    if a/len(scores) > 59:
        return ("no")
    else:
        return ("yes")
while 1:
    try:
        n = input()
        print(can_pass(n))
    except:
        break