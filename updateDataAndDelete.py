from configDB import get_connection
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from main import MyTable3

'''Question
updata data
'''
engine = get_connection()  # created db connection
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def getAllData(tableName):
    query = session.query(tableName).all()
    print(type(query))
    print(f"Table : {tableName.__tablename__}")
    print("id  name course age")
    for row in query:
        print(f"{row.id} ", end=" ")
        print(f"{row.name} ", end=" ")
        print(f"{row.course} ", end=" ")
        print(f"{row.age} ", end=" ")
        print()


def updateData(tableName):
        singleRec = session.query(tableName).filter(tableName.id==2).first()
        print("id  name course age")
        print(f"{singleRec.id} ", end=" ")
        print(f"{singleRec.name} ", end=" ")
        print(f"{singleRec.course} ", end=" ")
        print(f"{singleRec.age} ", end=" ")

        # singleRec.name = "FARHAN"
        # session.commit()


def deleteDate(tableName):
    getDesiredRecord = session.query(tableName).filter(tableName.id == 4).first()
    print("id  name course age")
    print(f"{getDesiredRecord.id} ", end=" ")
    print(f"{getDesiredRecord.name} ", end=" ")
    print(f"{getDesiredRecord.course} ", end=" ")
    print(f"{getDesiredRecord.age} ", end=" ")

    # session.delete(getDesiredRecord)
    # session.commit()


print("\n ********* Before UPDATE **********")
getAllData(MyTable3)

print("\n ********* AFTER UPDATE of id =2  NAME from Noor to FARHAN **********")
updateData(MyTable3)

print("\n ********* DELETE WHose ID = 4 **********")
deleteDate(MyTable3)

# I/O:
'''
 ********* Before UPDATE **********
<class 'list'>
Table : MyTable3
id  name course age
1  Noor  None  333
2  Noor  MCA  333
3  Noor2  MCA2  444
4  Noor3  MCA3  666
 ********* AFTER UPDATE of id =2  NAME from Noor to FARHAN **********
id  name  age
4  Noor3  666
3  Noor2  444
2  FARHAN  333
1  Noor  333
******* Records id>=2 *******
 filter record: id greater than or equal 2
 Table MyTable3
query MAPPED  : SELECT "MyTable3".id AS "MyTable3_id", "MyTable3".name AS "MyTable3_name", "MyTable3".course AS "MyTable3_course", "MyTable3".age AS "MyTable3_age"
FROM "MyTable3"
WHERE "MyTable3".id >= %(id_1)s
id  name  age
3  Noor2  444
4  Noor3  666
2  FARHAN  333

'''

# DELETE

'''
                             
 ********* Before UPDATE **********
<class 'list'>
Table : MyTable3     
id  name course age  
1  Noor  None  333   
3  Noor2  MCA2  444  
2  FARHAN  MCA  333  

 ********* AFTER UPDATE of id =2  NAME from Noor to FARHAN **********
id  name course age
2  FARHAN  MCA  333
 ********* DELETE WHose ID = 4 **********
id  name course age
Traceback (most recent call last):
  File "E:updateDataAndDelete.py", line 58, in <module>
    deleteDate(MyTable3)
  File "E:updateDataAndDelete.py", line 42, in deleteDate
    print(f"{getDesiredRecord.id} ", end=" ")
AttributeError: 'NoneType' object has no attribute 'id'

SINCE DELETED
'''