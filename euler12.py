
# need permutation function for primes


for n in range(20000 , 100000 , 1):
    g = 1
    x = 1
    v = n*(n+1)/2
    if v % 360 != 0:
        g = 0
    t = int(v)
    cat = [1]
    if n % 10000 == 0:
        print('check')
    if g == 1:
        while x < t + 1:
            x = x + 1
            if t % x == 0:
                cat.append(x)
                '''print('first' , x , t)
                print(cat)'''
                t = int(t/x)
                x = x - 1
                if t == 1:
                    break
    if len(cat) > 15:
        dog = [0]
        y = 0
        while y < v:
            y = y + 1
            if v % y == 0:
                dog.append(y)
        if len(dog) > 300:
            print(n , len(dog))
            


'''3 : 2**3 -2
4: 2**4 - 2

repeat: 2**(x-2)
ABC
A
B
C
AB
AC
BC




ABCD
A
B
C
D
AB
AC
AD
BC
BD
CD
ABC
ABD
ACD
BCD

AACD
A
C
D
AA
AC
AD
CD
AAC
AAD
ACD

AACC
A
C
AA
CC
AAC
ACC

AAAC
A
C
AA
AC
AAA
AAC


ABCDE
A
B
C
D
E
AB
AC
AD
AE
BC
BD
BE
CD
CE
DE
ABC
ABD
ABE
ACD
ACE
ADE
BCD
BCE
BDE
CDE
ABCD
ABCE
ABDE
ACDE
BCDE

AACDE
A
C
D
E
AA
AC
AD
AE




            
'''
