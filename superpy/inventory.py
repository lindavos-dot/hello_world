

# First step? How do i want to structure data?

# inventory (inventaris)
# stock (voorraad, met datum?)
# bought (inkoop met naam, prijs, aantal, houdbaarheidsdatum)
# sold (verkoop met naam, prijs, aantal, houdbaarheidsdatum of als de houdbaarheidsdatum is vervallen. Het feit dat dit is gebeurt)
# past_expiration_date (artikelen die over datum zijn gegaan en uit de voorraad lijst worden gehaald, worden hier opgeslagen)

# Beginnen met inventory. Hoe maak ik een csv file? Hoe maak ik een header?

import csv

with open('inventory.csv', mode= 'w') as inventory_file:
    inventory_writer = csv.writer(inventory_file, delimiter=',')

    inventory_writer.writerow(['id', 'name'])
    inventory_writer.writerow(['id', 'Orange'])
    inventory_writer.writerow(['id', 'Apple'])
    inventory_writer.writerow(['id', 'Pear'])
    inventory_writer.writerow(['id', 'Bread'])
    inventory_writer.writerow(['id', 'Cheese'])
    inventory_writer.writerow(['id', 'marmalade'])


    