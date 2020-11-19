#Andrew Murdoch
#CSCI 1030U
#Lab4
#2018-10-25

partyNames = ['Krogg', 'Glinda', 'Geoffrey']
partyHP = [180, 120, 150]
partyAttack = [20, 5, 15]
partyDefense = [20, 20, 15]
partyDead = [False, False, False]
bossAttack = 25
bossDefense = 15
bossHP = 500
roundNum = 0
Dead = False

def isPartyDead(Dead):
    if partyHP[0] <= 0 and partyHP[1] <= 0 and partyHP[2] <= 0:
        return True
            
def isDead(a):
    if partyHP[a] <= 0:
        partyDead[a] = True
    else: 
        partyDead[a] = False

while Dead == False and bossHP > 0:
    
    print(Dead)
    isPartyDead(Dead)
    isDead(0)
    isDead(1)
    isDead(2)
    
    roundNum = roundNum + 1
    print("")
    print('Round ', roundNum)
    
    if partyDead[0] == True:
        print ("Krogg cannot attack because he is dead")
    
    if partyDead[0] != True:
        damage = partyAttack[0] - bossDefense
        bossHP = bossHP - damage
        print('Krogg does ' , damage , ' points of damage to Boss')
    
    if partyDead[2] != True:
        damage = partyAttack[2] - bossDefense
        bossHP = bossHP - damage
        print('Geoffrey does ' , damage , ' points of damage to Boss')
        
    if partyDead[2] == True:
        print ("Geoffrey cannot attack because he is dead")
        
    if partyDead[1] != True:
        damage = bossAttack - partyDefense[1]
        partyHP[1] = partyHP[1] - damage
        print('Boss does ', damage, ' points of damage to Glinda')
        partyHP[1] += 5
    
    if partyDead[2] != True:
        damage = bossAttack - partyDefense[2]
        partyHP[2] = partyHP[2] - damage
        print('Boss does ', damage, ' points of damage to Geoffrey')
        partyHP[2] += 5
        
    if (partyDead[0] != True):
        damage = bossAttack - partyDefense[0]
        partyHP[0] = partyHP[0] - damage
        print('Boss does ', damage, ' points of damage to Krogg')
        partyHP[0] += 5

    
    print('Boss: ', bossHP)
    print('Krogg: ', partyHP[0])
    print('Glinda: ', partyHP[1])
    print('Geoffrey: ', partyHP[2])
        
    
if Dead == False:
    print('\nThe boss is dead. You are Victorious!')
        
if bossHP > 0:
    print('\nThe party is dead. You have been Defeated!')

