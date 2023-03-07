import models
import peewee
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    # You want ot get food on a budget
    # Query the database to retrieve the cheapest dish available
    
    query = models.Dish.select().order_by(models.Dish.price_in_cents)
    return  query.first() #...


def vegetarian_dishes() -> List[models.Dish]:
    # You'd like to know what vegetarian dishes are available
    # Query the database to return a list of dishes that contain only vegetarian ingredients.
    
    query = models.Dish.select().where(models.Ingredient.select(models.Ingredient.is_vegetarian))
    

    
    return  query #...


def best_average_rating() -> models.Restaurant:
    
    # You want to know what restaurant is best
    # Query the database to retrieve the restaurant that has the highest rating on average
    query = models.Restaurant.select().join(models.Rating.rating)
    return  query.first() #...# ...

def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    # ...


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    #...


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    #...

# Model.select(), for executing SELECT queries.
# >>> query = Stat.update(counter=Stat.counter + 1).where(Stat.url == request.url)
# >>> query.execute()
#  Model.get() 

# For more advanced operations, you can use SelectBase.get(). The following query retrieves the latest tweet from the user named charlie:
""" >>> (Tweet
...  .select()
...  .join(User)
...  .where(User.username == 'charlie')
...  .order_by(Tweet.created_date.desc())
...  .get())
<__main__.Tweet object at 0x2623410>"""

# You can filter for particular records using normal python operators. Peewee supports a wide variety of query operators:
""" >>> user = User.get(User.username == 'Charlie')
>>> for tweet in Tweet.select().where(Tweet.user == user, Tweet.is_published == True):
...     print(tweet.user.username, '->', tweet.message)
...
Charlie -> hello world
Charlie -> this is fun

>>> for tweet in Tweet.select().where(Tweet.created_date < datetime.datetime(2011, 1, 1)):
...     print(tweet.message, tweet.created_date)
...
Really old tweet 2010-01-01 00:00:00 """

# https://docs.peewee-orm.com/en/latest/peewee/query_examples.html#query-examples
# https://docs.peewee-orm.com/en/latest/peewee/querying.html


