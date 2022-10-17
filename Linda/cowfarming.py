print('Enter your name:')
x_0 = input()
print('Hello, ' + x_0.title() + "!")

import time
x_2 = time.localtime()

if x_2.tm_hour < 6 or x_2.tm_hour > 18:
    x2 = ("night")
else:
    x2 = ("day")

print("Is the current weather rainy or sunny?")
x1 = input()
print("Ok, so the weather is " + x1)

print("How about the wind? Is it windy or neutral?")
x1a = input()
print("So " + x1a + " huh?" )

from datetime import datetime
  
today = datetime.now()
  
x5 = today.month

def season(x5):
    if (x5 == 12 or 1 <= x5 <= 4):
        return "winter"   
    elif (4 <= x5 <= 5):
        return "spring" 
    elif (6 <= x5 <= 9):
        return "summer"
    else:
        return "fall"
    
print("And it is "+ season(x5) +".")

import sys

def strtobool(val):

    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True

    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))

def prompt(query):
    sys.stdout.write("%s [y/n]: " % query)
    val = input()
    try:
        ret = strtobool(val)
    except ValueError:
        sys.stdout.write("Please answer with y/n")
        return prompt(query)
    return ret

while True:
    if prompt("Do the cows need milking?") == True:
        x3= True
        break
    else:
        x3 = False
        break

print("Are the cows in the cowshed or the pasture?")
x4 = input()
print ("Ok, so the cows are in " + x4)

print("Is the slurrytank full or empty?")
x6 = input()
print ("Ok, so, " + x6 + " , hence your the farmer")

print("Does the gras needs mowing? Please answer with yes, or no.")
x7 = input()

print ("Ok, gottcha," + x7)

def farm_action(
    x1,                             #weather
    x1a,                            #windy
    x2,                             #time_of_day
    x3,                             #cows_need_milking
    x4,                             #cows_location
    x5,                             #season
    x6,                             #slurry_tank_full
    x7,                             #grass_long
):

    actions = ""
    moved_cows = False

    if x2 == "night" and x1 == "rainy" and x4 != "cowshed":
        actions += "take cows to cowshed\n"
    elif x3:
        if x4 != "cowshed":
            actions += "take cows to cowshed\n"
            moved_cows = True
        actions += "milk cows\n"
        if moved_cows:
            actions += "take cows back to pasture\n"
    elif x6 and x1 != "sunny" and x1a != "windy":
        if x4 != "cowshed":
            actions += "take cows to cowshed\n"
            moved_cows = True
        actions += "fertilize pasture\n"
        if moved_cows:
            actions += "take cows back to pasture\n"
    elif x7 and x5 == "spring" and x1 == "sunny":
        if cows_location == "pasture":
            actions += "take cows to cowshed\n"
            moved_cows = True
        actions += "mow grass\n"
        if moved_cows:
            actions += "take cows back to pasture\n"
    else:
        actions += "wait\n"

    return actions[:-1]

print(farm_action(x1, x1a, x2, x3, x4, x5, x6, x7))