drink = ['milk', 'tea', 'juice', 'beer', 'water']

def delay(t):
    w = 0               # pause begin
    while w <(10**4) * 100*t:
        w = w + 1       # pause end
    return(t)

"""def Qsave(*a):
    cat = []
    n = 0
    while n < len(a):
        cat.append(a[n])
        n = n + 1   
    while x == 'yes': 
        Q = input ('')
        if Q in cat:
            delay(5)
            print('one moment please while i prepare your',Q)
            delay(20)
            print('okay, finished')
            delay(5)
            print('what would you like next?')
        else:
            delay(5)
            print('sorry could you repeat that')
    return cat"""

def Q1(*a):
    cat = []
    n = 0
    while n < len(a):
        cat.append(a[n])
        n = n + 1   
    while x == 'yes': 
        Q = input ('')
        save = Q
        if Q in cat:
            t = 0
            while t < cat[0]:
                t = t + 1
                delay(10)
                special = ''
                if cat[t] == 'Q':
                    special = Q 
                print(a[-t], special)
                Q = save
        if Q == 'nex':
            break
        if Q not in cat and Q != 'nex':
            delay(5)
            print('sorry could you repeat that')
    return cat
    



ans = ['yes' , 'no']
num1 = 0
while True:
    num1 = num1 + 1
    if num1 == 1:
        x = input ('would you like a glass?: ')
    else:
        x = input ('')
    if x not in ans:
        print('I\'m sorry, could you please answer with a \'yes\' or \'no\'')
    if x == 'yes':
        y = 0
        
        delay(2)
        print('would you like')
        while y < 5:
            delay(2)
            print(drink[y])
            if y == 3:
                delay(4)
                print('or')
            y = y + 1


    Q1(4 , 'Q' , '' , '' , 'Q' , *drink , 'carol wants' , 'what would you like next' , 'okay done' , 'one moment please while I prepare your')
    delay(10)
    print('what is your favorite color?')
    Q1(2 , 'Q' , 'black' , 'yellow' , 'red' , 'white' , 'blue' , 'orange' , 'purple' , 'silver' , 'green' , 'pink' , 'I like it' , 'yes...')
    if x == 'no':
        delay(3)
        print('Fine then')
        delay(6)
        print('let me know if you change your mind')
    


    



