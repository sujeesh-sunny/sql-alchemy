from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, Numeric, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    price = Column(Numeric)
    Categories = Column(String(255))

password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

average_fruits_price_query = (
    session.query(
        func.avg(Grocery.price).label('average_price')
    )
    .filter(Grocery.Categories == 'Fruits')
    .first()
)

if average_fruits_price_query.average_price is not None:
    print(f"The average price of items in the 'Fruits' category is: {average_fruits_price_query.average_price}")
else:
    print("No items found in the 'Fruits' category.")
