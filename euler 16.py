num = str(2**1000)
print(num)
sam = 0

for x in range(0 , len(num) , 1):
    sam = int(num[x]) + sam
print(sam)
