import random


lijst = ['Bob', 'Linda', 'Wander']


def wie_moet_de_afwas_doen():
    
    afwasser = []
    
    while len(afwasser) < 1:
        random_name = random.choice(lijst)
        
        if random_name != 'Linda':
            afwasser.append(random_name)
            print(f'{afwasser} moet de vaat in de vaatwasser zetten')


wie_moet_de_afwas_doen()



