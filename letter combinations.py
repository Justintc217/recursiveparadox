# need to add amount vals at a different rate as iterations



cat = ['a' , 'b' , 'c' , 'd' , 'e']

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


dog = cat
y = 0
for w in range(0 , k , 1):
    reset = 0
    dave = ''
    for x in range(0 , k , 1):
        val = ''
        
        for n in range(0 , w , 1):
            if x + n > k - 1:
                break
            h = x + n
            val = val + cat[x + n]
            for r in range (h + 1, k , 1):
                new = val + cat[r]
                if new == dave:
                    reset = 1
                    break
                dog.append(new)
                print(new , dave)
                if x + n + r == 1:
                    dave = new
                    p = 1
            if reset == 1:
                break
        if reset == 1:
            break
    if reset == 1:
        break
                
                

pup = set(dog)
print(len(pup), pup)
'''v = 1
for g in range( 0 , k , 1):
    v = v * int(cat[g])
print(v)'''
