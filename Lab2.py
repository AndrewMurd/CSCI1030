
kroggName = 'Krogg'
kroggClass = 'Warrior'
kroggLevel = 1
kroggAttack = 18.5
kroggDefense = 12.5
kroggHP = 200
kroggXP = 0
kroggWeapons = ['Axe', 'Dagger', 'Unarmed']

krogg = (kroggName, kroggClass, kroggLevel, kroggAttack, 
         kroggDefense, kroggHP, kroggXP, kroggWeapons)


glindaName = 'Glinda'
glindaClass = 'Spellcaster'
glindaLevel = 1
glindaAttack = 4.5
glindaDefense = 25.0
glindaHP = 120 
glindaXP = 0
glindaWeapons = ['Staff','Unarmed']

glinda = (glindaName, glindaClass, glindaLevel, glindaAttack, 
          glindaDefense, glindaHP, glindaXP, glindaWeapons)

darkDragonName = 'Dark Dragon'
darkDragonClass = 'Boss'
darkDragonLevel = 10
darkDragonAttack = 25 
darkDragonDefense = 17.5
darkDragonHP = 500
darkDragonXP = 1000
darkDragonWeapons = ['Flame', 'Breath']

darkDragon = (darkDragonName, darkDragonClass, darkDragonLevel,
              darkDragonAttack, darkDragonDefense, darkDragonHP,
              darkDragonXP, darkDragonWeapons)

party = (krogg, glinda)

#krogg attacking dragon
damage = kroggAttack - darkDragonDefense
remainingHP = darkDragonHP - damage

print('Krogg is attacking the Dark Dragon for '+ str(damage) + ' damage.', 
      'The Dark Dragons remaining HP is ' + str(remainingHP))
