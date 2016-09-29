# x is tester for finding primary factors
# n is identification number for triangluar numbers
# v is triangular numbers
# t is triangluar numbers made into an integer
# r is values in cat to be multiplied by successful dividing x values and then added back into cat
# cat is the category for factors of triangular numbers



for n in range(1 , 20000 , 1):
    x = 1
    v = n*(n+1)/2
    t = int(v)
    cat = [1]
    while x < t + 1:
        x = x + 1
        if t % x == 0:
            dumbcat = cat
            for r in range(0 , len(dumbcat) , 1):
                y = cat[r] * x
                '''print( r , cat[r] , '*' , x , '=' , y)'''
                cat.append(y)
                'print(cat)'
            t = int(t/x)
            x = x - 1
        if t == 1:
            break
    if len(cat) > 498:
        kitty = set(cat)
        if len(kitty) > 400:
            print('special' , n , v, len(kitty), 'kitty')
print('done')
