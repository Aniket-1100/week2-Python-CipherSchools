#functions practice
def last_char(name):
    return name[-1]
print(last_char("aniket"))

def odd_even(num):
    if num%2==0:
        return "even"
    return "odd"
print(odd_even(10))

def is_even(n):
    if n%2==0:
        return True
    return False
print(is_even(10))

def is_even(n):
    return n%2==0

print(is_even(10))

def song():
    return "happy birthday song"
print(song())