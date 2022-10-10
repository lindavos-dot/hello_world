from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# shortest_names: takes a list of country names and returns a list of country names that have the shortest length. 

names = []

def shortest_names(countries):
    a = len(min(countries, key=len))
    for country in countries:
      if a == len(country):
        names.append(country)
    return names


# most_vowels: takes a list of country names and returns a list with the top three countries that have the most vowels in their name. 

name = []
vowels = "aeoui"

def most_vowels(countries):
  for country in countries:
      for letter in country:
        if letter.lower() in vowels:
            name.append(country)
  
  number_count = {}
  
  for country in name:
    if country in number_count:
      number_count[country] += 1
    else:
      number_count[country] = 1

  sorted_count = sorted(
      number_count.items(),
      key=lambda winning_countries: winning_countries[1],
      reverse = True
  )

  return sorted_count[0:3]


# alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. 

collection = []
alphabet = ["q", "w", "r", "t", "y" "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

def alphabet_set(countries):
    for country in countries:
      for letter in alphabet:
        if letter in country.lower():
          alphabet.remove(letter)          
          if country not in collection:
            collection.append(country)
    return collection, len(collection), len(alphabet)




# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`

if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """



print(shortest_names(get_countries()))
print(most_vowels(get_countries()))
print(alphabet_set(get_countries()))









