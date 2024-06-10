from sqlalchemy import String, Integer, Column, DateTime
from sqlalchemy.sql import func
from database import Base

class Disc(Base):
    __tablename__ = "discs"

    mold_name = Column(String, primary_key=True)
    plastic = Column(String, primary_key=True)
    manufacturer = Column(String)
    price = Column(Integer)
    url = Column(String)
    last_updated = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"Disc[mold_name={self.mold_name}, plastic={self.plastic}, manufacturer = {self.manufacturer}, price = {self.price}, url = {self.url}]"
