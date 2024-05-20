# One To Many Relationsip implenmented using SqlAlchemy 2.0
- Python : Python==3.10.5
- SqlLchemy: SQLAlchemy==2.0.24


## Important Info:
> **One To Many** : </br> A one to many relationship places a `foreign key on the child table` referencing the parent. `relationship() is then specified on the parent`, as referencing a collection of items represented by the child:


> **What does the Session do ?** <br></br>**1.** In the most general sense, the Session `establishes all conversations with the database and represents a “holding zone” for all the objects which you’ve loaded or associated with it during its lifespan`. It provides the interface where SELECT and other queries are made that will return and modify ORM-mapped objects. The ORM objects themselves are maintained inside the Session, inside a structure called the identity map - a data structure that maintains unique copies of each object, where “unique” means “only one object with a particular primary key”. </br> </br> **2.** The Session in its most common pattern of use begins in a mostly stateless form. Once queries are issued or other objects are persisted with it, it requests a connection resource from an `Engine` that is associated with the Session, and then establishes a `transaction on that connection`. This transaction remains in effect until the Session is instructed to commit or roll back the transaction. When the transaction ends, the connection resource associated with the Engine is released to the connection pool managed by the engine. A new transaction then starts with a new connection checkout.

## What we have done:
- Made two **tables** `User` and `Post` : Designed relationship as well. 
- **Created** User and Post. For learning purpose, Designed post only for user-1 so that we can undertand how to deleted and insert and use of `FK`.
- **Inserted** User and Post(through user-1) data :  `insertData.py File` .
- **Retrieved** Data : All shown in `retreiveData.py File` - `pasted console's output`.
- **Deletd** Data : All shown in `delete.py File` - pasted console's output AS well as ScreenShot Of UI TAble and console's output (Before and After deleting).

## Important Links:

- [YT-1-TO-Many](https://www.youtube.com/watch?v=cc0xt9uuKQo&t=396s):SQLAlchemy 2.0 ORM - with Sqlite -YT
- [OffDoc1ToMany](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)
- [Article](https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy)
