# Imports
import argparse
import csv
from datetime import date
from helper import *


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass

# WELKE PRODUCTEN BIEDT DE SUPERMARKT AAN?
# maak een csv bestand, inventaris + header (helper.py)
# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv')

# voeg regels invetaris toe aan het document (helper.py)
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv', 'id', 'Apple', 0, 0, '9999-12-31')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv', 'id', 'Banana', 0, 0, '9999-12-31')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv', 'id', 'Pear', 0, 0, '9999-12-31')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv', 'id', 'Mandarine', 0, 0, '9999-12-31')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv', 'id', 'Kiwi', 0, 0, '9999-12-31')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv', 'id', 'Apple', 0, 0, '9999-12-31')  # nakijken of het werkt

# maak een functie die de inventaris uitleest en deze laat zien
def inventory(filename): 

    with open(filename, mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list_products = []      
        
        for row in csv_reader:
            product = row['product']
            # print(product) # laat dezelfde producten twee keer zien (gewenste lijst maken)
            if product not in list_products:
                list_products.append(product)

    print(list_products)


# inventory('test.csv')
# inventory('inventory.csv')


# VOOR HOEVEEL IS ELK TYPE PRODUCT GEKOCHT EN WAT IS DE VERVALDATUM?
# maak een csv bestand, purchases en shrijf een header (helper.py)
# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv')

# voeg regels invetaris toe aan het document (helper.py)
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Apple', 4, 2, '2023-10-19')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Banana', 4, 2, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Pear', 4, 2, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Mandarine', 4, 2, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Kiwi', 4, 2, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Apple', 4, 1, '2023-10-18')  # nakijken of het werkt

# Voor hoeveel elk product is gekocht en wat de vervaldatum is
def purchase_information(filename):
    with open(filename, mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)  
        
        for row in csv_reader:
            product = row['product']
            price = int(row['price'])
            amount = int(row['amount'])
            date = row['expiration_date']
            total_purchase_price = amount * price
            print(f'This {product} was {price} euro per piece and the total amount of {amount} was purchased for {total_purchase_price} euro\'s')
            print(f'and in addition, this {product} is best before {date}')


# purchase_information('purchases.csv')


# VOOR HOEVEEL IS ELK TYPE PRODUCT VERKOCHT? OF ALS HET OVER DATUM IS TOESCHRIJVEN NAAR DERVING.CSV
# maak een csv bestand, sales en schrijf een header (helper.py)
# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv')

# voeg regels invetaris toe aan het document (helper.py)
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv', 'id', 'Apple', 2, 4, '2023-10-19')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv', 'id', 'Banana', 2, 4, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv', 'id', 'Pear', 2, 4, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv', 'id', 'Mandarine', 2, 4, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv', 'id', 'Kiwi', 2, 4, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv', 'id', 'Apple', 2, 3, '2023-10-18')  # nakijken of het werkt

# functie schrijven die laat zien voor hoeveel elk type product is verkocht
def sales_information(filename):
    with open(filename, mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)  
        
        for row in csv_reader:
            product = row['product']
            price = int(row['price'])
            amount = int(row['amount'])
            total_sales_price = amount * price
            print(f'This {product} was sold for {price} euro and the total of {amount} pieces was sold for {total_sales_price} euro\'s')

# sales_information('sales.csv')

# functie die kan laten zien hoeveel derving er is (over gespecificeerde tijdsperioden??)

# HOEVEEL VAN ELK TYPE PRODUCT HEEFT DE SUPERMARKT NU OP VOORRAAD?
# maak een functie die de voorrraad uitleest en deze laat zien (als deze ook gebruikt kan worden voor andere opdrachten, dan plaatsen bij helper.py)


# RAPPORTAGE VAN DE OMZET OVER GESPECIFICEERDE TIJDSPERIODEN
# RAPPORTAGE VAN DE WINST OVER GESPECIFICEERDE TIJDSPERIODEN


if __name__ == "__main__":
    main()
