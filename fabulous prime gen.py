
"fabulous prime generator"


def fpg(z):     # gives value of the z-th prime 
    cat = [2]
    x = 1
    v = 1
    y = 0
    t = 1
    if z == 1:
        x = 2
    while v == 1:
        g = 1
        x = x + 2
        for p in cat:
            if x % p == 0:
                g = 0
                break
        if g == 1:
            cat.append(x)
            print(x)
            y = y + x
            if x > 20000 * t:
                t = t + 1
                print('x=' , x , 'sum=' , y)
        return x
'---------------------------------------------------'


142915828923
142915828923
