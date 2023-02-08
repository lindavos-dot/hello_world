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


# inventory('inventory.csv')


# VOOR HOEVEEL IS ELK TYPE PRODUCT GEKOCHT EN WAT IS DE VERVALDATUM?

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

# VOOR HOEVEEL IS ELK TYPE PRODUCT VERKOCHT?
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


# HOEVEEL VAN ELK TYPE PRODUCT HEEFT DE SUPERMARKT NU OP VOORRAAD?

# ALS ER EEN NIEUW PRODUCT WORDT INGEKOCHT: SCHRIJVEN NAAR INKOOP BESTAND EN VOORRAAD BESTAND

def buy(path, id, product, amount, price, expiration_date):
    check_document(path)    
    
    with open(path, mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader: 
            
            if row['product'] == product and row['expiration_date'] == expiration_date:
                    current_amount = int(row['amount'])
                    new_amount = current_amount + amount

                    text = open(path, mode= 'r')
                    text = ''.join([word for word in text]).replace(str(current_amount), str(new_amount))
                
                    updated_stock = open(path, mode= 'w')
                    updated_stock.writelines(text)

                    append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', id, product, amount, price, expiration_date)
        
        else:
            append_new_lines(path, id, product, amount, price, expiration_date)
            append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', id, product, amount, price, expiration_date)
    

# buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv', 'id', 'Apple', 4, 2, '2023-10-19')
# buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv', 'id', 'Apple', 4, 2, '2023-10-18')
# buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv', 'id', 'Pear', 4, 2, '2023-10-19')

# buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv', 'id', 'Apple', 4, 2, '2022-10-19')  # toevoegen over datum appels


# ALS ER EEN PRODUCT WORDT VERKOCHT: SCHRIJVEN NAAR VERKOOP BESTAND EN VOORRAAD BESTAND

def sell(path, id, product, amount, price, expiration_date):
    check_document(path)
    
    with open(path, mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            
            if row['product'] == product and row['expiration_date'] == expiration_date:
                current_amount = int(row['amount'])
                new_amount = current_amount - amount

                text = open(path, mode= 'r')
                text = ''.join([word for word in text]).replace(str(current_amount), str(new_amount))
                
                updated_stock = open(path, mode= 'w')
                updated_stock.writelines(text)
                updated_stock.close()

                append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv', id, product, amount, price, expiration_date)

            else:
                print(f'{product} is sold out')


# sell('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv', 'id', 'Apple', 1, 2, '2023-10-19')

# VOORRAAD AANVRAAG VOOR 1 SPECIFIEK PRODUCT

def current_stock(product):
    expiration_date_expired('current_stock.csv') # als het goed is staat er nu alleen data in de lijst die niet over datum is    
    
    with open('current_stock.csv', mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            if row['product'] == product:
                amount = row['amount']
                print(f'We currently have a total of {amount} {product} in stock')
            
            else:
                print(f'{product} is sold out')


# current_stock('Apple')
# current_stock('Pear')

# VOORRAAD AANVRAAG VOOR ALLE PRODUCTEN IN STOCK (toepassing voor de jaarlijkse balans)

def total_in_stock(filename): 
    expiration_date_expired('current_stock.csv')
    
    with open(filename, mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            product = row['product']
            amount = row['amount']
            print(f'We currently have a total of {amount} {product} in stock')


# total_in_stock('test_current_stock.csv')


# RAPPORTAGE VAN DE OMZET OVER GESPECIFICEERDE TIJDSPERIODEN
# RAPPORTAGE VAN DE WINST OVER GESPECIFICEERDE TIJDSPERIODEN


if __name__ == "__main__":
    main()
