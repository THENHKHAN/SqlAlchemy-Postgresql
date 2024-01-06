from models import User, Comment
from connect import db_session


print("********* User table object  **********")
# get all users
rec = db_session.query(User).all()
for r in rec :
    print(r) # # it will return  username = jona   -- since we have two varibale in __str__() function

print("********* Comment table object  **********")
# get all comment
rec = db_session.query(Comment).all()
for r in rec :
    print(r) # # it will return  User = jona  comment = Hello World -- since we have two varibale in __str__() function

print("***** FILTER BY NAME ****** ")
r = db_session.query(User).filter(User.username=='jona').first()
print(r)

db_session.close()