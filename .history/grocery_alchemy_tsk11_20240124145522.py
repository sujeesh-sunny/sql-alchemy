from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Float, Integer, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    weight = Column(Float)
    Quantity = Column(Integer)

password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

highest_stock_weight_item_query = (
    session.query(
        Grocery.Name.label('grocery_name'),
        func.sum(Grocery.weight * Grocery.Quantity).label('total_stock_weight')
    )
    .group_by(Grocery.Name)
    .order_by(func.sum(Grocery.weight * Grocery.Quantity).desc())
    .first()
)

if highest_stock_weight_item_query:
    grocery_name, total_stock_weight = highest_stock_weight_item_query
    print(f"The item with the highest total stock weight is '{grocery_name}' with a total weight of {total_stock_weight:.2f} KG.")
else:
    print("No information found for the item with the highest total stock weight.")
