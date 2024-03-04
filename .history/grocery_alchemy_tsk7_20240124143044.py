from urllib.parse import quote_plus
from sqlalchemy import create_engine, func, select, text, column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = column(Integer, primary_key=True)
    Name = column(String(255))
    Unit_of_Measure = column(String(10))
    price = column(Float)
    Currency = column(String(3))
    Quantity = column(Integer)
    weight = column(Float)
    Variety = column(String(255))
    Country_of_Origin = column(String(255))
    Total_Stock_Quantity = column(Integer)
    stock_weight = column(Float)
    Brand_Name = column(String(255))
    Categories = column(String(255))

password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Grocery.Categories, func.sum(Grocery.stock_weight).label('total_stock_weight')) \
               .group_by(Grocery.Categories) \
               .all()

for row in result:
    print(f"Category: {row.Categories}, Total Stock Weight: {row.total_stock_weight}")
