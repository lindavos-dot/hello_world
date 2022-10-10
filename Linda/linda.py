from asyncio import _leave_task
from tkinter import N


spain_most_spoken_language = "Castilian Spanish"
switserland_most_spoken_language = "German"
print(spain_most_spoken_language == switserland_most_spoken_language)

spain_most_prevalent_religion = "Roman Catholic"
switserland_most_prevalent_religion = "Roman Catholic"
print(switserland_most_prevalent_religion == spain_most_prevalent_religion)

capital_of_spain = "Madrid"
capital_of_switserland = "Zurich"
print(len(capital_of_switserland) != len(capital_of_spain))

gdp_of_spain = 1715*10**9
gdp_of_switserland = 590.71*10**9
print(gdp_of_switserland > gdp_of_spain)

population_growth_rate_switserland = 0.0065
population_growth_rate_spain = 0.0013
print(population_growth_rate_switserland < 0.01 and population_growth_rate_spain < 0.01)

ten_million= 10 ** 7

spain_population_count= 47.16 * 10 **6 
switserland_population_count = 8.5 * 10 ** 6
print(spain_population_count > ten_million or switserland_population_count > ten_million)

ten_million= 10 ** 7
spain_population_count= 47.16 * 10 **6 
switserland_population_count = 8.5 * 10 ** 6
print((spain_population_count > ten_million and switserland_population_count <= ten_million)
    or (switserland_population_count > ten_million and spain_population_count <= ten_million))
    


leek_price = 2 
print("Leek is " + str(leek_price) + " euro per kilo" )

order_1 = "leek 4"
number_1 = int(order_1[order_1.find(" "):])
sum_total1 = leek_price * number_1
print(sum_total1)

broccoli_price_per_kilo = 2.34 #euro
order_2 = "broccoli 1.6"
found_number_2 = float(order_2[order_2.find(" "):])
sum_total_2 = float(found_number_2) * float(broccoli_price_per_kilo)
print(sum_total_2)

print(str(found_number_2)+ "kg broccoli cost " + str(round(sum_total_2, 2)) + "e")  


#'1.6kg broccoli costs 500.34e'

