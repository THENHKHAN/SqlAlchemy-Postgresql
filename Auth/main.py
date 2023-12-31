from typing import Union

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

from utils import validateToken
from models import User
from database import SessionLocal, init_db
from sqlalchemy.orm import Session

# Initialize the database tables when the application starts
init_db()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class RequestBody(BaseModel):
    token: str


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/google/signup/", status_code=201)
async def GoogleSignUp(body: RequestBody, db: Session = Depends(get_db)):
    access_token = body.token
    try:
        google_user_data = validateToken(access_token)
        user = User.create_user_without_pass(db=db, name=google_user_data.name, email=google_user_data.email, picture=google_user_data.picture)
        user = db.query(User).filter(User.id == 1).first()
        jwt_token = user.generate_token()

        return JSONResponse(status_code=201, content={"jwt_token" : jwt_token})
    except Exception as e:
    # By this way we can know about the type of error occurring
        print("The error is: ",e)
        return JSONResponse(status_code=404, content={"error" : "User cannot be created"})


@app.post("/google/signin/", status_code=200)
async def GoogleSignIn(body: RequestBody, db: Session = Depends(get_db)):
    access_token = body.token
    try:
        google_user_data = validateToken(access_token)
        user = db.query(User).filter(User.email == google_user_data.email).first()
        if user is None:
            return JSONResponse(status_code=404, content={"error" : "User not found"})
        jwt_token = user.generate_token()
        return JSONResponse(status_code=200, content={"jwt_token" : jwt_token})
    except Exception as e:
    # By this way we can know about the type of error occurring
        print("The error is: ",e)
        return JSONResponse(status_code=404, content={"error" : "Error while sign in"})


