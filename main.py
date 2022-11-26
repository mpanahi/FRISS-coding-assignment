from fastapi import Depends, FastAPI, HTTPException
from db import get_db, engine
import sql_app.models as models
import sql_app.schemas as schemas
from sql_app.repositories import PersonRepo
from sqlalchemy.orm import Session
import uvicorn
from fraud_detection.checking_strategy import *
from fastapi.responses import JSONResponse

app = FastAPI(title="FRISS Coding Assignmen")

models.Base.metadata.create_all(bind=engine)

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.post('/store', tags=["Person"],response_model=schemas.Person)
async def create_person(person_request: schemas.PersonCreate, db: Session = Depends(get_db)):
    """
    Create an Item and store it in the database
    """
    
    #db_person = PersonRepo.fetch_by_first_name(db, first_name=item_request.first_name)
    #if db_person:
        #raise HTTPException(status_code=400, detail="Item already exists!")

    return await PersonRepo.create(db=db, person=person_request)


@app.post('/check', tags=["Person"])
async def check_person(person_request: schemas.PersonCreate, db: Session = Depends(get_db)):
    """
    Checking the probability that the person already exists in the db
    """

    db_people = PersonRepo.fetch_all(db)


    checking=Checking(db_all=db_people, person=person_request,checking_strategy="strategyOne")
    return await checking.matching()


#if __name__ == "__main__":
    #uvicorn.run("main:app", port=9000, reload=True)
    
