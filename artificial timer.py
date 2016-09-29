'artificial timer'

y = 0
while y < 3:
    x = 0
    y = y + 1
    while x <(10**4) * 630:
        x = x + 1
    if y == 1:
        print('ready')
    if y == 2:
        print('set')
    if y == 3:
        print('go')


for z in range(0 , 60 , 1):                 # z is hours
    for y in range(0 , 60 , 1):             # y is minutes
        for x in range(0 , 60 , 1):         # x is seconds
            w = 0
            while w <(10**4) * 625:
                w = w + 1
            print(z,'h'  ,  y,'m'  ,  x,'s')
    if (y + 1) % 3 == 0:
        x = x + 2
    
