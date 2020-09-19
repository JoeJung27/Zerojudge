num = int(input())
lst = []
for i in range(num):
    ns = input().split()
    if int(ns[0]) == 1:
        print(int(ns[1])+int(ns[2]))
    elif int(ns[0]) == 2:
        print(int(ns[1])-int(ns[2]))
    elif int(ns[0]) == 3:
        print(int(ns[1])*int(ns[2]))
    else:
        print(int(int(ns[1])/int(ns[2]))) 

