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

## Creating Db using SqlALchemy 
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

# IMP:
'''
https://fastapi.tiangolo.com/tutorial/sql-databases/#main-fastapi-app : scroll for this - Create a dependency

'''

```
