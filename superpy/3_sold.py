# In het csv bestand wil ik een verkooplijst maken die gesorteerd is op datum. Zodat het duidelijk is op welke dag, wat is verkocht


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
    path = 'c:/Users/Linda Vos/Desktop/hello-world/superpy/3_sold.csv'
    isFile = os.path.isfile(path)

    if isFile == True:
        sold_file = isFile

    elif isFile == False:
        with open('3_sold.csv', mode= 'w') as sold_file:
            return sold_file


# check_document()

# Stap 2: De header toevoegen aan het document
def sold_writer_header():
    check_document()
    with open('3_sold.csv', mode= 'w', newline='') as file:
        sold_writer = csv.writer(file, delimiter=',')
        header = sold_writer.writerow(['id', 'sale_date', 'category', 'name', 'amount', 'price', 'expiration_date'])
        return header


# sold_writer_header()

# Stap 3: Inventaris toevoegen aan het document
  
def stock_writer(id, category, name, amount, price, expiration_date):
    check_document() 
    
    with open('3_sold.csv', mode= 'a', newline='') as file:
        stock_writer = csv.writer(file, delimiter=',')
        sale_date = required_format    
        return stock_writer.writerow([id, sale_date, category, name, amount, price, expiration_date])


# stock_writer('id', 'Fruit', 'Orange', 2, 1.30, '2023-10-15')
# stock_writer('id', 'Fruit', 'Apple', 2, 1, '2023-10-15')


# stock_writer with Argparse: 'sell' = verkoop. Als er iets wordt verkocht, moet de verkooplijst.
# normaal zou er tussen het bijwerken van de inkooplijst en de voorraadlijst een controle op de vrachtbon zitten en daarna de lijsten bijwerken
parser = argparse.ArgumentParser(description='Enter new stock')

parser.add_argument('--id', type=str, help='Enter id')
parser.add_argument('--category', type=str, help='Enter a category')
parser.add_argument('--name', type=str, help='Enter a name')
parser.add_argument('--amount', type=int, help='Enter an amount')
parser.add_argument('--price', type=float or int, help='Enter a price')
parser.add_argument('--expiration_date', type=str, help='Enter an expiration date (yyyy-mm-dd)')
parser.add_argument('--action', type=str, help='Enter an action')

args = parser.parse_args()

# python 3_sold.py --id id --category Fruit --name Banana --amount 20 --price 1.20 --expiration_date 2022-12-15 --action sell

# bijwerken inkooplijst
if args.action == 'sell':
    check_document() 
    with open('3_sold.csv', mode= 'a', newline='') as file:
        stock_writer = csv.writer(file, delimiter=',')
        id = args.id
        sale_date = required_format
        category = args.category
        name = args.name
        amount = args.amount
        price = args.price
        expiration_date = args.expiration_date
        stock_writer.writerow([id, sale_date, category, name, amount, price, expiration_date])

# bijwerken voorraadlijst (als naam en houdbaarheidsdatum gelijk aan elkaar zijn: dan voorraad bijwerken in de bestaande regel. 
# Als naam en houdbaarheidsdatum niet gelijk aan elkaar zijn, dan nieuwe regel aanmaken)