from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Float, Integer, ForeignKey, desc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

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

class NormalizedPrice(Base):
    __tablename__ = 'Normalized_Price'
    NP_ID = Column(Integer, primary_key=True)
    Normalized_Price = Column(Float)
    Unit_of_Measurement = Column(String(10))
    Product_ID = Column(Integer, ForeignKey('Grocery.RGS_ID'))
    
    grocery = relationship("Grocery", back_populates="normalized_prices")

Grocery.normalized_prices = relationship("NormalizedPrice", order_by=NormalizedPrice.NP_ID, back_populates="grocery")


password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store", echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

most_expensive_per_gram = (
    session.query(Grocery, NormalizedPrice)
    .join(NormalizedPrice, Grocery.RGS_ID == NormalizedPrice.Product_ID)
    .order_by(desc(Grocery.price / Grocery.weight))
    .first()
)

if most_expensive_per_gram:
    item, normalized_price = most_expensive_per_gram
    print(f"The most expensive per gram item is: {item.Name}, Price per gram: {item.price / item.weight}, Normalized Price: {normalized_price.Normalized_Price}")
else:
    print("No data found.")

session.close()
