from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer)
    place = Column(String(255))
    
engine = create_engine('mysql+pymysql://sujeesh_usr:Mysql@localhost/employee', echo=True)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

p1 = Employee(name='John', age=30, place='New York')
session.add_all([p1])  # Note: Use a list even for a single instance when using add_all
session.commit()
