 
cat = [3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29]
x = 5
v = 10
while v < 3000:
    x = x + 2
    prime = True
    for p in cat:
            if x % p == 0:
                break
            else cat.append(x)
    for z in range(3 , x + 2 , 2):
        if z == x:
            v = v + 1
            print(v , x)
        if prime == False:
            break
        if x % z == 0:
            prime = False

"if number passes % p test then put that number in cat"
            
