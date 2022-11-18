from sqlalchemy.orm import Session

from . import models, schemas


class PersonRepo:
    
 async def create(db: Session, person: schemas.PersonCreate):
        db_person = models.Person(first_name=person.first_name,last_name=person.last_name,birthdate=person.birthdate,identification=person.identification)
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return db_person



 
 def fetch_all(db: Session):
     return db.query(models.Person).all()
 

