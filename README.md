# <h1 align="center"> Learning SqlAlchemy with PostgreSQL </h1>
### Tech Stacks:
- PostgreSQL
- Python
- SqlALchemy : [OfficialDocs](https://docs.sqlalchemy.org/en/14/orm/query.html)

## Features and Queries Practice :
### Queries: 
- how to `create table`
- `insert data`: single `record` as well list of `records`
- `getALlData`
- get data by `order by`
- `filter`
- `Update Data`
- `Delete Data`
- `Made Relationship` : Between Invoice and Customer table - checkout the `queryOnRElation` file, there is mention there as well.
- [LinkForRef](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_joins.htm)
- `join` in the relationShipPythSqlAlchemySqlite directory.



## Branch Distribution:
- **nk** : Basics crud operations done - `1st branch`. Using `PostgreSql`
- **relationship** : Here we have relations Learing among table - `2nd branch`. Using `Sqlite`
- **1-many** : In this branch we'll have `One-To-Many` relationship implemeted with User and Post
- **Many-To-Many-Relationship** : In this branch we'll have `Many-to-Many` Relationships 

## Important Links:

- [fastAPI Offcial Docs](https://fastapi.tiangolo.com/tutorial/sql-databases/#main-fastapi-app)
- [Article](https://hackersandslackers.com/sqlalchemy-data-models/): About Relationship through `SqlAlchemy`
- [YT-Lect](https://www.youtube.com/watch?v=XWtj4zLl_tg&list=PLEt8Tae2spYlxiF1scFTTIGG37TouiF2t&index=2) : By `Ssali Jonathan` SQLAlchemy 2.0 ORM - Talked about Sqlite with SqlAlchemy. Explained well about relationship and CRUD (By user and Comment table).
- [YT-1-TO-Many](https://www.youtube.com/watch?v=cc0xt9uuKQo&t=396s)
- [SqlAlchemy_OffDocs](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) : In this full Crud given But you need to look in more but btter for start 
- [article-About-Relationship-In-SqlALchemy](https://vegibit.com/sqlalchemy-orm-relationships-one-to-many-many-to-one-many-to-many/)
- [Article2](https://vegibit.com/sqlalchemy-orm-relationships-one-to-many-many-to-one-many-to-many/) : All type of relationShip explained very well.
-[Article3](https://www.digitalocean.com/community/tutorials/how-to-use-many-to-many-database-relationships-with-flask-sqlalchemy): Well explained with example and table also shwed.
- [YT_TheoryWithEx1](https://www.youtube.com/watch?v=TX2fhj8Xrj8&list=PL3R9-um41JsxPg4WAPeEZgH6oAk2oti0Q&index=3) : Mapping Cardinalities & Participation Constraints  by `Shanu Kuttan`
- [YT_TheoryWithEx2](https://www.youtube.com/watch?v=GiLpCYekYmw&list=PL3R9-um41JsxPg4WAPeEZgH6oAk2oti0Q&index=8) : Converting ER Diagrams to Tables (Theory with Question practice) . Y can watch other lecture as well for more.

## Creating Db using SqlALchemy with Sqlite and FastAPI
```python
## database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} #connect_args={"check_same_thread": False}: is needed only for SQLite. It's not needed for other databases.
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # We need to have an independent database session/connection (SessionLocal) per request, use the same session through all the request and then close it after the request is finished.
                                        # And then a new session will be created for the next request.

Base = declarative_base()


## MAIN.PY
from fastapi import Depends, FastAPI, HTTPException,Response
from fastapi.responses import JSONResponse
# importing desired dependecy from other files
from blog.database import SessionLocal, engine #blog.database we have to provide project directgory/ package (that's y init inside the blog directory)
from . import models
from .schemas import BlogPydantic
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine) # migrating all the changes. If table is not there then create a new one and if there then it wont  create 

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # here we are closing

@app.get("/" )
async def index ():
       return {"message": "Hello World!"}

@app.post("/blog/", status_code=201)
def creat_blog(request:BlogPydantic, db:Session = Depends(get_db)):
     try:
            new_blog = models.Blog(title = request.title , body = request.body)
            db.add(new_blog)
            db.commit()
            db.refresh(new_blog)
            return {"data" : {"info":"blog created successfully" , "title" : request.title , "body":request} }
     except Exception as e:
    # By this way we can know about the type of error occurring
        print("The error is: ",e)
        return {"status_code":404, "error":[ {"detail": "Blog not created"} , {"errorDetail" : f"The error is: {e}"} ] }
        # return JSONResponse(status_code=404, content= {"error" : "Blog cannot be created", "errorDetail" : f"The error is: {e}", }) also working

#Run server:(blog) E:\NHKHAN_studySelf\1-ColabsWithTHE_NHKHAN\BitFumesFastAPi>uvicorn blog.main:app 

```


## What are the main differences between sqlalchemy-ORM and slqalchemy-core?


SQLAlchemy provides two main components for interacting with databases: `SQLAlchemy ORM` (Object-Relational Mapping) and `SQLAlchemy Core`. Here's a brief overview of the main differences between them:

## 1- SQLAlchemy ORM:

**Object-Relational Mapping (ORM)**: SQLAlchemy ORM allows you to interact with a relational database using Python objects that are mapped to database tables. It provides a higher-level, more abstract interface that allows you to work with Python classes and objects instead of raw SQL queries.

**Declarative Base**: In SQLAlchemy ORM, you can define your database models using a `declarative syntax`, typically by inheriting from `declarative_base()`. This allows you to define your tables and relationships using Python classes and attributes.

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

**Relationships**: ORM provides a powerful way to define `relationships` between tables using attributes like relationship. These relationships are expressed in terms of Python objects and are more intuitive than manually joining tables in SQL. ORM allows you to define relationships between tables using the `relationship attribute`.

```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")

```

**Automatic SQL Generation**: ORM automatically generates SQL statements for CRUD operations based on your model definitions. This makes it easier to perform common database operations without writing raw SQL.


## 2- SQLAlchemy Core:

**SQL Expression Language:** SQLAlchemy Core is a lower-level interface that focuses on SQL expression language. It allows you to express SQL queries using Python constructs and provides a way to interact with databases using SQL expressions.

**Explicit SQL:** With Core, you have more control over the SQL statements you write. You can construct SQL queries explicitly using functions and constructs provided by SQLAlchemy, giving you fine-grained control over the generated SQL.

```python
from sqlalchemy import create_engine, select, text

engine = create_engine("sqlite:///:memory:")

with engine.connect() as connection:
    result = connection.execute(select([users.c.name, users.c.age]).where(text("age > 25")))

```

**Schema Definition:** In Core, you define your database schema using explicit constructs like Table and Column. This gives you direct control over the structure of your database tables.

```python
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
)

```

**Query API:** Core provides a query API that allows you to construct SQL queries using a fluent API. While it's not as high-level as the ORM for working with Python objects, it provides flexibility and control for more complex queries.

```python
from sqlalchemy import select

result = select([users.c.name, users.c.age]).where(users.c.age > 25)

```

## Choosing Between ORM and Core

- **Use ORM when**: You prefer working with Python objects, want automatic CRUD operations, and find relationships and high-level abstractions beneficial.

- **Use Core when**: You need more control over the SQL being generated, prefer to work with explicit SQL expressions, or need to perform complex queries.

