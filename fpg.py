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




