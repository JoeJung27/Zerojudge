import math
def quadratic(a, b, c):
    if (b * b - 4 * a * c) < 0:
        return 'No real root'
    Delte = math.sqrt(b * b - 4 * a * c)
    if Delte > 0:
        x = (- b + Delte) / (2 * a)
        y = (- b - Delte) / (2 * a)
        return('Two different roots x1={} , x2={}\n'.format((int(x)),(int(y))))
    else:
        x = (- b) / (2 * a)
        return('Two same roots x={}\n'.format(int(x)))
n = input()
s = n.split()
d = quadratic(int(s[0]),int(s[1]),int(s[2]))
print(d)