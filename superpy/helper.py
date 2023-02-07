# imports

from datetime import datetime
import os
import csv


# Hier staat de code om csv bestanden aan te maken en te bewerken

# WORKING WITH TIME MODULES

def today():
    current_time = datetime.now()
    required_format = datetime.strftime(current_time, '%Y-%m-%d')
    return required_format


# print(today())   nakijken of het werkt

# CHECK DOCUMENT and WRITE HEADER

def check_document(path):
    check_file = os.path.isfile(os.path.join(path))

    if check_file == True:
        file = check_file

    elif check_file == False:
        with open(path, mode= 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            header = writer.writerow(['id', 'mutation_date', 'product', 'amount', 'price', 'expiration_date'])
            return header


# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy//test.csv')  # nakijken of het werkt
# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy test2.csv')  # nakijken of het werkt

# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/inventory.csv')
# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/purchases.csv')
# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/sales.csv')
# check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/stock_in_trade.csv')


# WRITING A LINE TO THE DOCUMENT

def append_new_lines(path, id, product, amount, price, expiration_date):
    check_document(path)

    with open(path, mode= 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        mutation_date = today()
        return writer.writerow([id, mutation_date, product, amount, price, expiration_date])


# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy//test.csv', 'id', 'Apple', 4, 2, '2023-10-19')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy//test.csv', 'id', 'Banana', 4, 2, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy//test.csv', 'id', 'Pear', 4, 2, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy//test.csv', 'id', 'Mandarine', 4, 2, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy//test.csv', 'id', 'Kiwi', 4, 2, '2023-10-18')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy test2.csv', 'id', 'Apple', 4, 2, '2023-10-18')  # nakijken of het werkt

# DELETING A LINE FROM THE DOCUMENT

def delete_line(filename, product):
    with open(filename, mode= 'r') as read_file:
        csv_reader = csv.reader(read_file)
        list_of_csv = list(csv_reader)

        for row in list_of_csv:
            for word in row:
                if word == product:
                    list_of_csv.remove(row)
                  
    with open(filename, mode= 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(list_of_csv)


# delete_line('test.csv', 'Apple')