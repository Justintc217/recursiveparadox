# palidrome generator

def rev(val):
    new = ""
    for t in range (1 , len(val) + 1 , 1):
        new = new + val[-t]
    return new
print(12/3)

u = rev('evil')
print(u)
for x in range(100000 , 1000000):
    g = 0
    x = x + 1
    y = str(x)
    if y == rev(y):
        for num in range(100 , 999):
            if g == 1:
                break
            if x % num == 0:
                for p in range(100 , 999):
                    if num * p == x:
                        print(x)
                        g = 1
                        break
                
