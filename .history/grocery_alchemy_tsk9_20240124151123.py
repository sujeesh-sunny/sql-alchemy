from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Unit_of_Measure = Column(String(50))
    price = Column(String(50))
    Currency = Column(String(50))
    Quantity = Column(Integer)
    weight = Column(String(50))
    Variety = Column(String(255))
    Country_of_Origin = Column(String(255))
    Total_Stock_Quantity = Column(Integer)
    stock_weight = Column(String(50))
    Brand_Name = Column(String(255))
    Categories = Column(String(50))


password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

subq = (
    session.query(
        Grocery.RGS_ID,
        func.rank().over(order_by=Grocery.Total_Stock_Quantity.desc()).label('stock_rank')
    )
    .filter(Grocery.Categories == 'Vegetables')
    .subquery()
)


query = (
    session.query(
        Grocery,
        subq.c.stock_rank
    )
    .outerjoin(subq, subq.c.RGS_ID == Grocery.RGS_ID)
    .filter(Grocery.Categories == 'Vegetables')
    .order_by(subq.c.stock_rank)
)

results = query.all()

for item, rank in results:
    print(f"Item: {item.Name}, Stock Quantity: {item.Total_Stock_Quantity}, Rank: {rank}")
