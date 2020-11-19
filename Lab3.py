
kroggAttack = 38.5
kroggDefense = 20.0
kroggHP = 200

bossAttack = 25
bossDefense = 12.5
bossHP = 1500
roundNum = 1

while kroggHP >= 0 and bossHP >= 0:
    roundNum += 1
    print('Round ', roundNum)
    damage = kroggAttack - bossDefense
    bossHP = bossHP - damage
    print('Krogg does ' , damage , ' points of damage to Boss')
    damage = bossAttack - kroggDefense
    kroggHP = kroggHP - damage
    print('Boss does ', damage, ' points of damage to Krogg')
    print('Boss: ', bossHP)
    print('Krogg: ', kroggHP)
    if kroggHP >= 0:
        print('The Krogg has won. You are Victorious!')
        
    if bossHP >= 0:
        print('The Boss has won. You have been Defeated!')
    