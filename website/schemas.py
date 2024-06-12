from pydantic import BaseModel
from typing import List

class Disc(BaseModel):
    mold_name: str
    plastic: str 
    manufacturer: str
    price: int
    url: str

    class Config:
        from_attributes = True

class DiscList(BaseModel):
    data: List[Disc]
