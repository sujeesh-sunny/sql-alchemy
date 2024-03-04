from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    price = Column(Float)
    weight = Column(Float)
    Variety = Column(String(255))
    Country_of_Origin = Column(String(255))
    Total_Stock_Quantity = Column(Integer)
    stock_weight = Column(Float)
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

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Query to join Groceries with Normalized Prices
result = (
    session.query(Grocery.Name, Grocery.price, NormalizedPrice.Normalized_Price, Grocery.weight)
    .join(NormalizedPrice, Grocery.RGS_ID == NormalizedPrice.Product_ID)
    .all()
)

for row in result:
    name, original_price, normalized_price, weight = row
    normalized_price_per_gram = original_price / weight
    print(f"Name: {name}, Original Price: {original_price}, Normalized Price: {normalized_price}, Weight: {weight}, Normalized Price per Gram: {normalized_price_per_gram}")

session.close()
