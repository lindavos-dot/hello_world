# Imports
import argparse
import csv
from helper import *
from rich.console import Console
import pandas as pd
from csv2pdf import convert




def buy(product, amount, price, expiration_date):
    product = product.lower()
    path = get_path('current_stock.csv')
    id = 'id'
    check_document(path)    
    
    #append_new_lines(get_path('purchases.csv'), id, product, amount, price, expiration_date)

    row = None
    product_in_csv = False # toegevoegd ter vervanging van != row['product'] omdat als de row['product'] wel gelijk is, maar row['expiration_date'] alsnog anders kan zijn
    # en er nog meer mogelijkheden zijn waar ik nu niet aan heb gedacht

    with open(path, mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        
        old_row = {}
        new_row = {}

        for row in csv_reader:
            #print(row['product'])
            if row['product'] == product and row['expiration_date'] == expiration_date:
                               
                old_row = row
                new_row = row

                delete_line(path, old_row['product'])
                current_amount = new_row['amount']               
                new_amount = int(current_amount) + int(amount)
                new_row['amount'] = new_amount
                
                append_new_lines(path, new_row['id'], new_row['product'], new_row['amount'], new_row['price'], new_row['expiration_date'])
                product_in_csv = True

        if product_in_csv is False:
            append_new_lines(path, id, product, amount, price, expiration_date)

        else:
            if row is None:
                #print("d")
                append_new_lines(path, id, product, amount, price, expiration_date)                


buy('Kaas', 1, 2, '2023-10-17')




'''
a = []
row = None
for row in a:
    print("hallo")
else:
    if row is None:
        print("joehoe")  

row = None
path = get_path('current_stock.csv')
with open(path, mode= 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(row['product'])                
'''
        




