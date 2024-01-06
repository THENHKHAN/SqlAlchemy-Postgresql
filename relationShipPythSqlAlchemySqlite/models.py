from connect import Base, db_session, engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,Text,String
from typing import List



# -------------  We can this synatx as well for SqlALchemy 2.0 ORM
# class MyTable(Base):
#     __tablename__ = 'myTable'
#     time_id = Column(DateTime, primary_key=True, default=datetime.utcnow)
#     customer_id = Column(String)
#     customer_name = Column(String)


# -------------  We can this synatx as well for SqlALchemy 2.0 ORM
class User(Base):
    __tablename__ = 'users'
   
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)
    email_address:Mapped[str] 
    
    # ONE-Many Relationship : One user can comment more that one times 
    comment: Mapped[List ["Comment"] ] =  relationship(back_populates="user")
    # comment: Mapped[List [Comment] ] =  relationship(back_populates="user") # in this case we have move below the Commnet class only then it will recognize the Comment class. So dont use this approach. Use the above one

    def __repr__(self) -> str:
        return f"User username={self.username} "


class Comment(Base):
    __tablename__ = 'comments'
   
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)
    text:Mapped[str] = mapped_column(String,nullable=False)
   
   
    user:Mapped["User"] =relationship(back_populates='comment') 
    # OR
    # user:Mapped["User"] =relationship("User", back_populates='comment')


    def __repr__(self) -> str:
        return f"User = {self.user.username}  comment = {self.text} , "


Base.metadata.create_all(bind=engine)