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

'''Microsoft Windows [Version 10.0.17134.1345]
(c) 2018 Microsoft Corporation. Alle rechten voorbehouden.

C:\Users\Linda Vos>sqlite3
SQLite version 3.40.1 2022-12-28 14:03:47
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .exit

C:\Users\Linda Vos>'''



