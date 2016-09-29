# fibonacci generator


x = 0
y = 1
answer = 0
while x < 4000000:
    z = x
    x = x + y
    y = z
    if x % 2 == 0:
        answer = answer + x
print(answer)
    
    
