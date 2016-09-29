#reverse your strings!



def rev(val):
    new = ""
    for t in range (1 , 7 , 1):
        new = new + val[-t]
    return new

print(rev('justin'))

