from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Float, Integer, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Unit_of_Measure = Column(String(10))
    price = Column(Float)
    Currency = Column(String(10))
    Quantity = Column(Integer)
    weight = Column(Float)
    Variety = Column(String(255))
    Country_of_Origin = Column(String(255))
    Total_Stock_Quantity = Column(Integer)
    stock_weight = Column(Float)
    Brand_Name = Column(String(255))
    Categories = Column(String(255))


password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store", echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

average_price_fruits = (
    session.query(func.avg(Grocery.price).label('average_price'))
    .filter(Grocery.Categories == 'Fruits')
    .first()
)

if average_price_fruits.average_price is not None:
    print(f"The average price of items in the 'Fruits' category is: {average_price_fruits.average_price}")
else:
    print("No data found.")

session.close()
