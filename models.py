# Database table - describe our database table
# This is what the DB sees
# We write python and SQLAlchemy does the rest by creating an sql table
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Student(Base): # creates pythone class student that inherits from base
    __tablename__='students'

    id = Column(Integer,primary_key=True, index=True) # id is a column in table and is an integer
    name = Column(String, nullable=False) #nullable = false means the field is required
    course = Column(String, nullable=False)
    grade = Column(Float, default=0.0)
    email = Column(String, unique=True)