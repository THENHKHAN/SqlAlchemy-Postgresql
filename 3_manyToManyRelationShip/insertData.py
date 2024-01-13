from models import db_session, Customer, Product, CustomerProduct



#  INSERTED CUSTOMER DATA
# customer1=Customer(name="customer 1")
# customer2=Customer(name="customer 2")
# customer3=Customer(name="customer 3")
# db_session.add_all([customer1, customer2, customer3])
# db_session.commit()
# db_session.close()

#  lets insert some product since we have customers

customer2 = db_session.query(Customer).filter(Customer.id == 2).first() # getting customer 2 only since it's id is 2



product1=Product(name="Chicken",price=2000)
product2=Product(name="Bread",price=1000,)
product3=Product(name="Milk",price=500)

# lets add product by customer 2
# customer2.product.append(
#     product1
# )
#  it will bascally add the product with name and price in products table and customer2's id and Product's id to customer_product table with id 1: 1 2 1 --> (customer_product's id itself, customer_id, and product_id )

#  multiple  together
# customer2.product.extend(
#     [product2, product3]
# )

db_session.commit()
db_session.close()

''' THEABOVE : '''