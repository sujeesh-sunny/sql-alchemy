from sqlalchemy import create_engine,column,string,integer
from sqlalchemy.orm import declarative_base,sessionmaker

Base = declarative_base()

class Employee(Base) :
    __tablename__ = 'employees'
    id = column(integer,primary_key = True)
    name = column(string(255),nullable = False)
    age = column(integer)
    place = column(string(255))
    
engine = create_engine('mysql+pymysql://sujeesh_usr:Mysql@121212@localhost/employee',echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

p1 = Employee(name='John', age=30, place='New York')
session.add_all(p1)
session.commit()