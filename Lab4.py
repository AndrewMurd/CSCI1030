#Andrew Murdoch
#CSCI 1030U
#Lab4
#2018-10-10

partyNames = ['Krogg', 'Glinda', 'Geoffrey']
partyHP = [180, 120, 150]
partyAttack = [20, 5, 15]
partyDefense = [20, 20, 15]
partyDead = [False, False, False]
bossAttack = 25
bossDefense = 15
bossHP = 500
roundNum = 0

while (partyDead[0] == "false" and partyDead[1] == "false" and partyDead[2] == "false") or bossHP > 0:
    
    roundNum = roundNum + 1
    print("")
    print('Round ', roundNum)
    
    if partyDead[0] == "true":
        print ("Krogg cannot attack because he is dead")
    
    if partyDead[0] != "true":
        damage = partyAttack[0] - bossDefense
        bossHP = bossHP - damage
        print('Krogg does ' , damage , ' points of damage to Boss')
    
    if partyDead[2] != "true":
        damage = partyAttack[2] - bossDefense
        bossHP = bossHP - damage
        print('Geoffrey does ' , damage , ' points of damage to Boss')
        
    if partyDead[2] == "true":
        print ("Geoffrey cannot attack because he is dead")
        
    if partyDead[1] != "true":
        damage = bossAttack - partyDefense[1]
        partyHP[1] = partyHP[1] - damage
        print('Boss does ', damage, ' points of damage to Glinda')
        partyHP[1] += 5
    
    if partyDead[2] != "true":
        damage = bossAttack - partyDefense[2]
        partyHP[2] = partyHP[2] - damage
        print('Boss does ', damage, ' points of damage to Geoffrey')
        partyHP[2] += 5
        
    if (partyDead[0] != "true"):
        damage = bossAttack - partyDefense[0]
        partyHP[0] = partyHP[0] - damage
        print('Boss does ', damage, ' points of damage to Krogg')
        partyHP[0] += 5

    
    print('Boss: ', bossHP)
    print('Krogg: ', partyHP[0])
    print('Glinda: ', partyHP[1])
    print('Geoffrey: ', partyHP[2])
    
    if partyHP[0] <= 0:
        partyDead[0] = "true"
        
    if partyHP[1] <= 0:
        partyDead[1] = "true"
        
    if partyHP[2] <= 0:
        partyDead[2] = "true"
    
    #if partyHP[0] > 0 and partyHP[1] > 0 and partyHP[2] > 0:
    #    print('The Party has won. You are Victorious!')
        
    #if bossHP > 0:
    #   print('The Boss has won. You have been Defeated!')
