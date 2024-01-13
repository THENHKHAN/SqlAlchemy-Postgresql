from models import db_session, Customer, Product

Customer2Instance = db_session.query(Customer).filter(Customer.id == 2).first()
ProdId3Instance = db_session.query(Product).filter(Product.id == 3).first() # wanted to deleted product whose id -3

Customer2Instance.product.remove(ProdId3Instance)
db_session.commit()
db_session.close()




ProdInstance = db_session.query(Product).all()
for prod in ProdInstance:
        print(f"  *************** prod -ID: {prod.id} ")
        print(f"Product's -name : {prod.name}")
        print(f"Product's -price : {prod.price}")
        print(f"Product's customer -LISTe : {prod.customer}") # prod.customer : like from customer to product retreible Customer had the LIST of PRODUCTS similary here Product would be LIST of Customer Associated with that prod.
        for cust in prod.customer:
              print(f"Product's customer -NAME : {cust.name}")


''''
2024-01-13 16:57:31,891 ********** Database connected successfully **************
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
Product's customer -LISTe : []  ************************************************ SEE here the customer is not here SICNE from prod -id 3 there is no custormer

'''