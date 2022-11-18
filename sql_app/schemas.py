from typing import List, Optional

from pydantic import BaseModel


class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birthdate: Optional[str] = None
    identification: Optional[str] = None
    


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True



