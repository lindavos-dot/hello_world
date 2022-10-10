# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

# Part 1: Create Passport

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport_person = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport_person


my_passport = create_passport("Linda Vos", "1986-8-19", "Amsterdam", 1.80, "Netherlands")
# print(my_passport["name"])

# Part 2: Add Stamp

def add_stamp(passport, country):
    if "stamps" not in passport:
        passport["stamps"] = []
    
    if country not in passport["stamps"] and country != passport["nationality"]:
            passport["stamps"].append(country)
    return passport

    
add_stamp(my_passport, "Germany")
# print(my_passport)

add_stamp(my_passport, "Belgium")
# print(my_passport)

add_stamp(my_passport, "Netherlands")
# print(my_passport)

# Part 3: Add biometric data

def add_biometric_data(passport, name, value, date):
    if "biometric" not in passport:
        passport["biometric"] = {}
    
    description = {
            "value": value,
            "date": date,
        }
    passport["biometric"][name] = description
    return passport


add_biometric_data(my_passport, "hair", "in the summer her hair turns completely white", "2022-06-21")
add_biometric_data(my_passport, "skin", "in summer her skin turns light brown", "2022-06-21")
print(my_passport)

