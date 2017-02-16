import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine



Base = declarative_base()

class Tasks(Base):
    __tablename__ = 'tasks' # create table with name tasks
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(DateTime())
    task_name = Column(String(250))
    task_cycles = Column(Integer)

engine = create_engine("sqlite:///tasklists.db")

# Create all table
Base.metadata.create_all(engine)





