from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, Numeric, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Unit_of_Measure = Column(String(255))
    price = Column(Numeric)
    Quantity = Column(Integer)

class JioMart(Base):
    __tablename__ = 'Jio_Mart'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Unit_of_Measure = Column(String(255))
    price = Column(Numeric)
    Quantity = Column(Integer)

password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

banana_comparison_query = (
    session.query(
        Grocery.Name.label('Grocery_Name'),
        Grocery.price.label('Grocery_Price'),
        Grocery.Unit_of_Measure.label('Grocery_Unit_of_Measure'),
        JioMart.Name.label('Jio_Mart_Name'),
        JioMart.price.label('Jio_Mart_Price'),
        JioMart.Unit_of_Measure.label('Jio_Mart_Unit_of_Measure')
    )
    .filter(Grocery.Name == 'Banana', JioMart.Name == 'Banana')
    .all()
)

for result in banana_comparison_query:
    grocery_name, grocery_price, grocery_unit, jio_mart_name, jio_mart_price, jio_mart_unit = result
    print(f"{grocery_name} ({grocery_unit}): {grocery_price} vs {jio_mart_name} ({jio_mart_unit}): {jio_mart_price}")
