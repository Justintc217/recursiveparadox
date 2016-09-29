
for x in range(10**8 , 10**9 , 2):
    g = 1
    if x % (10**7) == 0:
        print(x)
    for t in range(2 , 20 , 1):
        if x % t != 0:
            g = 0
            break
    if g == 1:
        print('success!!!' , x)
print('done')
