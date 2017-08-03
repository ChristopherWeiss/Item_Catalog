from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    category = Column(String(25))
    description = Column(String(250))
    


engine = create_engine('sqlite:///itemcatalogwithusers.db')


Base.metadata.create_all(engine)