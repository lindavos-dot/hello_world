# In het csv bestand wil ik een inkooplijst maken die gesorteerd is op datum. Zodat het duidelijk is op welke dag, wat is aangekocht
# De functies die hier staan gaan over het toevoegen van voorraad aan de inkooplijst(csv bestand)

from datetime import datetime
import os
import csv
import argparse


# werken met tijd

current_time = datetime.now()
required_format = datetime.strftime(current_time, '%Y-%m-%d')

# print(required_format)

# Stap 1 is controleren of het document er is
def check_document():
    path = 'c:/Users/Linda Vos/Desktop/hello-world/superpy/2_bought.csv'
    isFile = os.path.isfile(path)

    if isFile == True:
        inventory_file = isFile

    elif isFile == False:
        with open('2_bought.csv', mode= 'w') as inventory_file:
            return inventory_file


# check_document()

# Stap 2: De header toevoegen aan het document
def stock_writer_header():
    check_document()
    with open('2_bought.csv', mode= 'w', newline='') as stock_file:
        stock_writer = csv.writer(stock_file, delimiter=',')
        header = stock_writer.writerow(['id', 'category', 'name', 'amount', 'price', 'purchase_date', 'expiration_date'])
        return header


stock_writer_header()

# Stap 3: Inventaris toevoegen aan het document
  
def stock_writer(id, category, name, amount, price, purchase_date, expiration_date):
    check_document() 
    
    with open('stock.csv', mode= 'a', newline='') as stock_file:
        stock_writer = csv.writer(stock_file, delimiter=',')
            
        return stock_writer.writerow([id, category, name, amount, price, purchase_date, expiration_date])


# stock_writer('id', 'Fruit', 'Orange', 16, 1,30, '2023-10-15')


# stock_writer with Argparse
parser = argparse.ArgumentParser(description='Enter new stock')

parser.add_argument('--id', type=str, help='Enter id')
parser.add_argument('--category', type=str, help='Enter a category')
parser.add_argument('--name', type=str, help='Enter a name')
parser.add_argument('--amount', type=int, help='Enter an amount')
parser.add_argument('--price', type=float or int, help='Enter a price')
parser.add_argument('--expiration_date', type=str, help='Enter an expiration date (yyyy-mm-dd)')
parser.add_argument('--action', type=str, help='Enter an action')

args = parser.parse_args()

# python 2_bought.py --id id --category Fruit --name Orange --amount 20 --price 1.20 --expiration_date 2022-12-15 --action buy

if args.action == 'buy':
    def stock_writer(id, category, name, amount, price, expiration_date):
        check_document() 
    
        with open('2_bought.csv', mode= 'a', newline='') as stock_file:
            stock_writer = csv.writer(stock_file, delimiter=',')
            id = args.id
            category = args.category
            name = args.name
            amount = args.amount
            price = args.price
            purchase_date = required_format
            expiration_date = args.expiration_date

            return stock_writer.writerow([id, category, name, amount, price, purchase_date, expiration_date])