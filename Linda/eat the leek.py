from cgi import print_arguments


list_of_films = ["Daddy-O", "I passed for White", "The Secret Ways", "Bachelor Flat", "Daimond Head", "Gidget Goed to Rome"]

def alphabetical_order(list):
    alphabetical_list = sorted(list)
    return alphabetical_list

print(sorted(list_of_films, key=str.lower))


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

x = ['Bob', 'Shaun', 'Preeti', 'Jeff']
for aap in x:


    print(f'Hello, {aap}!')


for i in range(900,1000,5):
    print(i)

a_list.append(i)

print(a_list)