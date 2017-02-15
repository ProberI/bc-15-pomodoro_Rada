import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Tasks(Base):
    __tablename__ = 'logs' # create table with name logs
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(DateTime())
    task_name = Column(String(250))
    task_cycles = Column(Integer)

engine = create_engine("sqlite:///C:/Users/SIMPOL PAUL/Desktop/bc-15-pomodoro_Rada/rada-cli/tasklists.db")

# Create all table
Base.metadata.create_all(engine)





