from models import db, Ingredient, Restaurant, Dish, Rating
import peewee
import sqlite3


def data_test():
    db.connect()
    return db.create_tables([Ingredient, Restaurant, Dish, Rating])


def data_writer():
    db.connect()


    restaurants = [["Vilacidro", 1992, "16:00", "23:00"], ["Zaika", 2005, "14:00", "23:00"], ["MySnacks", 2005, "12:00", "23:00"]]

    dishes = [["Bambino pizza Maria", 1, 6000, "Tomaten"], ["Bambino pizza Italiana", 1, 6000, "Kaas"], ["Classic Burger", 2, 7500, "Rundvlees hamburger"], ["BBQ pulled chicken burger", 2, 9750, "Pulled Chicken"], ["Zak patat", 3, 4000, "Aardappel"], ["Franse Frietjes", 3, 2000, "Aardappel"]]

    ingredients = [["Tomaten", True, True, True], ["Kaas", True, False, False], ["Rosbief", False, False, True], ["Gorgonzola", True, False, False], ["Paprika", True, True, True], ["Artisjokken", True, True, True], ["Rundvlees hamburger", False, False, False], ["Sla", True, True, True], ["Rode ui", True, True, True], ["Augurk", True, True, True], ["Zaika Burgersaus", True, False, False], ["Pulled Chicken", False, False, False], ["Cheddar", True, False, False], ["Aardappel", True, True, True]] 

    ratings = [[1, 8, "Super!"], [1, 9, "Geweldig!"], [1, 10, "Top!"], [2, 6, "Moah"], [2, 5, "Oke"], [2, 6, "Moah"], [3, 2, "Booeee"], [3, 4, "Bleh"], [3, 5, "Bleh"]]

    for restaurant_name in restaurants:
        Restaurant.create(name = restaurant_name[0], open_since = restaurant_name[1], opening_time = restaurant_name[2], closing_time = restaurant_name[3])
    
    # for dish_name in dishes:
       # Dish.create(name = dish_name[0], served_at = dish_name[1], price_in_cents = dish_name[2], ingredients = dish_name[3])

    for ingredient_name in ingredients:
        Ingredient.create(name = ingredient_name[0], is_vegetarian = ingredient_name[1], is_vegan = ingredient_name[2], is_glutenfree = ingredient_name[3])
    
    for number in ratings:
        Ingredient.create(restaurant = number[0], rating = number[1], comment = number[2])
    