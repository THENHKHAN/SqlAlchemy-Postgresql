from models import db_session, Post, User
import logging

# lets see all posts data 
post = db_session.query(Post).all()    
count = 1
for data in post :
    print (f"-----   POST --->  {count} ")
    print(f"posts_id : {data.id}")
    print(f"posts_user_idOrAuthorID : {data.user_id}")
    print(f"posts_author : {data.author}") # getting auther name 
    print(f"posts_title : {data.title}")
    print(f"posts_content : {data.content}")
    # Querying by back_populate concept
    print(f"posts_email : {data.author.email}") # extractng through relation as we know author is the attribute in Post class which is using to get User's attrubute.
    logging.info("********************")
    count += 1


logging.info("\n\n ****** Data from USer  *******\n")
# let get Post's data though User table
user = db_session.query(User).filter(User.id == 1).first()

print(f"User_id : {user.id}")
print(f"User_name : {user.username}")
print(f"User_email : {user.email}")
print(f"Post_2ndPostContent : {user.posts[1].content}")
print("\n\n")
#  gettign post of user1 of id-1 : Querying by back_populate concept
for post in user.posts : # user.posts list of posts of User of id-1 
    logging.info(f"-------  Post of ID-{post.id}   ------------")
    print("post.id", post.id)
    print("post.title", post.title)
    print("post.content", post.content)

   

db_session.close()

#  OUTPUT

'''
-----   POST --->  1 
posts_id : 1
posts_user_idOrAuthorID : 1
posts_author : <UserName:  user1>
posts_title : Learn Django
posts_content : Lorem ipsum1
posts_email : noor@gmail.com
2024-01-07 12:19:43,183 ********************
-----   POST --->  2
posts_id : 2
posts_user_idOrAuthorID : 1
posts_author : <UserName:  user1>
posts_title : Learn Java
posts_content : Lorem ipsum2
posts_email : noor@gmail.com
2024-01-07 12:19:43,183 ********************
-----   POST --->  3
posts_id : 3
posts_user_idOrAuthorID : 1
posts_author : <UserName:  user1>
posts_title : Learn Javascript3
posts_content : Lorem ipsum
posts_email : noor@gmail.com
2024-01-07 12:19:43,183 ********************
-----   POST --->  4
posts_id : 4
posts_user_idOrAuthorID : 1
posts_author : <UserName:  user1>
posts_title : Learn HTML
posts_content : Lorem ipsum4
posts_email : noor@gmail.com
2024-01-07 12:19:43,183 ********************
-----   POST --->  5
posts_id : 5
posts_user_idOrAuthorID : 1
posts_author : <UserName:  user1>
posts_title : Learn css
posts_content : Lorem ipsum5
posts_email : noor@gmail.com
2024-01-07 12:19:43,183 ********************
2024-01-07 12:19:43,183

 ****** Data from USer  *******

User_id : 1
User_name : user1
User_email : noor@gmail.com
Post_2ndPostContent : Lorem ipsum2



2024-01-07 12:19:43,183 -------  Post of ID-1   ------------
post.id 1
post.title Learn Django
post.content Lorem ipsum1
2024-01-07 12:19:43,183 -------  Post of ID-2   ------------
post.id 2
post.title Learn Java
post.content Lorem ipsum2
2024-01-07 12:19:43,183 -------  Post of ID-3   ------------
post.id 3
post.title Learn Javascript3
post.content Lorem ipsum
2024-01-07 12:19:43,183 -------  Post of ID-4   ------------
post.id 4
post.title Learn HTML
post.content Lorem ipsum4
2024-01-07 12:19:43,183 -------  Post of ID-5   ------------
post.id 5
post.title Learn css
post.content Lorem ipsum5

'''