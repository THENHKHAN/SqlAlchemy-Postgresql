from configDB import get_connection
from sqlalchemy import create_engine, Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

'''
Making Relation through FK, PK 
'''
engine = get_connection()  # created db connection
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer",
                            back_populates="invoices")  # one-to-many relationship where one customer can have multiple invoices.


Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")
Base.metadata.create_all(engine)
# Now when we create a Customer object, a blank invoice collection will be present in the form of Python List.
c1 = Customer(name = "Gopal Krishna", address = "Bank Street Hydarebad", email = "gk@gmail.com")
# The invoices attribute of c1.invoices will be an empty list. We can assign items in the list as −

c1.invoices = [Invoice(invno = 10, amount = 15000), Invoice(invno = 14, amount = 3850)]

session.add(c1)
session.commit()
session.close()
print("DONE")
# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_building_relationship.htm


'''
You can construct Customer object by providing mapped attribute of invoices in the constructor itself by using the below command −

c2 = [
   Customer(
      name = "Govind Pant", 
      address = "Gulmandi Aurangabad",
      email = "gpant@gmail.com",
      invoices = [Invoice(invno = 3, amount = 10000), 
      Invoice(invno = 4, amount = 5000)]
   )
]


Or a list of objects to be added using add_all() function of session object as shown below −

rows = [
   Customer(
      name = "Govind Kala", 
      address = "Gulmandi Aurangabad", 
      email = "kala@gmail.com", 
      invoices = [Invoice(invno = 7, amount = 12000), Invoice(invno = 8, amount = 18500)]),

   Customer(
      name = "Abdul Rahman", 
      address = "Rohtak", 
      email = "abdulr@gmail.com",
      invoices = [Invoice(invno = 9, amount = 15000), 
      Invoice(invno = 11, amount = 6000)
   ])
]

session.add_all(rows)
session.commit()
'''