from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base
    
class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True,index=True)    
    identification = Column(String(200))
    first_name = Column(String(80), nullable=False)
    last_name= Column(String(80), nullable=False)
    birthdate = Column(String(80))
    def __repr__(self):
        return 'PersonModel(first_name=%s, last_name=%s)' % (self.first_name, self.last_name)
    

