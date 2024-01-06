from models import User, Comment
from connect import db_session

# updating COmmet table text from 'Hello World' to KAIZEN WORLD


commnetUpdate = db_session.query(Comment).filter(Comment.text =="Hello World").first()
print(f"Before updating commnetTxt : {commnetUpdate.text}")
if commnetUpdate is None:
    print("No record found")  
else:
        commnetUpdate.text = "KAIZEN WORLD"
        db_session.commit()
        print(f"After updating commnetTxt : {commnetUpdate.text}")


# #  updating name jona to NOOR

userNameUpdate = db_session.query(User).filter(User.username == 'jona').first()
print(f"Before updating userNameUpdate : {userNameUpdate.username}")
if userNameUpdate is None:
      print("No record found")
else:
      userNameUpdate.username = "NOOR"
      db_session.commit()
      print(f"AFTER updating userNameUpdate : {userNameUpdate.username}")

db_session.close()