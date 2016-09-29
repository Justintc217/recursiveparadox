'''lion = [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1]

O O O O O

Y X O O
Y X O O
Y X O O
Y X O O

1 , 4 , 4 + 3 + 2 + 1 , (4 + 3 + 2 + 1) + (3 + 2 + 1) + (2 + 1) + 1 ,

1 , 2 , 3        2 by 2
1 , 3 , 6 , 10
1 , 4 , 10 , 20 , 35
1 , 5 , 15 , 35 , 70 ,      5 by 5'''

summation = 0
dog = []
for x in range (1 , 22 , 1):
    dog.append(x)                       # puts 1 thru 20 into dog

for overarch in range(0 , 18 , 1):      # just counts up to 20 reps so the program stops at 20
    cat = dog                           # makes cat the previous dog
    dog = []                            # resets dog so new summations within cat can be put back in


    for y in range (1 , 22 , 1):        # y establishes the index within cat for how many indicies are we summing
        new = 0
        for x in range (0 , y , 1):     # sums up value of index of first to y in previous dog (cat) 
            new = cat[x] + new
        dog.append(new)                 # makes new set of values and puts them into dog
    print(dog)
print('next')
for t in range(0 , 20 , 1):
    print(dog[t])
    summation = summation + dog[t]
print(summation)
    







'-------------------------------------------'
'''x = 0
while d != 2 and r != 0:
    y = 0
    for r in range (0 , 3 , 1):
        d = 0
        r = 
        if r == 2 - x:
            while d - y != 2:
                d = d + 1
                
        if d == 2 and r != 2:
            r = r + 1
            if r == 2:
                print('check')
                break
        if d == 2 and r == 2:
            print('check')
            x = x + 1
            break'''
