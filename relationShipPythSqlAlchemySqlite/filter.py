from models import User, Comment
from connect import db_session


print("*************  Comment table Data    ******************** ")


comment = db_session.query(Comment).filter(Comment.text=="Please subscribe").first() # Comment table object
print(f"prinitng COmment instance : {comment}") # it will return  User = jona  comment = Hello World -- since we have two varibale in __str__() function
print(f"Comment_id : {comment.id}")
print(f"Comment_user_id : {comment.user_id}")
print(f"Comment_user : {comment.user}")
print(f"Comment_text : {comment.text}")
print(f"Comment_username: {comment.user.username}") # accesing username by comment table instance
print(f"Comment_email_address: {comment.user.email_address}") # accesing email_address by comment table instance


print("\n*************  User table Data    ******************** \n")
 
user = db_session.query(User).filter(User.email_address=="paul@sql.irg").first()# User table object
print(f"prinitng User instance : {user}") # it will return  User = jona  comment = Hello World -- since we have two varibale in __str__() function
print(f"User_id : {user.id}")
print(f"User_username : {user.username}")
print(f"User_email_address : {user.email_address}")
print(f"User_comment : {user.comment}") # list of comment by this user
print(f"User_comment[0] : {user.comment[0]}") # accesing oth index by comment table instance
print(f"User_comment[0].__tablename__ : {user.comment[0].__tablename__}") # getting table name thorugh user tabel
 
