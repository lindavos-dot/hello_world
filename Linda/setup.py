from models1 import (db, ZooKeeper, Enclosure, Animal)

import peewee

def data_test():
    db.connect()
    db.create_tables([Animal, ZooKeeper, Enclosure])

def data_writer():
    db.connect()
    zoo_keepers = ["Aidan", "Sharon", "Bob"]
    enclosures = [["barrel", 2], ["desert_enclosure", 1], ["savanna_enclosure", 2], ["jungle_enclosure", 2], ["jungle_enclosure", 2]]
    animals = [["Phil", "Meerkat", 2], ["Wendy", "Meerkat", 2], ["Simon", "Meerkat", 2], ["John", "Tiger", 3], ["Bob", "Snake", 4], ["Carly", "Parrot", 5]]

    for zoo_keeper_name in zoo_keepers:
        ZooKeeper.create(name = zoo_keeper_name)
    
    for enclosure in enclosures:
        Enclosure.create(name = enclosure[0], feeder = enclosure[1])

    for animal in animals:
        Animal.create(name = animal[0], type = animal[1], enclosure = animal[2])


def print_animal_names():
    for animal in Animal.select():
        print(animal.type)

def print_animal_names_savanne_enclosure():
    query = Animal.select(Animal, Enclosure).join(Enclosure).where(Enclosure.name == "savanna_enclosure")
    
    for animal in query:
        print(animal.name)
