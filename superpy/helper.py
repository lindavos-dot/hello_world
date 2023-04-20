# import
import os
import csv
from datetime import datetime, timedelta

# Hier staat de (generieke)code om csv bestanden aan te maken en te bewerken

'''
SETUP HELPER
'''

# Setting up a working directory: option to create a folder, absolute paths and checking on files 
# create_working_directory('superpy')

def create_working_directory(foldername): # set up folder where csv files are stored
    directory = os.path.join(os.getcwd(), foldername)
    return os.mkdir(directory)


def get_path(filename): # function helper
    path = os.path.abspath(os.path.join(os.getcwd(), filename))
    return path


# Check document and write header
def check_document(filename):
    path = get_path(filename)
    check_file = os.path.isfile(os.path.join(path))

    if check_file == True:
        filename = check_file

    elif check_file == False:
        with open(path, mode= 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            header = writer.writerow(['id', 'mutation_date', 'product', 'amount', 'price', 'expiration_date'])
            return header


'''
WORKING WITH TIME MODULES
'''

def reset_today(): # datum terugzetten naar kalender datum
    path = get_path('time.csv') 
    today = datetime.today().strftime('%Y-%m-%d')
    with open(path, mode= 'w') as file:
        file.write(str(today))


def get_today():  # uitlezen welke datum is opgeslagen 
    path = get_path('time.csv') 
    with open(path, mode= 'r') as file:
        reader = csv.reader(file)
        for date in reader:
            return date[0]


def get_today_object():  #tussenstap is nodig om herhaling van code te voorkomen in advance_time en backward_time, van string naar object voor timedelta (TypeError)
    today = get_today() 
    today_object = datetime.strptime(today, '%Y-%m-%d').date()
    return today_object


def advance_time(number): # datum vooruit zetten  
    days = timedelta(days= number)
    set_date = get_today_object() + days
    path = get_path('time.csv') 
    with open(path, mode= 'w') as file:
        file.write(str(set_date))


def backward_time(number): # datum achteruit zetten
    days = timedelta(days= number)
    set_date = get_today_object() - days
    path = get_path('time.csv') 
    with open(path, mode= 'w') as file:
        file.write(str(set_date))


'''
MAIN.PY FUNCTION HELPERS
'''

def append_new_lines(filename, id, product, amount, price, expiration_date): # Writing a line to a document
    check_document(filename)

    with open(get_path(filename), mode= 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        mutation_date = get_today()
        writer.writerow([id, mutation_date, product.lower(), amount, price, expiration_date])


def delete_line(filename, product): # Deleting a line from a document
    product = product.lower()
    with open(get_path(filename), mode= 'r') as read_file:
        csv_reader = csv.reader(read_file)
        list_of_csv = list(csv_reader)

        for row in list_of_csv:
            for word in row:
                if word == product:
                    list_of_csv.remove(row)
                  
    with open(get_path(filename), mode= 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        return writer.writerows(list_of_csv)


# Helper functie voor buy and sell functie (target: product & expiration_date)
def drop_line(filename, product, expiration_date):

    with open(get_path(filename), mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        lists = list(csv_reader)

        for row in lists:
            if row['product'] == product and row['expiration_date'] == expiration_date:
                lists.remove(row)

    header = ['id','mutation_date','product','amount','price','expiration_date']       
    with open(get_path(filename), mode= 'w', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader() 
        writer.writerows(lists) 


# LATEN ZIEN DAT EEN PRODUCT NIET IS VERKOCHT, MAAR DE HOUDBAARHEIDSDATUM IS VERSTREKEN
def expiration_date_expired():
    check_document('expiration_date_expired.csv')
    check_document('current_stock.csv')
    
    with open(get_path('current_stock.csv'), mode= 'r') as read_file:
        csv_reader = csv.DictReader(read_file)
        list_of_csv = list(csv_reader)
        expired_products = []
        
        date_today = reset_today()
        for row in list_of_csv:
            date = row['expiration_date']
            if date <= str(date_today):
                list_of_csv.remove(row)
                expired_products.append(row)
    
    
    header = ['id','mutation_date','product','amount','price','expiration_date']       
    with open(get_path('current_stock.csv'), mode= 'w', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader() 
        
        for data in list_of_csv:
            writer.writerow(data) 
    
    header = ['id','mutation_date','product','amount','price','expiration_date']   
    with open(get_path('expiration_date_expired.csv'), mode= 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        # writer.writeheader() 
        
        for data in expired_products:
            return writer.writerow(data)  


#append_new_lines('current_stock.csv', 'id', 'Banana', 4, 2, '2022-10-19')  # toevoegen over datum appels
#expiration_date_expired()
