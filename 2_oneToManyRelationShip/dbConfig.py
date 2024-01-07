from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import logging



SQLALCHEMY_DATABASE_URL = "sqlite:///./my_blog1ToN.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},
    echo=False# if True then in console all transacton will in the form of logger info 
)

Base = declarative_base()

# Create and configure logger
logging.basicConfig(
                    level=logging.INFO,  # Set the logging level to DEBUG
                    format='%(asctime)s %(message)s',
                    handlers=[
                        logging.StreamHandler()  # Console handler
                    ]
)
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
# logger.setLevel(logging.NOTSET)
logging.info("********** Database connected successfully **************")

