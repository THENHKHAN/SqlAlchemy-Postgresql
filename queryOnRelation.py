from sqlalchemy.orm import sessionmaker
from configDB import get_connection
from relationCreate import Customer, Invoice

engine = get_connection()  # created db connection
Session = sessionmaker(bind=engine)
session = Session()

print(f"Table1 : {Customer.__tablename__}")
print(f"Table2 : {Invoice.__tablename__}")

print("ID |  Name |         Invoice_No | Amount |")

for c, i in session.query(Customer, Invoice).filter(Customer.id == Invoice.custid).all():
    print(f"{c.id} ", end=" ")
    print(f"{c.name} ", end="    ")
    print(f"{i.invno} ", end=" ")
    print(f"{i.amount} ", end=" ")
    print()
# I/O:
'''
Table1 : customers
Table2 : invoices
ID |  Name |         Invoice_No | Amount |
1  Gopal Krishna     10  15000  
1  Gopal Krishna     14  3850  
'''