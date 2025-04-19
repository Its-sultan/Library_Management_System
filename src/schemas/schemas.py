
from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title:str = Field(...,example ="The Great Sultan")
    author: str = Field(..., example ="T. Sultan Abdallah")
    published_year: Optional[int] = Field(None, example =2310)
    isbn: Optional[str] = Field(None, example="152827rBTP4")
    
    
class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    
    class Config:
        orm_mode = True
        # This is to tell Pydantic to allow ORM models (like Book) to be returned as dictionaries. 
        # This is a security feature to ensure that only valid data is returned. 
        # This is the reason why we have to subclass our models from Pydantic's BaseModel


        