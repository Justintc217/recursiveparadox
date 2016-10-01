# fibonacci generator


prev = 0 # More meaningful identifiers
curr = 1
answer = 0
while prev < 4 * 1000 * 1000: # 4000000 can be difficult to read
    temp = prev
    prev += curr # Means add curr to prev
    curr = temp
    if prev % 2 == 0:
        answer += prev
print(answer)
