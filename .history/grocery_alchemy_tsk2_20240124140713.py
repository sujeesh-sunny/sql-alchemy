from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class GroceryItem(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    price = Column(Float)
    Categories = Column(String(255))

password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store", echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

vegetables = session.query(GroceryItem.RGS_ID, GroceryItem.Name, GroceryItem.price, GroceryItem.Categories).filter(GroceryItem.Categories == 'Vegetables').all()

for vegetable in vegetables:
    print(f"RGS_ID: {vegetable.RGS_ID}, Name: {vegetable.Name}, Price: {vegetable.price}, Category: {vegetable.Categories}")
