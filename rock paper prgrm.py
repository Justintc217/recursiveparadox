# rock paper scissors

opt = ['rock' , 'paper' , 'scissors']
check ='0123456789'

import delay
import fpg
import math

def lay(t):
    delay.delay(t)
    return t

def wait():
    delay.delay(19)
    return

print ('ready to play rock , paper , scissors?')
lay(3)
print ('say yes to begin')
while True:
    if input() == 'yes':
        print('let the games begin!')
        lay(3)
        print('and of course...')
        lay(3)
        print('may the odds be ever in your favor')
        break
    else:
        print('what\'s that? ... can you repeat yourself?')

lay(4)
print('please input any random positive whole number less than 1000 to begin')


while True:
    r = input()
    g = 1
    for test in range(0 , len(r)):
        if r[test] not in check:
            print('please try again')
            g = 0
    if g == 1:
        break
    
    
        
lay(8)
print('let\'s begin: type in "rock" , "paper" , or "scissors"')
r = int(r)
point = 0
winrate = 0
loserate = 0
for y in range (r):
    det = int((y + fpg.fpg(y) + 2 * math.sin(y)))
    'print(det)'
    result = det % 3
    result = (result + (y % 3)) % 3
    while True:
        player = input()
        if player in opt:
            break
        print('sorry... can you retype your answer?')
    comp = result
    '''if result == 0:
        a = a + 1
    if result == 1:
        b = b + 1
    if result == 2:
        c = c + 1'''
    result = opt[result]
    lay(6)
    print('')
    print('computer chose' , result)
    for choice in range (0 , 3):
        if opt[choice] == player:
            player = choice
            break
    print('')
    lay(4) 
    if comp > player:     
        w = 1
    if player > comp:
        w = 2
    if comp == player:
        w = 0
    if comp == player + 2:
        w = 2
    if player == comp + 2:
        w = 1





# funny victories



    if w == 1:
        point = point - 1
        loserate = loserate + 1
        if point < 0:
            point = 0
        if point > 2:
            
            if comp == 0:
                print('your scissors were ripped out of your hand by the machine')
                wait()
                print('you marvel at your hand')
                wait()
                print('as blood dripped slowly from it')
                wait()
                print('you scream for help but it is too late')
                lay(12)
                print('...the rock of death has claimed your soul')
                lay(15)
                print('alas... tis machine that will conquer man')
            if comp == 1:
                print('furious, you prepare to smash the computer to pieces with your deadly rock')
                wait()
                print('but suddenly you hear the printer begin to operate')
                wait()
                print('the printer projects a terrible and frightful noise, not too disimilar from the hell-born sound of an alarm clock')
                wait()
                print('but wait... it is an alarm clock')
                wait()
                print('you wake up; leaping out of your bead')
                wait()
                print('what a strange dream you think')
                wait()
                print('you then open your dream journal to record it')
                wait()
                print('but sadly... desperately sadly you recieve a paper cut')
                wait()
                print('this paper cut becomes infected and before you know it...')
                wait()
                print('You die')
                lay(26)
                print('DRAMATICALLY......')
            if comp == 2:
                print('the computer waged information warfare upon you')
                wait()
                print('the whole of society was hipmotized to kill you with scissors')
                wait()
                print('they killed you... but donated your organs to a healthcare charity')
                wait()
                print('your organs are used throughout the world and save five lives')
                wait()
                print('congradulations!')
                wait()
                print('but you are unable to celebrate... because you are dead')
                wait()
                print('remember... never bring paper to a scissor fight')
                wait()
                wait()
                print('but actually though... don\'t do it again')
        else:
            print('YOU LOSE :(')
    if w == 2:
        point = point + 1
        winrate = winrate + 1
        print('YOU WON! ;)')
        
    if w == 0:
        print('tis a DRAW')

    print('')
    lay(4)
    print('you have' , point , 'victory points')
    lay(2)
    if (winrate + loserate) != 0:
        winper = 10000 * winrate // (winrate + loserate)
        winper = winper / 100
    print('winrate: ' , winper , '%')
        
    
