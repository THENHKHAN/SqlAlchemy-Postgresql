from models import User, Comment
from connect import db_session

rec = db_session.query(Comment).filter(Comment.text=="What's up?").first()
if rec is None:
    print("No record found")  
else:
        db_session.delete(rec)
        db_session.commit()
        print("Successfully deleled")