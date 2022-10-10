# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

#Part 1
# Create a variable leek_price with an integer value of 2.
# Cast this into a string and use the +-operator to print a string like this one, only with the correct price in it:

leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo.")

#Part 2
#We got an order for four leeks! Store the string 'leek 4' in a variable.
#Use find and slicing to extract the number from this string.
#Cast it into an integer.
#Use this and leek_price to compute the sum total and store it in sum_total. Print out the value for this variable.

order_1 = "leek 4"
number_1 = int(order_1[order_1.find(" "):])
sum_total = leek_price * number_1
print(sum_total)

#Part 3
#Broccoli costs 2.34 euros per kg. We got an order: 'broccoli 1.6'.
#Create one variable for the broccoli price and one for the order.
#Compute the total price for this order.
#Use the +-operator to assemble and print a string that looks like the following:
#'1.6kg broccoli costs 500.34e'

broccoli_price = 2.34
order_2 = "broccoli 1.6"
number_2 = float(order_2[order_2.find(" "):])
total_price = float(number_2) * float(broccoli_price)
print(str(number_2) + "kg broccoli costs " + str(round(total_price, 2)) + "e")

