from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'grocery'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    Quantity = Column(Integer)
    price = Column(Float)
    Categories = Column(String(255))


password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Grocery")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

new_grocery = [
    Grocery(name='Apple', quantity=1, price=60, category='fruits'),
    Grocery(name='Orange', quantity=1, price=40, category='fruits'),
    Grocery(name='Pineapple', quantity=2, price=70, category='fruits'),
    Grocery(name='Tomato', quantity=1, price=30, category='vegetables'),
    Grocery(name='Potato', quantity=1, price=20, category='vegetables'),
    Grocery(name='Onion', quantity=1, price=45, category='vegetables')
    
]
session.add_all(new_grocery)
session.commit()