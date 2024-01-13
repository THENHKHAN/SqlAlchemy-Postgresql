from models import db_session, Customer, CustomerProduct, Product

customer2 = db_session.query(Customer).filter(Customer.id == 2).first()
print(customer2) # <Customer Name :  customer 2>
# now through  customer2 of  customer 2 instance we get all the infor about  customer 2 of id 2

print(f" customer 2 id : {customer2.id}")
print(f" customer 2 name : {customer2.name}")
print(f" customer 2 product Associated with : {customer2.product}") # [<Product Name :  Chicken>, <Product Name :  Bread>, <Product Name :  Milk>]
#  since customer will have  list of prods
 
customer2ProdHave = {prod.name : prod.price for prod in customer2.product} # tryinmg to get product witj price
print(customer2ProdHave) # {'Chicken': 2000.0, 'Bread': 1000.0, 'Milk': 500.0}


#  getting all proc=duct info associated with customer2
for prod in customer2.product: # prod will be Product imstance
    print(f"Customer product  *************** prod -ID: {prod.id} ")
    print(f"Customer -id : {customer2.id}")
    print(f"Customer -name : {customer2.name}")
    print(f"Customer's prod -id : {prod.id}")
    print(f"Customer's prod -name : {prod.name}")
    print(f"Customer's prod -price : {prod.price}")

print("\n\n\n")

#  let get all product info that whcih product is belog to which customer
ProdInstance = db_session.query(Product).all()
for prod in ProdInstance:
        print(f"  *************** prod -ID: {prod.id} ")
        print(f"Product's -name : {prod.name}")
        print(f"Product's -price : {prod.price}")
        print(f"Product's customer -LISTe : {prod.customer}") # prod.customer : like from customer to product retreible Customer had the LIST of PRODUCTS similary here Product would be LIST of Customer Associated with that prod.
        for cust in prod.customer:
              print(f"Product's customer -NAME : {cust.name}")



'''

2024-01-13 16:42:17,577 ********** Database connected successfully **************
<Customer Name :  customer 2>
 customer 2 id : 2
 customer 2 name : customer 2
 customer 2 product Associated with : [<Product Name :  Chicken>, <Product Name :  Bread>, <Product Name :  Milk>]
{'Chicken': 2000.0, 'Bread': 1000.0, 'Milk': 500.0}
Customer product  *************** prod -ID: 1
Customer -id : 2
Customer -name : customer 2
Customer's prod -id : 1
Customer's prod -name : Chicken
Customer's prod -price : 2000.0
Customer product  *************** prod -ID: 2
Customer -id : 2
Customer -name : customer 2
Customer's prod -id : 2
Customer's prod -name : Bread
Customer's prod -price : 1000.0
Customer product  *************** prod -ID: 3
Customer -id : 2
Customer -name : customer 2
Customer's prod -id : 3
Customer's prod -name : Milk
Customer's prod -price : 500.0




  *************** prod -ID: 1
Product's -name : Chicken
Product's -price : 2000.0
Product's customer -LISTe : [<Customer Name :  customer 2>]
Product's customer -NAME : customer 2
  *************** prod -ID: 2
Product's -name : Bread
Product's -price : 1000.0
Product's customer -LISTe : [<Customer Name :  customer 2>]
Product's customer -NAME : customer 2
  *************** prod -ID: 3
Product's -name : Milk
Product's -price : 500.0
Product's customer -LISTe : [<Customer Name :  customer 2>]
Product's customer -NAME : customer 2

''' 
