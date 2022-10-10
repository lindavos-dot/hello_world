# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# The language spoken the most in Switzerland is the same as in Spain. 1
spain_language_most_spoken = "Castilian Spanish"
switzerland_language_most_spoken = "German"
print(spain_language_most_spoken == switzerland_language_most_spoken)

# The most prevalent religion in Switzerland is the same as in Spain. 2
spain_most_prevalent_religion = "Roman Catholic"
switzerland_most_prevalent_religion = "Roman Catholic"
print(spain_most_prevalent_religion == switzerland_most_prevalent_religion)

# The name length of Spain's capital does not equal that of Switzerland. 3
length_capital_spain = len("Madrid")
length_capital_switzerland = len("Bern")
print(length_capital_spain != length_capital_switzerland)

# Switzerland's GDP is greater than Spain's GDP. 4
gdp_spain = 1714860000000
gdp_switzerland = 590710000000
print(gdp_switzerland > gdp_spain)

# The population growth is less than 1% in Switzerland and Spain. 5
population_growth_spain = -0.03
population_growth_switzerland = 0.65
population_rate = 1
print(population_growth_switzerland and population_growth_spain < population_rate)

# At least one of the two countries has a population count of over 10 million. 6
population_count_spain = 47260584
population_count_switzerland = 8453550
population_count_over = 10000000
print(population_count_spain > population_count_over or population_count_switzerland > population_count_over)

# Exactly one of the two countries has a population count of over 10 million. 7 
if ((population_count_spain > population_count_over) and (population_count_switzerland < population_count_over)) or ((population_count_spain < population_count_over) and (population_count_switzerland > population_count_over)):
   Exactly_one_of_the_two_has_population_count_of_over_10_milion = True
else: Exactly_one_of_the_two_has_population_count_of_over_10_milion =  False

print(Exactly_one_of_the_two_has_population_count_of_over_10_milion)
 