__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# imports
from models import *
import peewee

def search(term): # Search for products based on a term. The search should target both the name and description fields.
    term = term.lower()
    query = (Product
            .select()
            .join(ProductTag)
            .join(Tag)
            .where(Product.productname.contains(term) | Product.description.contains(term) | ProductTag.product_tag.contains(term) | Tag.tag.contains(term)))
    
    search_results = []
    
    for product in query:      
       
        if product.productname not in search_results:
            search_results.append(product.productname)
        
    return search_results


# print(search('jumper')) # testen tags
# print(search('wool')) # testen description
# print(search('sweater')) # testen product naam


def list_user_products(user_id): # View the products of a given user.
    query = Product.select().join(User).where(User.id == user_id)

    search_results = []
    
    for product in query:      
       
        if product.productname not in search_results:
            search_results.append(product.productname)
        
    return search_results


# print(list_user_products(1)) # sweater
# print(list_user_products(2)) # trouser
# print(list_user_products(3)) # coat


def list_products_per_tag(tag_id): # View all products for a given tag.
    query = Product.select().join(ProductTag).join(Tag).where(Tag.id == tag_id)

    for products in query:
        return products.productname


# print(list_products_per_tag(1)) # sweater
# print(list_products_per_tag(4)) # trouser
# print(list_products_per_tag(7)) # coat


def add_product_to_catalog(product_name, product_description, product_price, product_quantity, user_id): # Add a product to a user.
    add_product = Product.create(
        productname = product_name, 
        description = product_description, 
        price = product_price, quantity = product_quantity, 
        owner = user_id
        )
    return add_product


# add_product_to_catalog('t-shirt', 'cotton t-shirt', 15, 50, 1)
# print(list_user_products(1)) # ['sweater', 't-shirt']


def add_tags_to_products(product_id, tag):
    add_tags = ProductTag.create(product = product_id, product_tag = tag)
    return add_tags


# add_tags_to_products(4, 3)


def update_stock(product_id, new_quantity): # Update the stock quantity of a product.
    query = Product.update(quantity = new_quantity).where(Product.id == product_id)
    return query.execute()


# update_stock(4, 40) # van 50 stuks naar 40 stuks


def purchase_product(product_id, buyer_id, sold_quantity): # Handle a purchase between a buyer and a seller for a given product
    # add new transactions
    add_transaction = TrackTransaction.create(buyer = buyer_id, product = product_id, quantity = sold_quantity)
    
    # update current quantity
    query_current_stock = Product.select().where(Product.id == product_id)
    
    for amount in query_current_stock:
        current_stock = amount.quantity
    
    sum_updated_stock = current_stock - sold_quantity
    return add_transaction, update_stock(product_id, sum_updated_stock)


# purchase_product(1, 2, 2)


def remove_product(product_id): # Remove a product from a user.
    query = Product.select().where(Product.id == product_id)

    for product in query:
        return product.delete_instance()


# remove_product(5)


