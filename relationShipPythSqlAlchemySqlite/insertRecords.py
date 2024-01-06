from connect import db_session
from models import User, Comment


user1 = User(
    username = 'jona',
    email_address = "jonathan@sql.irg",
    comment = [
         Comment(text="Hello World"),
         Comment(text="Please subscribe")
    ]
)

paul = User(
    username = 'paul',
    email_address = "paul@sql.irg",
    comment = [
         Comment(text="What's up?"),
         Comment(text="Please subscribe")
    ]
)


db_session.add_all([user1,paul])

db_session.commit()

db_session.close()
# Create the table


# Print the newly added user
print("new_user")