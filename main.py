from configDB import get_connection
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from datetime import datetime
# from sqlalchemy.ext import declarative_base # deprecated
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = get_connection()
print(engine)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class MyTable(Base):
    __tablename__ = 'myTable'
    time_id = Column(DateTime, primary_key=True, default=datetime.utcnow)
    customer_id = Column(String)
    customer_name = Column(String)


class MyTable2(Base):
    __tablename__ = 'MyTable2'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class MyTable3(Base):
    __tablename__ = 'MyTable3'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    course = Column(String(20))
    age = Column(Integer)


# Base.metadata.create_all(engine)

# Example: Adding a new record to the 'myTable' table
# new_record = MyTable(name='Noor', age='333')
# new_record = MyTable2(name='Noor', age='333')
# new_record = MyTable3(name='Noor', age='333', course="MCA")
# session.add(new_record)
new_record1 = MyTable3(name='Noor2', age='444', course="MCA2")
new_record2 = MyTable3(name='Noor3', age='666', course="MCA3")
new_record3 = MyTable3(name='Noor4', age='555', course="MCA4")

session.add_all([new_record1,new_record2,new_record3]) # to insert multiple records at once
session.commit()

# Close the session when done
session.close()
print("DONE")
# print(f"table {new_record.__tablename__} created successfully")
