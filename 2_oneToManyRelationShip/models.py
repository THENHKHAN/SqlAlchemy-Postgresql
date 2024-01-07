
from sqlalchemy import (Integer, Column, String, ForeignKey)
from sqlalchemy.orm import relationship, sessionmaker
from dbConfig import Base, engine


"""
class User:
    id:int pk
    username:str
    email:str


class Post:
    id:int pk
    title:str
    content:str
    user_id:int foreignkey
"""

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username=Column(String(40),nullable=False)
    email=Column(String(40),nullable=True)

    posts=relationship("Post", back_populates='author', cascade="all , delete" ) # author will link to the Post table and but that will not reflect in table(unlike FK) when we see bcz its virtula just to link two or more tables.
#  they establish a bidirectional relationship between User and Post. Thats means we can we acess daat from User to Post as well as Post to User 

    def __repr__(self):
        return f"<UserName:  {self.username}>"
 
# ABOUT DeleteRecords in 1-M relationship
    # for  deleting in 1-M relationship : In parent -  posts=relationship("Post", back_populates='author') we have to use cascade. What this means is we are deleteing any user then All the post related to that User will be deleted as well.

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title=Column(String(45),nullable=False)
    content=Column(String(255),nullable=False)
    user_id=Column(Integer, ForeignKey('users.id') ) # FK 

    # relationship
    author=relationship("User", back_populates='posts')

    
    def __repr__(self):
        return f"<Post_Title: {self.title}>"


Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Use the session to add and commit the new user
db_session = SessionLocal()


