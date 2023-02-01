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
    path = 'c:/Users/Linda Vos/Desktop/hello-world/superpy/4_stock.csv'
    isFile = os.path.isfile(path)

    if isFile == True:
        stock_file = isFile

    elif isFile == False:
        with open('4_stock.csv', mode= 'w') as stock_file:
            return stock_file


# check_document()

# Stap 2: De header toevoegen aan het document
def stock_writer_header():
    check_document()
    with open('4_stock.csv', mode= 'w', newline='') as stock_file:
        stock_writer = csv.writer(stock_file, delimiter=',')
        header = stock_writer.writerow(['id', 'category', 'name', 'amount', 'expiration_date'])
        return header


# stock_writer_header()

# Stap 3: Inventaris toevoegen aan het document - inkooplijst uitlezen in zijn geheel bij start van applicatie

def read_purchase_list():
    with open("2_bought.csv", mode= 'r') as file:
        csvreader = csv.reader(file)
        next(file)
        
        with open('4_stock.csv', mode= 'a', newline='') as stock_file:
            stock_writer = csv.writer(stock_file, delimiter=',')
                
            for row in csvreader:
                lines = row[0], row[2], row[3], row[4], row[6]
                # print(lines)
                stock_writer.writerow(lines)


# read_purchase_list()

# Een nachtrun, waarbij de voorraad wordt toegevoegd aan de hand van wat er vandaag is ingekocht:

def read_purchase_list_today():
    with open("2_bought.csv", mode= 'r') as file:
        csvreader = csv.reader(file)
        next(file)
        
        with open('4_stock.csv', mode= 'a', newline='') as stock_file:
            stock_writer = csv.writer(stock_file, delimiter=',')
                
            for row in csvreader:
                if row[1] == required_format:
                    lines = row[0], row[2], row[3], row[4], row[6]
                    # print(lines)
                    stock_writer.writerow(lines)


# read_purchase_list_today()

# Stap 4: Voorraad verwijderen uit de voorraadlijst als er verkoop heeft plaatsgevonden

current_stock = open("4_stock.csv", mode= 'r')
current_stock = ''.join([i for i in current_stock])
# print(current_stock)


sales_list = open("3_sold.csv", mode= 'r')
sales_list = ''.join([i for i in sales_list])
# print(sales_list)

    

def read_sales_list():
    

        
        with open('4_stock.csv', mode= 'r', newline='') as stock_file:
            stock_writer = csv.reader(stock_file, delimiter=',')
            next(stock_writer)
                
            for row in csvreader:
                lines = row[0], row[2], row[3], row[4], row[6]
                print(lines)

                for row in stock_writer:
                    data = row[3]
                    print(data)
                # stock_writer.writerow(lines)


# read_sales_list()