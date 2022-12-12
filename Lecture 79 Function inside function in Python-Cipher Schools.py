def greater(a,b):
    if a>b:
        return a 
    return b
print(greater(10,20))

def greatest(a,b,c):
    if a>b and b>c:
        return a
    elif b>a and b>c:
        return b 
    else:
        return c
print(greatest(10,20,30))

def new_greatest(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c)
print(new_greatest(10,20,30))