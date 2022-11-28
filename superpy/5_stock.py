# voorraad document aanmaken, van waaruit ook de sold en over datum artikelen vanuit worden gehaald (?)
# indeling: id, category, naam product, aantal op voorraad, houdbaarheidsdatum, 

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
    path = 'c:/Users/Linda Vos/Desktop/hello-world/superpy/stock.csv'
    isFile = os.path.isfile(path)

    if isFile == True:
        inventory_file = isFile

    elif isFile == False:
        with open('stock.csv', mode= 'w') as inventory_file:
            return inventory_file


# check_document()

# Stap 2: De header toevoegen aan het document
def stock_writer_header():
    check_document()
    with open('stock.csv', mode= 'w', newline='') as stock_file:
        stock_writer = csv.writer(stock_file, delimiter=',')
        header = stock_writer.writerow(['id', 'category', 'name', 'amount', 'price', 'expiration_date'])
        return header


# stock_writer_header()

# Stap 3: Inventaris toevoegen aan het document
  
def stock_writer(id, category, name, amount, price, expiration_date):
    check_document() 
    
    with open('stock.csv', mode= 'a', newline='') as stock_file:
        stock_writer = csv.writer(stock_file, delimiter=',')
            
        return stock_writer.writerow([id, category, name, amount, price, expiration_date])


# stock_writer('id', 'Fruit', 'Orange', 16, 1.30, '2023-10-15')
# stock_writer('id', 'Fruit', 'Apple', 16, 1, '2023-10-15')


# stock_writer with Argparse
parser = argparse.ArgumentParser(description='Enter new stock')

parser.add_argument('--name', type=str, help='Enter a name')
parser.add_argument('--amount', type=int, help='Enter an amount')
parser.add_argument('--price', type=float or int, help='Enter a price')
parser.add_argument('--action', type=str, help='Enter an action')

args = parser.parse_args()

if args.action == 'buy': 
    with open('stock.csv', mode= 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for word in row:
                if word == args.name:
                    current_amount = int(row[3])
                    new_amount = current_amount - args.amount
                    # print(new_amount)
                    text = open("stock.csv", mode= 'r')
                    text = ''.join([i for i in text]).replace(str(current_amount), str(new_amount))
                    actual_stock = open("stock.csv", mode= 'w')
                    actual_stock.writelines(text)
                    actual_stock.close()


# python 5_stock.py --name Apple --amount 2 --price 1.40 --action buy