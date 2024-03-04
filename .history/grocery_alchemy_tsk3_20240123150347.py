from urllib.parse import quote_plus
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

password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store", echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

cheapest_fruit = session.query(GroceryItem.Name, GroceryItem.price).filter(GroceryItem.Categories == 'Fruits').order_by(GroceryItem.price).first()

if cheapest_fruit:
    print(f"Cheapest Fruit: {cheapest_fruit.Name}, Price: {cheapest_fruit.price}")
else:
    print("No fruits found in the groceries table.")
