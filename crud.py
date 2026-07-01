# sqlalchemy, pydantic, fastapi, sqlite, class
# This is the file where DB operations happen
# Where DB work happens
# We have to open sessions in SQLAlchemy
from sqlalchemy.orm import Session
import models, schemas

def create_students(db:Session,student:schemas.StudentCreate):
    db_student=models.Student(**student.model_dump()) # Unpacking dict (name='Alice')
    db.add(db_student) #Stage the record - says I want to save this
    db.commit() #Save to disk - this is when data is actually written to DB
    db.refresh(db_student) # Reloads after saving it in DB and gives a new ID
    return db_student #Return completed student object

def get_student(db:Session,student_id:int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()
    #Starts a query on the student table and filters based on id and returns only first result
    #Returns none if nothing is found

#Read all records - Query all students
def get_students(db:Session):
    return db.query(models.Student).all() #Like select * from students

#Update record
def update_student(db:Session,student_id:int,data: schemas.StudentUpdate):
    student = db.query(models.Student).filter(models.Student.id==student_id).first()
    if not student:
        return None
    updates = data.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)
    return student

# Delete Record
def delete_student(db:Session,student_id:int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    db.delete(student)
    db.commit()
    return student