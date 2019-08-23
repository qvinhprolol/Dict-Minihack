import random
champ = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': 'Shield, Breadloaf',
    'Gold': 100,
    'Level': 2
}

spell_list = [
    {
        'Name': 'Tackle',
        'Minimum level': 1,
        'Damage': 5,
        'Hit rate': 0.3
    },
    {
        'Name':'Quick Attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5
    },
    {
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2
    }
]


# for i in range(3):
#     print('Skill '+str(i+1),end="")
#     print(':')
#     for key,value in spell_list[i].items():
#         print(key,value)
#     print('')

print('Available skills: ')
for i in range(3):
    print(i+1,end='')
    print('.',end=' ')
    print(spell_list[i]['Name'])

select = int(input('Select a skill: '))
x = spell_list[select-1]['Minimum level']
y = champ['Level']
z = random.randint(0,1)
if y > x:
    if z > spell_list[select-1]['Hit rate']:
        print('Spell hit!')
        print('Damage: ',spell_list[select-1]['Damage'])
    else:
        print('Missed spell')
else: 
    print('Insufficient level')

