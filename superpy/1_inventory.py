

# First step? How do i want to structure data?

# inventory (inventaris toevoegen en laten zien)
# bought (inkoopbestand)
# sold (verkoopbestand)
# past_expiration_date (dervingbestand)
# stock (voorraad bestand, die bijgewerkt wordt door bought, sold, past_expiration_date betanden/functies)

# Beginnen met inventory. Welke producten biedt de supermarkt aan?

import os
import csv
from itertools import islice


# Stap 1: Bestaat het csv document? met de os-module?
def check_document():
    path = 'c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv'
    isFile = os.path.isfile(path)

    if isFile == True:
        inventory_file = isFile

    elif isFile == False:
        with open('inventory.csv', mode= 'w') as inventory_file:
            return inventory_file
        

# check_document()

# Stap 2: De header toevoegen aan het document
def inventory_writer_header():
    check_document()
    with open('inventory.csv', mode= 'w', newline='') as inventory_file:
        inventory_writer = csv.writer(inventory_file, delimiter=',')
        header = inventory_writer.writerow(['id', 'category', 'name'])
        return header


# Stap 3: Inventaris toevoegen aan het document
def inventory_writer():
    check_document()
    with open('inventory.csv', mode= 'a', newline='') as inventory_file:
        inventory_writer = csv.writer(inventory_file, delimiter=',')

        inventory_writer.writerow(['id', 'Fruit', 'Orange'])
        inventory_writer.writerow(['id', 'Fruit', 'Apple'])
        inventory_writer.writerow(['id', 'Fruit', 'Pear'])
        inventory_writer.writerow(['id', 'Bread and banquet', 'Bread'])
        inventory_writer.writerow(['id', 'Dairy', 'Cheese'])
        inventory_writer.writerow(['id', 'Toppings', 'Marmalade'])


# inventory_writer_header()        
# inventory_writer()   

# Stap 4: De inventaris laten zien
def inventory():
    with open('inventory.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_file)
        for line in csv_reader:
            print(line[1:])


# inventory()