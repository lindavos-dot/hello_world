__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# imports
from models import *





def search(term):
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


def list_user_products(user_id):
    ...


def list_products_per_tag(tag_id):
    ...


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...




