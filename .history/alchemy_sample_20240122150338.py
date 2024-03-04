from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees_1'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer)
    place = Column(String(255))

# URL-encode the password
password = "Mysql@121212"
encoded_password = quote_plus(password)

# Corrected connection URL
engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/people")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

data = [
    Employee(name='John', age=30, place='New York'),
    Employee(name='Alice', age=25, place='Lose Angeles'),
    Employee(name='Bob', age=35, place='Chicago'),
    Employee(name='John', age=30, place='San Francisco'),
    Employee(name='Sujeesh', age=24, place='Nilambur'),
    Employee(name='Abhijith', age=25, place='Nathapuram'),
    Employee(name='Jazil', age=20, place='Calicut')
]

session.add_all([p1,p2])

session.commit()