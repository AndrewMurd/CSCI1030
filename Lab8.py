#Andrew Murdoch
#CSCI 1030U
#Lab8
#2018-11-17


class Character:
    def __init__(self, name, hp, attackpower, defensepower, magic):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.attackpower = attackpower
        self.defensepower = defensepower
        self.magic = magic
    
    def __str__(self):
        return self.name + " has " + self.hp + " HP"
    
    def isDead(self):
        if (self.hp <= 0):
            return True
        else:
            return False
        
    def isPartyDead(self, party):
        for x in range(len(party)):
            if (party[x].hp <= 0):
                return True
            else:
                return False
        
    def attack(self, otherCharacter):
        damage = self.attackpower - otherCharacter.defensepower
        otherCharacter.hp = otherCharacter.hp - damage
        return print(self.name, " does ", damage, " points of damage to ", otherCharacter.name)
    
    def heal(self, party):
        for x in range(len(party)):
            party[x].hp =  + self.magic
            return print(self.name, " heals ", self.magic, " hp for ", party[x].name)
        

krogg = Character('Krogg', 180, 20, 20, 0)
glinda = Character('Glinda', 120, 5, 20, 5)
geoffrey = Character('Geoffrey', 150, 15, 15, 0)
party = [krogg, glinda, geoffrey]
boss = Character('Boss', 500, 25, 15, 0)

round = 1

while (not boss.isDead()) and (not krogg.isPartyDead(party) and not glinda.isPartyDead(party) and not geoffrey.isPartyDead(party)):
    print('Round', round)

    #krogg attacks
    krogg.attack(boss)
    # geoffrey attacks
    geoffrey.attack(boss)

    #glinda heals
    glinda.heal(party)

    #boss attacks
    for partyMember in party:
        boss.attack(partyMember)
    #show progress
    for partyMember in party:
        print(partyMember)
        print(boss)
        print('')

    round += 1
    if isPartyDead(party):
        print('Your whole party is dead. You lose.')
    elif boss.isDead():
        print('The boss is dead. You are victorious!')
    
        