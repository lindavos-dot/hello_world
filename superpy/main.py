# Imports
import argparse
import csv
from datetime import date
from helper import *


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.


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
            price = float(row['price'])
            amount = float(row['amount'])
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
            price = float(row['price'])
            amount = float(row['amount'])
            total_sales_price = amount * price
            print(f'This {product} was sold for {price} euro and the total of {amount} pieces was sold for {total_sales_price} euro\'s')


# sales_information('sales.csv')


# HOEVEEL VAN ELK TYPE PRODUCT HEEFT DE SUPERMARKT NU OP VOORRAAD?
# ALS ER EEN NIEUW PRODUCT WORDT INGEKOCHT: SCHRIJVEN NAAR INKOOP BESTAND EN VOORRAAD BESTAND

def buy(product, amount, price, expiration_date):
    path = 'c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv'
    id = 'id'
    check_document(path)    
    
    with open(path, mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader: 
            
            if row['product'] == product and row['expiration_date'] == expiration_date:
                    current_amount = float(row['amount'])
                    new_amount = current_amount + amount

                    text = open(path, mode= 'r')
                    text = ''.join([word for word in text]).replace(str(current_amount), str(new_amount))
                
                    updated_stock = open(path, mode= 'w')
                    updated_stock.writelines(text)

                    append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', id, product, amount, price, expiration_date)
        
            else:
                append_new_lines(path, id, product, amount, price, expiration_date)
                append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv', id, product, amount, price, expiration_date)
    

# ALS ER EEN PRODUCT WORDT VERKOCHT: SCHRIJVEN NAAR VERKOOP BESTAND EN VOORRAAD BESTAND

def sell(path, id, product, amount, price, expiration_date):
    path = 'c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv'
    id = 'id'
    check_document(path)
    
    with open(path, mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            
            if row['product'] == product and row['expiration_date'] == expiration_date:
                current_amount = float(row['amount'])
                new_amount = current_amount - amount

                text = open(path, mode= 'r')
                text = ''.join([word for word in text]).replace(str(current_amount), str(new_amount))
                
                updated_stock = open(path, mode= 'w')
                updated_stock.writelines(text)
                updated_stock.close()

                append_new_lines(path, id, product, amount, price, expiration_date)

            else:
                print(f'{product} is sold out')


# VOORRAAD AANVRAAG VOOR 1 SPECIFIEK PRODUCT

def current_stock(product):
    expiration_date_expired() # als het goed is staat er nu alleen data in de lijst die niet over datum is    
    
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

# VOORRAAD AANVRAAG VOOR ALLE PRODUCTEN IN STOCK

def total_in_stock(filename): 
    expiration_date_expired()
    
    with open(filename, mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            product = row['product']
            amount = row['amount']
            date = row['expiration_date']
            print(f'We currently have a total of {amount} {product} in stock and these will be expired by {date}')


# total_in_stock('current_stock.csv')

# VAN WELKE PRODUCTEN OP VOORRAAD IS DE HOUDBAARHEIDSDATUM VERSTREKEN?
def spoiled_products(): 
    expiration_date_expired()
    
    with open('expiration_date_expired.csv', mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            product = row['product']
            amount = row['amount']
            print(f'Of this {product} , a total of {amount} have expired')


# spoiled_products()


# RAPPORTAGE VAN DE OMZET OVER GESPECIFICEERDE TIJDSPERIODEN (omzet: verkoopprijs * aantal)

def revenue(start_date, end_date):
    with open('sales.csv', mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)  
        total_revenue = 0

        for row in csv_reader:
            if row['mutation_date'] >= start_date and row['mutation_date'] <= end_date:
                price = float(row['price'])
                amount = float(row['amount'])
                total_revenue += price * amount
                print(total_revenue)
            else:
                print('please check the start date and end date, required format is: yyyy-mm-dd')
    

# revenue('2023-01-01', '2023-02-12')
# revenue('2023-01-01', '2023-02-28')

# RAPPORTAGE VAN DE WINST OVER GESPECIFICEERDE TIJDSPERIODEN (winst in deze situatie: verkoopprijs - inkoopprijs)

def profit(start_date, end_date):
    with open('sales.csv', mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)  
        total_revenue = 0

        for row in csv_reader:
            if row['mutation_date'] >= start_date and row['mutation_date'] <= end_date:
                price = float(row['price'])
                amount = float(row['amount'])
                total_revenue += price * amount

    with open('purchases.csv', mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)  
        total_purchase = 0

        for row in csv_reader:
            if row['mutation_date'] >= start_date and row['mutation_date'] <= end_date:
                price = float(row['price'])
                amount = float(row['amount'])
                total_purchase += price * amount

                profit = total_revenue - total_purchase
        
        return print(profit)


# profit('2023-01-01', '2023-02-12')

# Superpy command line tool: werken met Parser en subparsers

# WELKE PRODUCTEN BIEDT DE SUPERMARKT AAN? "inventory"
# VOOR HOEVEEL IS ELK TYPE PRODUCT GEKOCHT EN WAT IS DE VERVALDATUM? "purchases"
# VOOR HOEVEEL IS ELK TYPE PRODUCT VERKOCHT? "sales"
# VAN WELKE PRODUCTEN OP VOORRAAD IS DE HOUDBAARHEIDSDATUM VERSTREKEN? "lack"
# HOEVEEL VAN ELK TYPE PRODUCT HEEFT DE SUPERMARKT NU OP VOORRAAD? "stock"

# RAPPORTAGE VAN DE OMZET OVER GESPECIFICEERDE TIJDSPERIODEN "revenue"
# RAPPORTAGE VAN DE WINST OVER GESPECIFICEERDE TIJDSPERIODEN "profit"

def main(command_line=None):
    parser = argparse.ArgumentParser(description='Superpy command line tool for for supermarket data')
    subparsers = parser.add_subparsers(dest='command')

    # Subparser "inventory"
    get_inventory = subparsers.add_parser('inventory', help= 'Shows the inventory of the supermarket')
    
    # Subparser "purchases"
    get_purchases = subparsers.add_parser('purchases', help= 'Shows the purchases of the supermarket')   
    
    # Subparser "sales"
    get_sales = subparsers.add_parser('sales', help= 'Shows the sales of the supermarket')
    
    # Subparser "lack"
    get_lack = subparsers.add_parser('lack', help= 'Shows the shrinkage of the supermarket')
    
    # Subparser "stock"
    get_stock = subparsers.add_parser('stock', help= 'Shows the stock of the supermarket')
    
    # Subparser "buy"
    ad_buy = subparsers.add_parser('buy', help= 'add new purchase to current stock file and purchases file')
    ad_buy.add_argument('product', help= 'Please enter the name of the purchased item')
    ad_buy.add_argument('amount', help= 'Please enter the amount of the purchased item')
    ad_buy.add_argument('price', help= 'Please enter the price of the purchased item')
    ad_buy.add_argument('expiration_date', help= 'Please enter an expiration date in the following format: yyyy-mm-dd')

    # Subparser "sell"
    ad_sell = subparsers.add_parser('sell', help= 'remove stock from the current stock file and sales file')
    ad_sell.add_argument('product', help= 'Please enter the name of the sold item')
    ad_sell.add_argument('amount', help= 'Please enter the amount of the sold item')
    ad_sell.add_argument('price', help= 'Please enter the price of the sold item')
    ad_sell.add_argument('expiration_date', help= 'Please enter an expiration date in the following format: yyyy-mm-dd')

    # Subparser "revenue"
    get_revenue = subparsers.add_parser('revenue', help= 'Shows the revenue of the supermarket. Please enter dates in the following format: yyyy-mm-dd')
    get_revenue.add_argument('start_date', help= 'Please enter a start date in the following format: yyyy-mm-dd')
    get_revenue.add_argument('end_date', help= 'Please enter a start date in the following format: yyyy-mm-dd')

    # Subparser "profit"
    get_profit = subparsers.add_parser('profit', help= 'Shows the profit of the supermarket. Please enter dates in the following format: yyyy-mm-dd')
    get_profit.add_argument('start_date', help= 'Please enter a start date in the following format: yyyy-mm-dd')
    get_profit.add_argument('end_date', help= 'Please enter a start date in the following format: yyyy-mm-dd')


    args = parser.parse_args(command_line)

    if args.command == 'inventory':     # python main.py inventory
        inventory('inventory.csv')
    
    elif args.command == 'purchases':       # python main.py purchases
        purchase_information('purchases.csv')

    elif args.command == 'sales':       # python main.py sales
        sales_information('sales.csv')

    elif args.command == 'lack':       # python main.py lack
        spoiled_products()
    
    elif args.command == 'stock':       # python main.py stock
        total_in_stock('current_stock.csv')
    
    elif args.command == 'buy':       # python main.py buy 'Plum', 4, 2, '2023-10-19'
        buy(args.product, args.amount, args.price, args.expiration_date)
    
    elif args.command == 'sell':       # python main.py sell 'Apple', 4, 2, '2023-10-19'
        buy(args.product, args.amount, args.price, args.expiration_date)

    elif args.command == 'revenue':       # python main.py revenue 2023-01-01 2023-02-28      
        revenue(args.start_date, args.end_date)
    
    elif args.command == 'profit':       # python main.py profit 2023-01-01 2023-02-28      
        profit(args.start_date, args.end_date)

    else:
        print('Command not recognized (choose from \'inventory\', \'purchases\', \'sales\', \'lack\', \'stock\', \'buy\', \'sell\',\'revenue\', \'profit\')')



if __name__ == "__main__":
    main()
