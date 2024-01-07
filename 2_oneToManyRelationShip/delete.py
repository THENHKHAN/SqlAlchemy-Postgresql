from models import Post, User, db_session
import logging
#  since i have post of user1 of id-1

#QUESTION::::  delete user of id=1 . It will delete user as well as all the post related to this user SINCE we have used CASCADE in User Class while creating relationship.



user_id_1 = db_session.query(User).filter(User.id==1).first()
# delete user of id=1 . It will delete user as well as all the post related to this user SINCE we have used CASCADE in User Class while creating relationship.



print(f"########################### Before Deleting all User's Data ###########################")
all_users = db_session.query(User).all()

for user in all_users:
    print(f"******* User of ID : {user.id} ******* ")
    user_data = {"user_id": user.id , "user_name" : user.username , "user_email": user.email}
    print(user_data)
    


print(f"########################### Before Deleting all Post's Data ###########################")
all_posts = db_session.query(Post).all()

for post in all_posts:
    print(f"******* Post of ID : {post.id} ******* ")
    posts_data = {"post_id": post.id , "post_author" : post.author.username , "post_title": post.title, "post_content": post.content}
    print(posts_data)




user_id_1 = db_session.query(User).filter(User.id==1).first()
# delete user of id=1 . It will delete user as well as all the post related to this user SINCE we have used CASCADE in User Class while creating relationship.


db_session.delete(user_id_1)
db_session.commit()



logging.info(f"########################### AFTERRRRRR Deleting , User's Data ###########################")
all_users = db_session.query(User).all()

for user in all_users:
    print(f"******* User of ID : {user.id} ******* ")
    user_data = {"user_id": user.id , "user_name" : user.username , "user_email": user.email}
    print(user_data)
    


logging.info(f"########################### AFTERRRRRR Deleting , Post's Data ###########################")
all_posts = db_session.query(Post).all()

for post in all_posts:
    print(f"******* Post of ID : {post.id} ******* ")
    posts_data = {"post_id": post.id , "post_author" : post.author.username , "post_title": post.title, "post_content": post.content}
    print(posts_data)


db_session.close()


#  INPUT/ OUTPUT::::

''''

2024-01-07 22:32:30,631 ********** Database connected successfully **************
########################### Before Deleting all User's Data ###########################
******* User of ID : 1 *******
{'user_id': 1, 'user_name': 'user1', 'user_email': 'noor@gmail.com'}
******* User of ID : 2 *******
{'user_id': 2, 'user_name': 'user2', 'user_email': 'noor2@gmail.com'}
########################### Before Deleting all Post's Data ###########################
******* Post of ID : 1 *******
{'post_id': 1, 'post_author': 'user1', 'post_title': 'Learn Django', 'post_content': 'Lorem ipsum1'}
******* Post of ID : 2 *******
{'post_id': 2, 'post_author': 'user1', 'post_title': 'Learn Java', 'post_content': 'Lorem ipsum2'}
******* Post of ID : 3 *******
{'post_id': 3, 'post_author': 'user1', 'post_title': 'Learn Javascript3', 'post_content': 'Lorem ipsum'}
******* Post of ID : 4 *******
{'post_id': 4, 'post_author': 'user1', 'post_title': 'Learn HTML', 'post_content': 'Lorem ipsum4'}
******* Post of ID : 5 *******
{'post_id': 5, 'post_author': 'user1', 'post_title': 'Learn css', 'post_content': 'Lorem ipsum5'}
2024-01-07 22:32:30,655 ########################### AFTERRRRRR Deleting , User's Data ###########################
******* User of ID : 2 *******
{'user_id': 2, 'user_name': 'user2', 'user_email': 'noor2@gmail.com'}
2024-01-07 22:32:30,657 ########################### AFTERRRRRR Deleting , Post's Data ###########################

NO DATA IN POST BCZ ALl DELETED RELATED TO USER-1
'''