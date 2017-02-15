import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Tasks(Base):
    __tablename__ = 'logs' # create table with name logs
    id = Column(Integer, primary_key=True, autoincrement=True)
    


