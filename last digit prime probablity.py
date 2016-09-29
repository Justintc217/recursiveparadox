"fabulous prime generator"

def fpg(z):     # gives value of the prime
    cat = [2]
    x = 1
    v = 1
    while v < z:
        g = 1
        x = x + 2
        for p in cat:
            if x % p == 0:
                g = 0
                break
        if g == 1:
            cat.append(x)
            v = v + 1
    return x
'---------------------------------------------------'

t = 100
while t <= 5000:
    x = 0
    a = 0
    b = 0
    c = 0
    d = 0
    while x < t:
        x = x + 1
        y =(fpg(x))
        y = str(y)
        if y[-1] == str(1):
            a = a + 1
        if y[-1] == str(3):
            b = b + 1
        if y[-1] == str(7):
            c = c + 1
        if y[-1] == str(9):
            d = d + 1
    t = t + 100
    print(t , a , b , c , d)
