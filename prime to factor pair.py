# need to add amount vals at a different rate as iterations



cat = [2 , 2 , 3 , 3 , 5 , 7]

k = len(cat)
'''dog = len(cat) * [cat]
print(dog)

for y in range(0 , len(cat) , 1):
    for x in range(0 , something , 1):
        comb = cat[y]'''
'''dog = []
for w in range(0 , k , 1):
    for x in range(0 , k , 1):
        for y in range(x + 1, k , 1):
            val = cat[x]
            for n in range(0 , w , 1):
                if y + n > k - 1:
                    break
                val = val + cat[y + n]
            print(val)
            dog.append(val)
pup = set(dog)
print(len(pup), pup)'''


dog = []
y = 0
for w in range(0 , k , 1):               
    for x in range(0 , k , 1):
        val = 1
        for n in range(0 , w , 1):
            if x + n > k - 1:
                break
            val = val * cat[x + n]
            for r in range (x + n + 1, k , 1):
                new = val * cat[r]
                dog.append(new)
                print(new)
pup = set(dog)
print(len(pup), pup)
print(2 * 2 * 3 * 3 * 5 * 7)






