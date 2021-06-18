import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///cars.db')
Base = declarative_base()

class Projektas(Base):
    __tablename__ = 'Cars'
    id = Column(Integer, primary_key=True)
    make = Column("Make", String)
    model = Column("Model", String)
    color = Column("Color", String)
    year = Column("Year", Integer)
    price = Column("Price", Integer)

    def __init__(self, make, model, color, year, price):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.make} - {self.model}, {self.color}: {self.year}, {self.price}"

Base.metadata.create_all(engine)