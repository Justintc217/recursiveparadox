# box grid number of routes / legs of pascal triangle summer

# formula F(leg0 = leg of 1s) (n + r)!/[(r + 1)!]^2

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
    




