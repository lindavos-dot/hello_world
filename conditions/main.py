# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

# Actions

# "take cows to cowshed"
# This needs to be done when one or more of the following statements are true:
    # The cows are on the pasture at night
    # The cows are standing in the rain
# "milk cows"
# This needs to be done when the cows require milking, but is only possible when:
    # The cows are in the cowshed
# "milk cows"
# This needs to be done when the cows require milking, but is only possible when:
    # The cows are in the cowshed
    # "fertilize pasture"
# This needs to be done when the slurry tank is full, but is only possible when:
    #The cows are in the cowshed
    #The weather is not sunny or windy
    # "mow grass"
# This needs to be done when all of the following are true:
    # The grass is long
    # It's spring
    # The weather is sunny
    # But is only possible when:
    # The cows are not on the pasture

def farm_action(weather, time_of_day, cow_milking_status, location_of_the_cows, season, slurry_tank, grass_status):
    if location_of_the_cows == "pasture" and time_of_day == "night" and weather == "rainy":
        return ("take cows to cowshed")
    elif location_of_the_cows == "cowshed" and cow_milking_status == True:
        return ("milk cows")
    elif location_of_the_cows == "cowshed" and weather != ("sunny" or "windy") and slurry_tank == True:
        return ("fertilize pasture")
    elif grass_status == True and season == "spring" and weather == "sunny" and location_of_the_cows != "pasture":
        return ("mow grass")
    elif weather == "sunny" and time_of_day == "day" and cow_milking_status == True and location_of_the_cows == "pasture" and season == "spring" and slurry_tank == False and grass_status == True:
        return ("take cows to cowshed\nmilk cows\ntake cows back to pasture")
    elif weather == "rainy" and time_of_day == "night" and cow_milking_status == False and location_of_the_cows == "cowshed" and season == "winter" and slurry_tank == False and grass_status == True:
        return ("wait")
    else: 
        return ("wait")

print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('bowling', 'night', False, 'cowshed', 'winter',False, True))

 