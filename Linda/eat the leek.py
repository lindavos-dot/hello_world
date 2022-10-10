from http.client import FOUND


leek_price = 2 
print("leek is " + str(leek_price) + " euro per kilo")

order_1 = "leek 4"
found_number_order_1= int(order_1[order_1.find(" "):]) 
print(found_number_order_1)

sum_total = found_number_order_1 * leek_price
print(sum_total)

broccoli_price = 2.34 #euro
order_2 = "broccoli 1.6"
number_2 = float(order_2[order_2.find(" "):])
total_pricing = float(broccoli_price) * float(number_2)
print(str(number_2) + " kg broccoli cost " + str(round(total_pricing,2)) + "e")
