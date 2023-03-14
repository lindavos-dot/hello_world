# imports
from peewee import *
import peewee
import sqlite3


# Define DB
db = peewee.SqliteDatabase("betsy-webshop.db")


# Create Basemodel
class BaseModel(Model):
    class Meta:
        database = db


# Models go here. As a bonus requirement, you must consider the various constraints for all fields and incorporate these constraints in the data model. 
class User(BaseModel):  # A user has a name, address data, and billing information.
    # id = AutoField()
    username = CharField(unique=True, max_length=50)
    address = TextField(null=True)


class Billing(BaseModel):
    # id = AutoField()
    userid = ForeignKeyField(User)
    ideal = BooleanField()
    paypal = BooleanField()
    creditcard = BooleanField()
    klarna = BooleanField()


class Tag(BaseModel):
    # id = AutoField()
    tag = CharField(unique=True, max_length=50) # The tags should not be duplicated.


class Product(BaseModel): # The products must have a name, a description, a price per unit, and a quantity describing the amount in stock.
    # id = AutoField()
    productname = CharField()
    description = TextField()
    price = DecimalField(max_digits=6, decimal_places=2, auto_round=True) # The price should be stored in a safe way; rounding errors should be impossible.
    # max_digits has been added to prevent too large transactions going through Betsy, max now is: 9999,99
    quantity = IntegerField()
    owner = ForeignKeyField(User, backref='products') # Each user must be able to own a number of products.


class ProductTag(BaseModel):
    product = ForeignKeyField(Product)
    product_tag = ForeignKeyField(Tag)


class TrackTransaction(BaseModel): # The transaction model must link a buyer with a purchased product and a quantity of purchased items
     # id = AutoField()
    buyer = ForeignKeyField(User) # You can assume that only users can purchase goods
    product = ForeignKeyField(Product)
    quantity = IntegerField()


# Test data - To test if your database and queries are working we want to be able to populate the database with data quickly

def populate_test_database(): # Add a populate_test_database function that fills the database with example data that works with your queries
    db.connect()
    db.create_tables([User, Billing, Tag, Product, ProductTag, TrackTransaction])

    users = [['Linda', 'Streetname 1, City1'], ['Bob', 'Streetname 2, City2'], ['Matilda', 'Streetname 3, City3']]
    billing_methods = [[1, True, True, True, True], [2, True, True, True, True], [3, True, True, True, False], [4, True, True, True, False]]
    words_for_tag = ['sweater', 'jumper', 'jersey', 'pants', 'leggings', 'breeching', 'jacket', 'sack', 'cloak']
    products = [['sweater', 'fine wool sweater for the winter', 69, 50, 1], ['trouser', 'fine wool trouser for the winter', 89, 50, 2], ['coat', 'fine wool coat for the winter', 139, 50, 3]]
    product_tags = [[1, 1], [1, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]
    purchases = [[1, 2, 1], [2, 3, 1], [3, 1, 2]]

    for user in users:
        User.create(username = user[0], address = user[1])
    
    for payment in billing_methods:
        Billing.create(userid = payment[0], ideal = payment[1], paypal = payment[2], creditcard = payment[3], klarna = payment[4])
    
    for word in words_for_tag:
        Tag.create(tag = word)
    
    for products_to_sell in products:
        Product.create(productname = products_to_sell[0], description = products_to_sell[1], price = products_to_sell[2], quantity = products_to_sell[3], owner = products_to_sell[4])

    for word in product_tags:
        ProductTag.create(product = word[0], product_tag = word[1])
    
    for purchase in purchases:
        TrackTransaction.create(buyer = purchase[0], product = purchase[1], quantity = purchase[2])
    


