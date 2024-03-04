from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Grocery(Base):
    __tablename__ = 'Grocery'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Variety = Column(String(255))
    Country_of_Origin = Column(String(255))

class JioMart(Base):
    __tablename__ = 'Jio_Mart'
    RGS_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Variety = Column(String(255))
    Country_of_Origin = Column(String(255))

password = "Mysql@121212"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sujeesh_usr:{encoded_password}@localhost/Relaince_Grocery_Store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

reliance_apple_query = (
    session.query(Grocery.Variety, Grocery.Country_of_Origin)
    .filter(Grocery.Name == 'Apple')
    .all()
)

jio_mart_apple_query = (
    session.query(JioMart.Variety, JioMart.Country_of_Origin)
    .filter(JioMart.Name == 'Apple')
    .all()
)

print("Variety and Country of Origin for Apples in Reliance Groceries:")
for variety, origin in reliance_apple_query:
    print(f"Variety: {variety}, Country of Origin: {origin}")

print("\nVariety and Country of Origin for Apples in Jio_Mart:")
for variety, origin in jio_mart_apple_query:
    print(f"Variety: {variety}, Country of Origin: {origin}")
