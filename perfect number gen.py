'hogwarts perfect'              # none found btwn 10k and 37k


for x in range(1 , 100000000 , 1):
    y = 0
    z = 0
    while y < x - 1:
        g = 0
        w = 0
        y = y + 1
        if x % y == 0:
            g = 1
        if g == 1:
            w = y
            z = z + w
        if y == x - 1 and z == x:
            print('perfect' , x)

    if x % 1000 == 0:
        print('x=' , x)


        




