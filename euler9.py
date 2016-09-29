

for a in range (1 , 500 , 1):
    for b in range (1 , 500 , 1):
        if (a**2 + b**2)**(0.5) ==  int((a**2 + b**2)**(0.5)):
            c = (a**2 + b**2)**(0.5)
            if (a + b + c) == 1000:
                print('special!!!!!!!!!!' , a * b * c)
