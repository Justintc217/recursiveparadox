

def f(*a):
    x = 0
    y = 0
    cat = []
    while x < len(a):
        cat.append(a[x])
        x = x + 1
    while y < len(a):
        y = y + 1
        Q = input('answer:')
        if Q in cat:
            print(a[-1])
    return cat

food = ['apple' , 'banana' , 'carrot', 'dragon', 'eel']



new = f(*food, 'welcome to my house')

if 'apple' in new:
    print('success')
