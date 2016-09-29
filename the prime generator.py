"The prime generator"

x = 1
v = 1   
while v < 10001:
    z = 1
    x = x + 2
    prime = True
    while z < x:
        z = z + 2
        if z == x:
            v = v + 1
            print(v , x) 
        if prime == False:
            z = x
        if x % z == 0:
                prime = False



2826
            
        
            
      
    
    
    
