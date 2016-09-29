def fpg(z):     
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

'----------------------------------------------------------'

def basech(base , x):
    alphabet = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'L' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
    val = str()
    new = val
    while x != 0:
        dig = x % base
        if dig > 9:
            dig = alphabet[dig - 10]
        str(dig)
        x = x//base
        val = val + str(dig)
        if x == 0:
            p = len(val) + 1
            for t in range (1 , p , 1):
                new = new + val[-t]
    return (new)

'-----------------------------------------------------------'

#primes in prime bases

for z in range(2 , 20 , 1):
    x = fpg(z)
    for b in range(2 , 17 , 1):
        if b < 2:
            b = 2
            print('warning for next number')
        print(z , '  prime =', x , '  base =', b , '  result =', basech(b , x))


