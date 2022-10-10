# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# Write a function alphabetical_order that takes one argument: a list of strings that represent film names. 
# It returns a list of the same films in alphabetical order.

list_of_films = ["Daddy-O", "I passed for White", "The Secret Ways", "Bachelor Flat", "Daimond Head", "Gidget Goed to Rome"]

def alphabetical_order(list):
    alphabetical_list = sorted(list)
    return alphabetical_list

print(alphabetical_order(list_of_films))

# Write a function won_golden_globe that takes a film name and returns True or False based on whether or not this movie won a Golden Globe.
# Look into using the lower-function on the given film string.

def won_golden_globe(film_name):
    won_golden_globe = [
        "jaws",
        "e.t. the extra-terrestrial",
        "Star wars: episode iv - a new hope",
        "memoirs of a geisha",
    ]
    return film_name.lower() in won_golden_globe

print(won_golden_globe("Jaws"))
print(won_golden_globe("Jeff"))


# Write a function remove_toto_albums that takes a list of strings, removes Joseph's Toto albums from it and returns the tidy list. 

toto_albums = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "Old Is New"]
list_of_films.extend(toto_albums)

print(list_of_films)

def remove_toto_albums(list):
    for element in toto_albums:
        if element in list:
          list.remove(element)
    return list

remove_toto_albums(list_of_films)

print(list_of_films)