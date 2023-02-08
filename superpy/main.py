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
#append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Pear', 4, 2, '2023-10-18')  # nakijken of het werkt
#append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Mandarine', 4, 2, '2023-10-18')  # nakijken of het werkt
#append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Kiwi', 4, 2, '2023-10-18')  # nakijken of het werkt
#append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Apple', 4, 1, '2023-10-18')  # nakijken of het werkt

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

# LATEN ZIEN DAT EEN PRODUCT NIET IS VERKOCHT, MAAR DE HOUDBAARHEIDSDATUM IS VERSTREKEN

def expiration_date_expired(filename):
    check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/expiration_date_expired.csv')
    check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv')
    
    with open(filename, mode= 'r') as read_file:
        csv_reader = csv.DictReader(read_file)
        list_of_csv = list(csv_reader)
        expired_products = []
        
        date_today = today()
        for row in list_of_csv:
            date = row['expiration_date']
            if date <= date_today:
                list_of_csv.remove(row)
                expired_products.append(row)
    
    
    header = ['id','mutation_date','product','amount','price','expiration_date']       
    with open('current_stock.csv', mode= 'w', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader() 
        
        for data in list_of_csv:
            writer.writerow(data) 
    
    header = ['id','mutation_date','product','amount','price','expiration_date']   
    with open('expiration_date_expired.csv', mode= 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader() 
        
        for data in expired_products:
            return writer.writerow(data)  
    
   
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', 'id', 'Apple', 4, 2, '2022-10-19')  # toevoegen over datum appels
# expiration_date_expired('purchases.csv')


# HOEVEEL VAN ELK TYPE PRODUCT HEEFT DE SUPERMARKT NU OP VOORRAAD?

# ALS ER EEN NIEUW PRODUCT WORDT INGEKOCHT: SCHRIJVEN NAAR INKOOP BESTAND EN VOORRAAD BESTAND
def test_buy(path, id, product, amount, price, expiration_date):
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

                    append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_purchases.csv', id, product, amount, price, expiration_date)
        
        else:
            append_new_lines(path, id, product, amount, price, expiration_date)
            append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_purchases.csv', id, product, amount, price, expiration_date)
    

# test_buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_current_stock.csv', 'id', 'Apple', 4, 2, '2023-10-19')
# test_buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/test.csv', 'id', 'Apple', 4, 2, '2023-10-18')
# test_buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/test.csv', 'id', 'Pear', 4, 2, '2023-10-19')

# ALS ER EEN PRODUCT WORDT VERKOCHT: SCHRIJVEN NAAR VERKOOP BESTAND EN VOORRAAD BESTAND

def test_sell(path, id, product, amount, price, expiration_date):
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

                append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_sales.csv', id, product, amount, price, expiration_date)

            else:
                print(f'{product} is sold out')


# test_sell('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_current_stock.csv', 'id', 'Apple', 1, 2, '2023-10-19')

# VOORRAAD AANVRAAG VOOR 1 SPECIFIEK PRODUCT
# begin met opschonen inkoop bestand door expiration_date_expired(filename)

def current_stock(product):
    expiration_date_expired('test_current_stock.csv') # als het goed is staat er nu alleen data in de lijst die niet over datum is    
    
    with open('test_current_stock.csv', mode= 'r') as csv_file:
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
# begin met opschonen inkoop bestand door expiration_date_expired(filename)
def total_in_stock(filename): 
    expiration_date_expired('test_current_stock.csv')
    
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
