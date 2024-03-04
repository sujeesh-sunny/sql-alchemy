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

p1 = Employee(name='john', age=30, place='New York')
p2 = Employee(name='alice', age=20, place='New York')

session.add_all([p1,p2])

session.commit()