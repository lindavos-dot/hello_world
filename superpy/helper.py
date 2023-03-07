# import
import datetime
import os
import csv

# Hier staat de (generieke)code om csv bestanden aan te maken en te bewerken

# WORKING WITH TIME MODULES
def get_today():
    return datetime.date.today()


#print(get_today())

def advance_time(number):
    today = get_today()
    days = datetime.timedelta(days= number)
    return(today + days)


#print(advance_time(2))


def backward_time(number):
    today = get_today()
    days = datetime.timedelta(days=number)
    return today - days


#print(backward_time(2))


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


# WRITING A LINE TO A DOCUMENT
def append_new_lines(path, id, product, amount, price, expiration_date):
    check_document(path)

    with open(path, mode= 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        mutation_date = get_today()
        return writer.writerow([id, mutation_date, product, amount, price, expiration_date])


# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy//test.csv', 'id', 'Apple', 4, 2, '2023-10-19')  # nakijken of het werkt
# append_new_lines('c:/Users/Linda Vos/Desktop/hello-world/superpy//test.csv', 'id', 'Banana', 4, 2, '2023-10-18')  # nakijken of het werkt


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


# delete_line('test.csv', 'Apple')


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
