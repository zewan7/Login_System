from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import sessionmaker
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from config import config

engine = sqlalchemy.create_engine(config["db_url"])
Session = sessionmaker(bind=engine)
session = Session()
DateTime = mysql.DATETIME

Base = declarative_base()


class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(BLOB(255), nullable=False)
    create_time = Column(DateTime)
    update_time = Column(DateTime)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
