import psycopg2
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
# for postgreSQL database credentials can be written as
# Load environment variables from the .env file
""" i have setup working directory as sqlAlchemyCrud so it will load from that"""
load_dotenv()


def get_connection():
    # Access the password using the PASSWORD key
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    database = os.getenv("DATABASE")
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    # for creating connection string
    connectionStr = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connectionStr, echo=False)
    # Establish a connection: Using psycopg2 to connect with the PostgreSQL database.
    # conn = psycopg2.connect(connectionStr)
    print(" connection engine Object-> ", engine)
    return engine

if __name__ == '__main__':

    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        user = os.getenv("USER")
        host = os.getenv("HOST")
        engine = get_connection()
        print( f"Connection to the *** {host} *** for user *** {user} *** created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
