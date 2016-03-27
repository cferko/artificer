import numpy as np

class Character():

    def __init__(self,
                 name,
                 race,
                 house,
                 age,
                 strength,
                 constitution,
                 dexterity,
                 intelligence,
                 wisdom,
                 charisma):
                     
        self.name = name
        self.race = race
        self.house=house
        self.age = age
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        
    def __str__(self):
        return self.name+" d'"+self.house
        
def generate_stats():
    keeper_scores = []
    
    for ability_index in range(6):
        these_rolls = []
        for roll_index in range(4):
            these_rolls.append(np.random.randint(low=1, high=7))
        
        this_sum = sum(sorted(these_rolls)[-3:]) ## Add up three largest
        
        keeper_scores.append(this_sum)
        
    return keeper_scores
    
surnames = ['Cadon', 'Donric', 'Ghammara', 'Jeordo', 'Kjaldar', 'Larenthil', 'Micaeli', 'Oraite', 'Phaelanmyr', 
                'Saryn', 'Thagash', 'Vernalis']
                
flavor_mapping = {
    'Cadon':'Human',
    'Donric':'Human',
    'Ghammara':'Halfling',
    'Jeordo':'Halfling',
    'Kjaldar':'Dwarven',
    'Larenthil':"Elven",
    'Micaeli':'Elven',
    'Oraite':'Human',
    'Saryn':'Gnomish',
    'Thagash':'Orcish',
    'Vernalis':'Human',
    'Phaelanmyr':'Elven'}
    
flavor_lists = {
    'Human':('Cadon', 'Donric', 'Oraite', 'Vernalis'),
    'Halfling':('Ghammara', 'Jeordo'),
    'Elven':('Larenthil', 'Micaeli', 'Phaelanmyr'),
    'Orcish':('Thagash',),
    'Gnomish':('Saryn',),
    'Dwarven':('Kjaldar',)
    }
    
reverse_flavor = {value:key for key, value in flavor_mapping.items()}
    
def get_character(first_name, house, race):
    raw_stats = generate_stats()
    
    if race=="forgeling":
        strength = raw_stats[0] + 2
        constitution = raw_stats[1] + 2
        age = np.random.randint(3, 34) ## Window of forgeling creation
    else:
        strength = raw_stats[0]
        constitution = raw_stats[1]
        age = np.random.randint(18, 60) ## Humans and Kalashi age similarly
    
    dexterity = raw_stats[2]
    intelligence = raw_stats[3]    
    
    if race=='kalashi':
        wisdom = raw_stats[4] + 2
        charisma = raw_stats[5] + 2
    else:
        wisdom = raw_stats[4]
        charisma = raw_stats[5]

    this_char = Character(first_name,
                          race,
                          house,
                          age,
                          strength,
                          constitution,
                          dexterity,
                          intelligence,
                          wisdom,
                          charisma)
    return this_char