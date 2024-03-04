from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Variety = Column(String(255))
    Total_Stock_Quantity = Column(Integer)

password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")
        
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

max_variety_item = (
    session.query(
        Grocery.Name,
        func.count(func.distinct(Grocery.Variety)).label('variety_count')
    )
    .group_by(Grocery.Name)
    .order_by(func.count(func.distinct(Grocery.Variety)).desc())
    .first()
)

if max_variety_item:
    item_name, variety_count = max_variety_item
    print(f"The item with the maximum number of varieties is '{item_name}' with {variety_count} varieties.")
else:
    print("No items found.")
