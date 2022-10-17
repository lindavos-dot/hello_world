

# First step? How do i want to structure data?

# inventory (inventaris)
# stock (voorraad, met datum?)
# bought (inkoop met naam, prijs, aantal, houdbaarheidsdatum)
# sold (verkoop met naam, prijs, aantal, houdbaarheidsdatum of als de houdbaarheidsdatum is vervallen. Het feit dat dit is gebeurt)
# past_expiration_date (artikelen die over datum zijn gegaan en uit de voorraad lijst worden gehaald, worden hier opgeslagen)

# Beginnen met inventory. Welke producten biedt de supermarkt aan?

import os
import csv


# Stap 1: Bestaat het csv document? met de os-module?
def check_document():
    path = "c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv"
    isFile = os.path.isfile(path)

    if isFile == True:
        inventory_file = isFile
        print("inventory.csv bestaat al")

    elif isFile == False:
        with open('inventory.csv', mode= 'a') as inventory_file:
            print("inventory.csv is aangemaakt")
            return inventory_file
        

# check_document()

# Stap 2: De header toevoegen aan het document        TOEVOEGEN CHECKEN OF HET BESTAAT??
def inventory_writer_header():
    check_document()
    with open('inventory.csv', mode= 'w') as inventory_file:
        inventory_writer = csv.writer(inventory_file, delimiter=',')
        header = inventory_writer.writerow(['id', 'category', 'name'])
        return header


# Stap 3: Inventaris toevoegen aan het document EERST DOCUMENT LEZEN, DAARNA SCHRIJVEN
def inventory_writer(category, name):
    check_document()
    with open('inventory.csv', mode= 'w') as inventory_file:
        inventory_writer = csv.writer(inventory_file, delimiter=',')

        inventory_writer.writerow(['id', 'Fruit', 'Orange'])
        inventory_writer.writerow(['id', 'Fruit', 'Apple'])
        inventory_writer.writerow(['id', 'Fruit', 'Pear'])
        inventory_writer.writerow(['id', 'Bread and banquet', 'Bread'])
        inventory_writer.writerow(['id', 'Dairy', 'Cheese'])
        inventory_writer.writerow(['id', 'Toppings', 'marmalade'])'''
        
    