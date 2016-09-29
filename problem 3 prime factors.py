x = 1
v = 1
while v < 20:
    z = 1
    x = x + 2
    prime = True
    y = 2
    while z < x:
        z = z + 2
        print(z , y)
        if z == x:
            v = v + 1
            "print(v , x)"
        if prime == False:
            z = x
        if z % y != 0:
            y = z
            if x % y == 0:
                prime = False
            
        
            
      
    
    
    
