from models import User, Post, db_session
import logging

# lets 1st create user 

# user1 = User(
#     username="user1",
#     email="noor@gmail.com"
# )
# user2 = User(
#     username="user2",
#     email="noor2@gmail.com"
# )

# db_session.add(user2)
# db_session.commit()
# print(user2)
# logging.info("*** user created ***")


'''  Lets create post for only one user of id -1 '''

# 1st we need to get that user
user = db_session.query(User).filter(User.id==1).first() 

print(user)


# now lets create post by user1 only 
posts=[
    {
        "title":"Learn Django",
        "content":"Lorem ipsum1"
    },
      {
        "title":"Learn Java",
        "content":"Lorem ipsum2"
    },
      {
        "title":"Learn Javascript3",
        "content":"Lorem ipsum"
    },
      {
        "title":"Learn HTML",
        "content":"Lorem ipsum4"
    },
      {
        "title":"Learn css",
        "content":"Lorem ipsum5"
    },

]
# we'll have to insert one by one through loop

for post in posts:
    postData = Post(
        title=post["title"], 
        content=post["content"], 
        user_id=user.id
     )
    # now lets add
    db_session.add(postData)
    db_session.commit()


db_session.close()