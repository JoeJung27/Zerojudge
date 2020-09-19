import sys
for num in sys.stdin:
    num = int(num)
    out = ''
    t = 2
    while num != 1:
        if num % t == 0:
            pow = 0
            while True:
                pow = pow + 1
                num = num / t
                if num % t != 0 : break
            if pow > 1:
                out = out + str(t) + '^' + str(pow) + ' * '
            elif pow == 1:
                out = str(out) + str(t) + ' * '
        t = t + 1 
    out = out.strip(' ').strip('*')   
    print(out)