import time
import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from sqlalchemy import create_engine, MetaData, Table

Base = declarative_base()
engine = create_engine("sqlite:///C:/Users/SIMPOL PAUL/Desktop/bc-15-pomodoro_Rada/rada-cli/tasklists.db")

class Tasks(Base):
    __tablename__ = 'taskrecords'
    


