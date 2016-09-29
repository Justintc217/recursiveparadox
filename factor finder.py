
'factor finder'

x = 76576500      #choose
y = 0
z = 0
g = 0
cat = []
while y < x:
    y = y + 1
    w = 0
    if x % y == 0:
        print('factor' , y)
        cat.append(y)
        w = y
        z = z + y
        g = g + 1
    if y == x:
        print(g)
        print('cat info' , len(cat) , cat)
        print('sumvalue of factors' , z)
        print('perfect tester' , z - x)
