
# Many-to-Many Database Relationsip implenmented using SqlAlchemy 2.0
- Python : Python==3.10.5
- SqlLchemy: SQLAlchemy==2.0.24

## Important Info:
> **1-** Many-to-many relationships represent the relationship between two entities where multiple instances of one entity can be related to multiple instances of another entity. For example, multiple students can take multiple courses, and each course can be taken by multiple students. <br><br> **2-** In SQLAlchemy, many-to-many relationships are implemented using an intermediate table, also known as an association table, that maps the relationships between the two entities. The intermediate table contains foreign keys to both of the related tables and serves as a mapping between them. <br> Link: [RefArticle](https://vegibit.com/sqlalchemy-orm-relationships-one-to-many-many-to-one-many-to-many/)

# What i have done :

- Created Customer 
- Create Assign product to particluar product .
- Get  Product info Via Customer
- Get  Customer info Via Product
- How to `delete Product` from Customer profile: `It will reflect in the associative table`
- tables: Customer , Product and an Associative table that will contains Fks for Customer and Product stuffs

## Important Links:
- [forRef_YT](https://www.youtube.com/watch?v=3IDiEC0ZwPg)
- [Article1](https://www.digitalocean.com/community/tutorials/how-to-use-many-to-many-database-relationships-with-flask-sqlalchemy) : Well explained with example and table also showed.
- [Article2](https://hackersandslackers.com/sqlalchemy-data-models/)
- [Article3](https://vegibit.com/sqlalchemy-orm-relationships-one-to-many-many-to-one-many-to-many/)
- [Article4](https://www.educba.com/sqlalchemy-many-to-many/)
- YT_conceptualLearning : [YT_Conceptual](https://www.youtube.com/watch?v=TX2fhj8Xrj8&list=PL3R9-um41JsxPg4WAPeEZgH6oAk2oti0Q&index=3), [Converting ER Diagrams to Tables](https://www.youtube.com/watch?v=GiLpCYekYmw&list=PL3R9-um41JsxPg4WAPeEZgH6oAk2oti0Q&index=8)
