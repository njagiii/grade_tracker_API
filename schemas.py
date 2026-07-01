# This will be the data validator
#This is what the user sees
from pydantic import BaseModel
from typing import Optional

#This is what the user sends to create
class StudentCreate(BaseModel): #Schema for when someone wants to add a new student
    name:str
    course:str
    grade:float = 0.0
    email:str

#This is what the user sends to update
#This class is for when someone wants to change student details
#Here everything is optional-One is able to update one or two fields to change
class StudentUpdate(BaseModel):
    name: Optional[str] = None #None means skip updating it if not sent
    course:Optional[str] = None
    grade:Optional[float] = None
    email:Optional[str] = None

# This is what comes back when someone makes a request 
# it contains ID because we want to tell user the ID they were assigned
class StudentResponse(BaseModel):
    id:int
    name:str
    course: str
    grade:float
    email:str

# Bridge between database and API worlds
# DB gives SQLAlchemy object, the API needs to return a pydantic schema
class Config: #A configuration setting - special pydantic class
    from_attributes = True # Must be true to read SQLAlchemy model object