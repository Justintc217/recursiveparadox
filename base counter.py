# basech function
# x is number of interest
# goes up to base 36!



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

print(basech(36 , 82000))
