def password(code):
    lst = list(code)
    num = []
    for i in range(6):
        num.append(abs( ord(lst[i+1]) - ord(lst[i]) ))
    ans = ''.join(str(e) for e in num)
    return ans
    
while(1):
    try:
        CODE = input()
        print(password(CODE))
    except:
        break