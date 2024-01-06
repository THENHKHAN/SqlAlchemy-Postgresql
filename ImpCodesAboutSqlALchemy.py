connect.py ----------------------------------------------------------------------------------------------------------------


from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./my_blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, #connect_args={"check_same_thread": False}: is needed only for SQLite. It's not needed for other databases.
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # We need to have an independent database session/connection (SessionLocal) per request, use the same session through all the request and then close it after the request is finished.
                                        # And then a new session will be created for the next request.

Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()


# Create the database and tables
Base.metadata.create_all(bind=engine) #  line to create the database and tables. SO must be  ran after all table creation and before commit.




'''

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./my_blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, #connect_args={"check_same_thread": False}: is needed only for SQLite. It's not needed for other databases.
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # We need to have an independent database session/connection (SessionLocal) per request, use the same session through all the request and then close it after the request is finished.
                                        # And then a new session will be created for the next request.

Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()


# Define your models here, for example:
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True)

# Create the database and tables
Base.metadata.create_all(bind=engine) #  line to create the database and tables.

# Commit the changes
db_session.commit()

print("Database and tables created.")

user = User(username="Noor3", email="abc@gmail.com")

db_session.add(user)

# db_session.commit()
# db_session.refresh(user)

print("Data inserted.")
print(user.__table__.columns)
print(User.__table__.columns)
db_session.close

'''

#  From CMD or by  User.__table__ we can see the SCHEMA of TABLE. And User.__tablename__  attribute we can  see the table name. Her below User is the class name
'''
>>> from connect import User
Database and tables created.
Data inserted.
ReadOnlyColumnCollection(users.id, users.username, users.email)
ReadOnlyColumnCollection(users.id, users.username, users.email)
>>> User.__tablename__
'users'
>>> User.__table__     
Table('users', MetaData(), Column('id', Integer(), table=<users>, primary_key=True, nullable=False), Column('username', String(), table=<users>), Column('email', String(), table=<users>), schema=None)
>>>

'''



models.py   ----------------------------------------------------------------------------------------------------------------
# IN this how to create tabel and insert data / list of records 

from connect import Base , db_session
from sqlalchemy import create_engine,Column,Integer,String


# Define your models here, for example:
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True)

    def __str__(self):

        return f"UserName: {self.username} and EMAIL: {self.email}"


print("Database and tables created.")

users=[
    {
        "username":"jerry",
        "email":"jerry@company.com"
    },
     {
        "username":"jordan",
        "email":"jordan@company.com"
    }, {
        "username":"jackson",
        "email":"jackson@company.com"
    }, {
        "username":"jarden",
        "email":"j@company.com"
    }, {
        "username":"john",
        "email":"john@company.com"
    }, {
        "username":"jack",
        "email":"jack@company.com"
    },
]

# db_session.add(user)
# obj = db_session.query(User).all()
# db_session.commit()


#  hOW TO ADD LIST OF RECORDS:
for u in users:
    user = User(username = u["username"], email= u["email"])
    db_session.add(user)
    db_session.commit()

db_session.close
print("Data inserted.")
## Btter to make three or one file for initializing db , creating table and inserting data. Import file always run before the current file.
# https://www.youtube.com/watch?v=70mNRClYJko&list=PLEt8Tae2spYlxiF1scFTTIGG37TouiF2t&index=2

# [SqlAlchemy_OffDocs](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)