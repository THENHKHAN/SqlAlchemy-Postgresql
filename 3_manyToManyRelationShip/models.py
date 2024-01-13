"""

table association:
    id : its own PK
    product_id: int fk(products.id)
    cutomer_id: int fk(customers.id)


class Customer:
    id : int pk
    name : str 


class Product:
    id : int pk
    name: str
    price : int
"""
#  without making class it wwill be the assicaite table: WARNING --> But its better to create a class based nt variable based table
# association_table=Table(
#     'association',
#     Base.metadata,
#     Column('customer_id',ForeignKey('customers.id')),
#     Column('product_id',ForeignKey('products.id'))

# )


from sqlalchemy import (ForeignKey, Column, String, Integer, Float)
from sqlalchemy.orm import relationship, sessionmaker

from dbConfig import Base, engine


#  Association table in which we'll have link both the table (Customer, Product) primary key.
class CustomerProduct(Base):
        __tablename__ = 'customer_product'

        id = Column(Integer, primary_key=True)

#  linking other related tables
        customer_id = Column(Integer, ForeignKey('customers.id')  )
        product_id = Column(Integer, ForeignKey('products.id' ) )


# Customer class  is equavalent to customers table in DB
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    product = relationship('Product', secondary='customer_product', back_populates='customer') # secondary='customer_product': customer_product will be linking to the associate table
# customer will have  list of prods
    def __repr__(self):
        return f"<Customer Name :  {self.name}>"


# Product class  is equavalent to products table in DB
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    customer = relationship('Customer', secondary='customer_product' , back_populates='product' )
    # Product will have  list of customer

    def __repr__(self):
         return f"<Product Name :  {self.name}>"

Base.metadata.create_all(engine) # it will make all the chnages in DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = SessionLocal() # this variable db_session will be used anywhere to query on DB by importing