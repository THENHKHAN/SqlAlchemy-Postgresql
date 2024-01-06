# We need to use select Function of sqlAlchemy.
# To join these two tables using SQLAlchemy Core, developers can use the join() function.

from models import User, Comment
from connect import db_session
from sqlalchemy import select


# Perform a join query to retrieve data from multiple tables 

stmt = select(Comment.id, Comment.text, Comment.user_id, User.username, User.id, User.email_address).select_from( 
    Comment).join(User, Comment.user_id== User.id) # it will show only those user who have commentted

results = db_session.execute(stmt) 
  
print ("Comment_id|Comment.text|Comment.user_id|User.username| User.id|email_address")
for row in results: 
    print((row)) 
  
db_session.close() 

'''
Comment_id|Comment.text|Comment.user_id|User.username| User.id|email_address
(1, 'Hello World', 1, 'jona', 1, 'jonathan@sql.irg')
(2, 'Please subscribe', 1, 'jona', 1, 'jonathan@sql.irg')
(3, "What's up?", 2, 'paul', 2, 'paul@sql.irg')
(4, 'Please subscribe', 2, 'paul', 2, 'paul@sql.irg')
'''

# we have 5 comment but in 5th comment the user id of 4 was not had any user(I know its not conceptually right for showing JOIN is working fine). 
# 5th commnet was this : id-5, text-'checkkkkk', user_id-4 but in user table there was only two user paul of id 2 and jona with id-1