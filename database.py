# The foundation file - connects python code to database
from sqlalchemy import create_engine #a function that creates the connection
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker #a function that produces database session on demand

DATABASE_URL = 'sqlite:///./grades.db' # This string tells sqlalchemy where exactly our database lives './' exists in same folder

# The engine is the actual connection to the database. It uses URL to know where to connect
engine = create_engine(DATABASE_URL,connect_args={'check_same_thread':False})

# SessionLocal is a blueprint for creating session
SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

#Base is the parent class for all our DB models
Base = declarative_base()

def get_db():
    db = SessionLocal() # Creates a fresh db session
    try:
        yield db # yield gives the session to whoever calls get_db and poses here
    finally:
        db.close() # Closes the session and returns the connection. Cleanup happens
