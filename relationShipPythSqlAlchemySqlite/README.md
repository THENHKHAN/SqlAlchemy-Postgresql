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

## Choosing Between ORM and Core

- **Use ORM when**: You prefer working with Python objects, want automatic CRUD operations, and find relationships and high-level abstractions beneficial.

- **Use Core when**: You need more control over the SQL being generated, prefer to work with explicit SQL expressions, or need to perform complex queries.
