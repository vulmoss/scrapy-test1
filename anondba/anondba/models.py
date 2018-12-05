from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy import Date
engine=create_engine('mysql+mysqldb://root@localhost:3306/anondba?charset=utf8')
Base=declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id=Column(Integer,primary_key=True)
    name = Column(String(64),index=True)
    desc=Column(String(1024))
    type1=Column(String(64),index=True)
class User(Base):
    __tablename__ ='users'

    id = Column(Integer,primary_key=True)
    name = Column(String(64),index=True)
    type=Column(String(64),index=True)
    status=Column(String(64),index=True)
    job=Column(String(64))
    level=Column(Integer,index=True)
    join_date=Column(Date)
    learn_courses_num=Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
