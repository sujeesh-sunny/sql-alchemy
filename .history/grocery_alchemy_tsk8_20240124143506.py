from sqlalchemy import create_engine, func, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Unit_of_Measure = Column(String(10))
    price = Column(Float)
    Currency = Column(String(3))
    Quantity = Column(Integer)
    weight = Column(Float)
    Variety = Column(String(255))
    Country_of_Origin = Column(String(255))
    Total_Stock_Quantity = Column(Integer)
    stock_weight = Column(Float)
    Brand_Name = Column(String(255))
    Categories = Column(String(255))

# URL-encode the password
password = "Mysql@121212"
encoded_password = quote_plus(password)

# Corrected connection URL
engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Calculate the average price of all items
average_price = session.query(func.avg(Grocery.price)).scalar()

# Query to find items with prices above the average price
result = session.query(Grocery) \
               .filter(Grocery.price > average_price) \
               .all()

for item in result:
    print(f"Item: {item.Name}, Price: {item.price}")
