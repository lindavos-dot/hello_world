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
        bought_file = isFile

    elif isFile == False:
        with open('2_bought.csv', mode= 'w') as bought_file:
            return bought_file


# check_document()

# Stap 2: De header toevoegen aan het document
def bought_writer_header():
    check_document()
    with open('2_bought.csv', mode= 'w', newline='') as file:
        bought_writer = csv.writer(file, delimiter=',')
        header = bought_writer.writerow(['id', 'purchase_date', 'category', 'name', 'amount', 'price', 'expiration_date'])
        return header


# bought_writer_header()

# Stap 3: Inventaris toevoegen aan het document
  
def stock_writer(id, category, name, amount, price, expiration_date):
    check_document() 
    
    with open('2_bought.csv', mode= 'a', newline='') as file:
        stock_writer = csv.writer(file, delimiter=',')
        purchase_date = required_format    
        return stock_writer.writerow([id, purchase_date, category, name, amount, price, expiration_date])


# stock_writer('id', 'Fruit', 'Orange', 16, 1.30, '2023-10-15')
# stock_writer('id', 'Fruit', 'Apple', 16, 1, '2023-10-15')


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

# python 2_bought.py --id id --category Fruit --name Banana --amount 20 --price 1.20 --expiration_date 2022-12-15 --action buy

if args.action == 'buy':
    check_document() 
    with open('2_bought.csv', mode= 'a', newline='') as file:
        stock_writer = csv.writer(file, delimiter=',')
        id = args.id
        purchase_date = required_format
        category = args.category
        name = args.name
        amount = args.amount
        price = args.price
        expiration_date = args.expiration_date
        stock_writer.writelines([id, purchase_date, category, name, amount, price, expiration_date])

