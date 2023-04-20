# Imports
import argparse
import csv
from helper import *
from rich.console import Console
import pandas as pd
from csv2pdf import convert

def drop_line(product, expiration_date):
    path = get_path('current_stock.csv')
    with open(path, mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        listing = list(csv_reader)

        for row in listing:
            if row['product'] == product and row['expiration_date'] == expiration_date:
                listing.remove(row)

    header = ['id','mutation_date','product','amount','price','expiration_date']       
    with open(get_path('current_stock.csv'), mode= 'w', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader() 
        writer.writerows(listing) 
        




#drop_line('koek', '2023-10-23')




def buy(product, amount, price, expiration_date):
    product = product.lower()
    path = get_path('current_stock.csv')
    id = 'id'
    check_document(path)    
    
    #append_new_lines(get_path('purchases.csv'), id, product, amount, price, expiration_date)

    row = None              # UnboundLocalError: local variable 'row' referenced before assignment
    product_in_csv = False  # ter vervanging van != row['product'] omdat als de row['product'] wel gelijk is, maar row['expiration_date'] alsnog anders kan zijn
                            # en er misschien nog meer mogelijkheden zijn waar ik nu niet aan heb gedacht. Anders teveel if, elif, elif, elif

    with open(path, mode= 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row['product'] == product and row['expiration_date'] == expiration_date:
                               
                old_row = row
                new_row = row

                drop_line(old_row['product'], old_row['expiration_date'])
                current_amount = new_row['amount']               
                new_amount = int(current_amount) + int(amount)
                new_row['amount'] = new_amount
                
                append_new_lines(path, new_row['id'], new_row['product'], new_row['amount'], new_row['price'], new_row['expiration_date'])
                product_in_csv = True

        if product_in_csv is False:
            append_new_lines(path, id, product, amount, price, expiration_date)

        else:
            if row is None:
                append_new_lines(path, id, product, amount, price, expiration_date)                
             


#buy('Koek', 1, 2, '2023-10-13')
#buy('Koek', 1, 2, '2023-10-23')
#buy('Koek', 1, 2, '2023-10-22')




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


                old_row = {}
        new_row = {}

        for row in csv_reader:
            #print(row['product'])
            if row['product'] == product and row['expiration_date'] == expiration_date:
                               
                old_row = row
                new_row = row
                print(path, old_row['product'])
                deleteline(path, old_row['product'])
                
                current_amount = new_row['amount']               
                new_amount = int(current_amount) + int(amount)
                new_row['amount'] = new_amount
                
                print(path, new_row['id'], new_row['product'], new_row['amount'], new_row['price'], new_row['expiration_date'])
                append_new_lines(path, new_row['id'], new_row['product'], new_row['amount'], new_row['price'], new_row['expiration_date'])           
'''
        




