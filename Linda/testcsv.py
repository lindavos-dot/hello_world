

import csv
import os

def check_document(path):
    check_file = os.path.isfile(os.path.join(path))

    if check_file == True:
        file = check_file

    elif check_file == False:
        with open(path, mode= 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            header = writer.writerow(['id', 'product', 'amount'])
            return header


# check_document('c:/Users/Linda Vos/Desktop/hello-world/Linda//test.csv')  # nakijken of het werkt

def test(path, product, amount):
    check_document(path)

    with open(path, mode= 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        return writer.writerow([id, product, amount])


# test('c:/Users/Linda Vos/Desktop/hello-world/Linda//test.csv','Apple', 4)
# test('c:/Users/Linda Vos/Desktop/hello-world/Linda//test.csv','Pear', 4)
# test('c:/Users/Linda Vos/Desktop/hello-world/Linda//test.csv','Plum', 4)

def inventory(filename): 

    with open(filename, mode= 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            print(row)



# inventory('test.csv')