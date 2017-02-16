import os
import sys
import time
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Tasks(Base):
    __tablename__ = 'tasks'  # create table with name tasks
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(String(250))
    task_name = Column(String(250))
    stop_time = Column(String(250))

engine = create_engine("sqlite:///tasklist.db")

# Create all table
Base.metadata.create_all(engine)





