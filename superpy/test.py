from helper import *

import csv



# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/test.csv', 'id', 'Apple', 4, 2, '2023-10-19')  # nakijken of het werkt

def test_buy(path, id, product, amount, price, expiration_date):
    check_document(path)    
    
    with open('test_current_stock.csv', mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader: 
            
            if row['product'] == product and row['expiration_date'] == expiration_date:
                    current_amount = int(row['amount'])
                    new_amount = current_amount + amount

                    text = open("test_current_stock.csv", mode= 'r')
                    text = ''.join([word for word in text]).replace(str(current_amount), str(new_amount))
                
                    updated_stock = open("test_current_stock.csv", mode= 'w')
                    updated_stock.writelines(text)

                    append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_purchases.csv', id, product, amount, price, expiration_date)
        
        else:
            append_new_lines(path, id, product, amount, price, expiration_date)
            append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_purchases.csv', id, product, amount, price, expiration_date)
    

# test_buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_current_stock.csv', 'id', 'Apple', 4, 2, '2023-10-19')
# test_buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/test.csv', 'id', 'Apple', 4, 2, '2023-10-18')
# test_buy('c:/Users/Linda Vos/Desktop/hello-world/superpy/test.csv', 'id', 'Pear', 4, 2, '2023-10-19')






def test_sell(path, id, product, amount, price, expiration_date):
    check_document(path)
    
    with open('test_current_stock.csv', mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            
            if row['product'] == product and row['expiration_date'] == expiration_date:
                current_amount = int(row['amount'])
                new_amount = current_amount - amount

                text = open("test_current_stock.csv", mode= 'r')
                text = ''.join([word for word in text]).replace(str(current_amount), str(new_amount))
                
                actual_stock = open("test_current_stock.csv", mode= 'w')
                actual_stock.writelines(text)
                actual_stock.close()

                append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_sales.csv', id, product, amount, price, expiration_date)

            else:
                print('This product is sold out')


# test_sell('c:/Users/Linda Vos/Desktop/hello-world/superpy/test_current_stock.csv', 'id', 'Apple', 1, 2, '2023-10-19')