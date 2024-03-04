from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class GroceryItem(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
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

# Replace 'your_password' with the actual password
password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store", echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

data = [
    GroceryItem(
        Name='Apple', Unit_of_Measure='KG', price=100.0000, Currency='INR', Quantity=6, weight=1.0000,
        Variety='Kashmir_Apple', Country_of_Origin='India', Total_Stock_Quantity=500, stock_weight=250.0000,
        Brand_Name='KA', Categories='Fruits'
    ),
    GroceryItem(
        Name='Tomato', Unit_of_Measure='KG', price=25.0000, Currency='INR', Quantity=6, weight=1.0000,
        Variety='Roma', Country_of_Origin='Italy', Total_Stock_Quantity=100, stock_weight=50.0000,
        Brand_Name='FreshVeg', Categories='Vegetables'
    ),
    GroceryItem(
        Name='Brocoli', Unit_of_Measure='KG', price=50.0000, Currency='INR', Quantity=6, weight=1.0000,
        Variety='calabrase', Country_of_Origin='USA', Total_Stock_Quantity=50, stock_weight=150.0000,
        Brand_Name='GreenHarvest', Categories='Vegetables'
    ),
    GroceryItem(
        Name='Banana', Unit_of_Measure='KG', price=50.0000, Currency='INR', Quantity=6, weight=1.0000,
        Variety='Cavandish', Country_of_Origin='Ecuador', Total_Stock_Quantity=50, stock_weight=150.0000,
        Brand_Name='TropicalDelight', Categories='Vegetables'
    ),
    GroceryItem(
        Name='Orange', Unit_of_Measure='KG', price=60.0000, Currency='INR', Quantity=6, weight=1.0000,
        Variety='Valancia', Country_of_Origin='USA', Total_Stock_Quantity=50, stock_weight=150.0000,
        Brand_Name='VineSweet', Categories='Fruits'
    ),
    GroceryItem(
        Name='Grapes', Unit_of_Measure='KG', price=65.0000, Currency='INR', Quantity=5, weight=1.0000,
        Variety='Gold', Country_of_Origin='India', Total_Stock_Quantity=250, stock_weight=500.0000,
        Brand_Name='IG', Categories='Fruits'
    ),
]

session.add_all(data)
session.commit()
