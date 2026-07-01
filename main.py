#Where it all connects
#Creates FastAPI app
#Creates the DB tables
#Defines all endpoints
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import get_db, engine

models.Base.metadata.create_all(bind=engine)


# Create your application - this is the main object
app = FastAPI(title='Student Grade Tracker', 
              description='Track students grades with Fast API',
              version='1.0.0')


# Create
@app.post('/students/',response_model=schemas.StudentResponse)
def create_student(student:schemas.StudentCreate,db:Session=Depends(get_db)):
    return crud.create_students(db,student)

#Read all
@app.get('/students/',response_model=List[schemas.StudentResponse])
def get_students(db:Session=Depends(get_db)):
    return crud.get_students(db)
    
#Read one
@app.get('/student/{student_id}',response_model=schemas.StudentResponse)
def get_student(student_id:int,db:Session=Depends(get_db)):
    student = crud.get_student(db,student_id)
    if not student:
        raise HTTPException(404,'Student Not Found!!')
    return student

#Update
@app.put('/students/{student_id}',response_model=schemas.StudentResponse)
def update_student(student_id:int,data: schemas.StudentUpdate,
                   db:Session=Depends(get_db)):
    updated_student = crud.update_student(db,student_id,data)
    if not updated_student:
        raise HTTPException(404, 'Failed to update check the values or id you input!!')
    return updated_student

#Delete
@app.delete('/students/{student_id}')
def delete_student(student_id:int,db:Session=Depends(get_db)):
    student = crud.delete_student(db,student_id)
    if not student:
        raise HTTPException(404, 'Student not found!!')
    return{'Message':'Student Deleted Successfully!!'}

#SQLite - DB that lives in a single file or on your computer. No installation, configuration or server needed
#SQLAlchemy - python library that talks to the DB for us. We write python it writes SQL

# Session - A temporary connection to the DB - open it, use it, close it
#Files needed - database.py, models.py, schemas.py, crud.py