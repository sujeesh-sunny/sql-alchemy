from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'grocery'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    Quantity = Column(Integer)
    Price = Column(Float)
    Categories = Column(String(255))


password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Grocery")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

new_grocery = [
    Grocery(Name='Apple', Quantity=1, Price=60, Categories='fruits'),
    Grocery(Name='Orange', Quantity=1, Price=40, Categories='fruits'),
    Grocery(Name='Pineapple', Quantity=2, Price=70, Categories='fruits'),
    Grocery(Name='Tomato', Quantity=1, Price=30, Categories='vegetables'),
    Grocery(Name='Potato', Quantity=1, Price=20, Categories='vegetables'),
    Grocery(Name='Onion', Quantity=1, Price=45, Categories='vegetables')
    
]
session.add_all(new_grocery)
session.commit()