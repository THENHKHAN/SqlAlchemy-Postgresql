import os
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from passlib.hash import bcrypt
from utils import generate_random_password
from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv

load_dotenv()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    name = Column(String)
    picture = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
        
    @classmethod
    def create_user_without_pass(cls, db, email: str, name:str, picture:str):
        print(name, email, picture)
        random_password = generate_random_password()  
        # Hash the password using bcrypt
        hashed_password = bcrypt.hash(random_password)
        # Create a new user
        user = cls(email=email, hashed_password=hashed_password, name=name, picture=picture)

        # Save the user to the database
        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    def generate_token(self, algorithm: str = "HS256", expires_in_minutes: int = 36000):
        # Get the secret key from the environment
        secret_key = os.getenv("SECRET_KEY")
        if secret_key is None:
            raise ValueError("SECRET_KEY not found in environment variables")

        # Prepare the payload
        payload = {
            "sub": str(self.id),
            "name": self.name,
            "email": self.email,
            "exp": datetime.utcnow() + timedelta(minutes=expires_in_minutes),
        }

        # Generate the token using PyJWT
        token = jwt.encode(payload, secret_key, algorithm=algorithm)

        return token.decode('utf-8')
