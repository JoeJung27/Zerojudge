a = input()
b = a.split()
m = b[0]
d = b[1]
s = (int(m)*2+int(d))%3
if s == 0:
    print("普通")
if s == 1:
    print("吉")
if s == 2:
    print("大吉")