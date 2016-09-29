# comp training

act = ['split' , 'use left hit left' , 'use left hit right' , 'use right hit left' , 'use right hit right']

'mistake = []'
wisechoice = []
pwisechoice = []
playerwin = 0
compwin = 0
game = 1
y = input()
y = int(y)
while True:
    plh = 1
    prh = 1
    clh = 1
    crh = 1
    goodmove = []
    pgoodmove = []
    badmove = []
    turn = 0

    game = game + 1
    whofirst = game % 2
    

    while True:
        if whofirst == 0 or turn > 0:
            turn = turn + 1
            save2 = [clh , crh , plh , prh]
            g = 1
            while g == 1:
                if clh + crh == 0:
                    break
                choice = []
                det = int(y**2 - 2 * y + y ** (1.3))
                result = det % 5
                player = act[result]
                choice.append(player)
                'badmove.append(save)'
                'badmove.append(comp)'
                if game > 2:
                    pgoodmove.append(psave)
                    pgoodmove.append(comp)
                # computer strat
                for var in range(0 , len(pwisechoice) , 1):
                    'print(plh , prh , clh , crh, len(wisechoice))'
                    if pwisechoice[var] == [plh , prh , clh , crh]:
                        choice.append(pwisechoice[var + 1])
                        
                chosen = (4 * y - y **2) % (len(choice))
                player = choice[chosen]

                if player == act[0]:
                    if plh == 0 or prh == 0:
                        if plh == 2 or prh == 2:
                            plh = 1
                            prh = 1
                            g = 0
                        if plh == 4 or prh == 4:
                            plh = 2
                            prh = 2
                            g = 0
                if player == act[1]:
                    clh = clh + plh
                if player == act[2]:
                    crh = crh + plh
                if player == act[3]:
                    clh = clh + prh
                if player == act[4]:
                    crh = crh + prh
                if (plh != 0 and player in act[1:3]) or (prh != 0 and player in act[3:5]):
                    g = 0
                y = y + 2
            '''print('p:' , player)'''
                
            if clh > 4:
                clh = 0
            if crh > 4:
                crh = 0
            if clh + crh == 0:
                for x in range(0 , len(goodmove) , 1):
                    'mistake.append(save[x])'
                    'mistake.append(badmove[x])'
                    wisechoice.append(goodmove[x])
                playerwin = playerwin + 1
                '''print('YOU WON!! :D')
                print('game:' , game)
                playerwin = playerwin + 1
                print('playerwin:' , playerwin)'''

                '''print(goodmove)
                print(wisechoice)
                print(turn)'''
                break

                    
            
        if whofirst == 1 or turn > 0:
            
            turn = turn + 1
            cg = 1
            y = y + 1
            psave = [clh , crh , plh , prh]
            while cg == 1:
                choice = []
                if plh + prh == 0:
                    break
                det = int(y + y ** (2.3) - y ** 1.6)
                result = det % 5
                comp = act[result]
                choice.append(comp)
                'badmove.append(save)'
                'badmove.append(comp)'
                goodmove.append(save2)
                goodmove.append(player)
                # computer strat
                for var in range(0 , len(wisechoice) , 1):
                    'print(plh , prh , clh , crh, len(wisechoice))'
                    if wisechoice[var] == [plh , prh , clh , crh]:
                        choice.append(wisechoice[var + 1])
                        
                chosen = (3 * y - y **2) % (len(choice))
                comp = choice[chosen]
                if comp == act[0]:
                    if clh == 0 or crh == 0:
                        if clh == 2 or crh == 2:
                            clh = 1
                            crh = 1
                            cg = 0
                        if clh == 4 or crh == 4:
                            clh = 2
                            crh = 2
                            cg = 0
                if comp == act[1]:
                    plh = plh + clh
                if comp == act[2]:
                    prh = prh + clh
                if comp == act[3]:
                    plh = plh + crh
                if comp == act[4]:
                    prh = prh + crh
                if (clh != 0 and comp in act[1:3]) or (crh != 0 and comp in act[3:5]):
                    cg = 0
                y = y + 1
            

            if plh > 4:
                plh = 0
            if prh > 4:
                prh = 0
            if plh + prh == 0:
                for x in range(0 , len(pgoodmove) , 1):
                    'mistake.append(save[x])'
                    'mistake.append(badmove[x])'
                    pwisechoice.append(pgoodmove[x])

                compwin = compwin + 1
                '''print('YOU LOSE :(')
                print('game:' , game)
                compwin = compwin + 1
                print('compwin:' , compwin)'''
                break

        if game % 100 == 0:
            print('SUCCESS!!' , compwin , playerwin)
          






