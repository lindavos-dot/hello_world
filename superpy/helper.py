# import
import os
import csv
from datetime import datetime, timedelta

# Hier staat de (generieke)code om csv bestanden aan te maken en te bewerken

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


# WORKING WITH TIME MODULES

def reset_today(): # datum terugzetten naar kalender datum
    today = datetime.today().strftime('%Y-%m-%d')
    with open('time.csv', mode= 'w') as file:
        file.write(today)


#reset_today()


def get_today():  # uitlezen welke datum is opgeslagen 
    with open('time.csv', mode= 'r') as file:
        reader = csv.reader(file)
        for date in reader:
            return date[0]


#print(get_today())

def get_today_object():  #tussenstap is nodig om herhaling van code te voorkomen in advance_time en backward_time, van string naar object voor timedelta (TypeError)
    today = get_today() 
    today_object = datetime.strptime(today, '%Y-%m-%d').date()
    return today_object


#print(get_today_object())

def advance_time(number): # datum vooruit zetten  
    days = timedelta(days= number)
    set_date = get_today_object() + days

    with open('time.csv', mode= 'w') as file:
        file.write(str(set_date))


#advance_time(2)
#print(get_today())


def backward_time(number): # datum achteruit zetten
    days = timedelta(days= number)
    set_date = get_today_object() - days

    with open('time.csv', mode= 'w') as file:
        file.write(str(set_date))


#backward_time(2)
#print(get_today())


# WRITING A LINE TO A DOCUMENT
def append_new_lines(path, id, product, amount, price, expiration_date):
    check_document(path)

    with open(path, mode= 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        mutation_date = get_today()
        writer.writerow([id, mutation_date, product, amount, price, expiration_date])


# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv', 'id', 'Plum', 4, 2, '2023-10-19')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv', 'id', 'Apple', 4, 2, '2023-10-18')  # nakijken of het werkt


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
        return writer.writerows(list_of_csv)


# delete_line('current_stock.csv', 'Plum')
# delete_line('sales.csv', 'Snoep')


# LATEN ZIEN DAT EEN PRODUCT NIET IS VERKOCHT, MAAR DE HOUDBAARHEIDSDATUM IS VERSTREKEN
def expiration_date_expired():
    check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/expiration_date_expired.csv')
    check_document('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv')
    
    filename = 'current_stock.csv'
    with open(filename, mode= 'r') as read_file:
        csv_reader = csv.DictReader(read_file)
        list_of_csv = list(csv_reader)
        expired_products = []
        
        date_today = get_today()
        for row in list_of_csv:
            date = row['expiration_date']
            if date <= date_today:
                list_of_csv.remove(row)
                expired_products.append(row)
    
    
    header = ['id','mutation_date','product','amount','price','expiration_date']       
    with open('current_stock.csv', mode= 'w', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader() 
        
        for data in list_of_csv:
            writer.writerow(data) 
    
    header = ['id','mutation_date','product','amount','price','expiration_date']   
    with open('expiration_date_expired.csv', mode= 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        # writer.writeheader() 
        
        for data in expired_products:
            return writer.writerow(data)  


# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy/current_stock.csv', 'id', 'Apple', 4, 2, '2022-10-19')  # toevoegen over datum appels
# expiration_date_expired()
