from configDB import get_connection
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from main import MyTable3

'''Question
get all data from table: MyTable3
get  data in order
get data by filter
count of results
'''

engine = get_connection()  # created db connection
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def getAllData(tableName):
    # data = session.query(tableName) # <class 'sqlalchemy.orm.query.Query'>
    data = session.query(tableName).all() # query object has all() method which returns a resultset in the form of list of objects.
    print(type(data))
    print(f"Table : {tableName.__tablename__}")
    print("id  name course age")
    for row in data:
        print(f"{row.id} ", end=" ")
        print(f"{row.name} ", end=" ")
        print(f"{row.course} ", end=" ")
        print(f"{row.age} ", end=" ")
        print()

# 2 : get  data in order
def getDataByOrder(tableName):
    print("order by Age and name \n Table", tableName.__tablename__)
    query = session.query(tableName).order_by( tableName.id.desc() ).all() # by default it will return in ascending But desc() then return in desc
    print("query type: ", type(query))
    print(query)
    print("id  name  age")
    for row in query:
        print(f"{row.id} ", end=" ")
        print(f"{row.name} ", end=" ")
        print(f"{row.age} ", end=" ")
        print()


def getDataByFilter(tableName):
    print(" filter record: id greater than or equal 2 \n Table", tableName.__tablename__)
    query = session.query(tableName).filter(tableName.id >=2 )
    print(f"query MAPPED  : {query}")
    print("id  name  age")
    for row in query:
        print(f"{row.id} ", end=" ")
        print(f"{row.name} ", end=" ")
        print(f"{row.age} ", end=" ")
        print()

getAllData(MyTable3)
print("******* Order by Of ABOVE  Asc/Dsc based on id ******* ")
getDataByOrder(MyTable3)
print("******* Records id>=2 ******* ")
getDataByFilter(MyTable3)

#  I/O:

'''
Session Closed DONE
<class 'list'>
Table : MyTable3                                                                                                                                                                        
id  name course age                                                                                                                                                                     
1  Noor  None  333                                                                                                                                                                      
2  Noor  MCA  333                                                                                                                                                                       
3  Noor2  MCA2  444                                                                                                                                                                     
4  Noor3  MCA3  666                                                                                                                                                                     
******* Order by Of ABOVE  Asc/Dsc based on id *******                                                                                                                                  
order by Age and name                                                                                                                                                                   
 Table MyTable3                                                                                                                                                                         
query type:  <class 'list'>                                                                                                                                                             
[<main.MyTable3 object at 0x000001FC2C996B60>, <main.MyTable3 object at 0x000001FC2C996BC0>, <main.MyTable3 object at 0x000001FC2C996AA0>, <main.MyTable3 object at 0x000001FC2C996A40>]
id  name  age                                                                                                                                                                           
4  Noor3  666                                                                                                                                                                           
3  Noor2  444                                                                                                                                                                           
2  Noor  333                                                                                                                                                                            
1  Noor  333                                                                                                                                                                            
******* Records id>=2 *******                                                                                                                                                           
 filter record: id greater than or equal 2                                                                                                                                              
 Table MyTable3                                                                                                                                                                         
query MAPPED  : SELECT "MyTable3".id AS "MyTable3_id", "MyTable3".name AS "MyTable3_name", "MyTable3".course AS "MyTable3_course", "MyTable3".age AS "MyTable3_age"                     
FROM "MyTable3"                                                                                                                                                                         
WHERE "MyTable3".id >= %(id_1)s                                                                                                                                                         
id  name  age                                                                                                                                                                           
2  Noor  333                                                                                                                                                                            
3  Noor2  444                                                                                                                                                                           
4  Noor3  666


'''