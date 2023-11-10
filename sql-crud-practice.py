from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


#create a class-based model for the "Programmer" table
class Country(base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)
    currency = Column(String)
    population = Column(Float)
    language = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records for our Programmer table
brazil = Country(
    name = "Brazil",
    capital="Brasilia",
    currency="Real",
    population=219,
    language="Portuguese"
)

denmark = Country(
    name = "Denmark",
    capital="Copenhagen",
    currency="Danish Kroner",
    population=5.9,
    language="Danish"
)

mexico = Country(
    name = "Mexico",
    capital="Mexico City",
    currency="Peso",
    population=129,
    language="Spanish"
)

vietnam = Country(
    name = "Vietnam",
    capital="Hanoi",
    currency="Vietnamese Dong",
    population=102,
    language="Vietnamese"
)

# add each instance of our programmers to our session
# session.add(brazil)
# session.add(denmark)
# session.add(mexico)
# session.add(vietnam)

# deleting a record
country_name = input("Please enter the country you wish to delete: ")
country = session.query(Country).filter_by(name=country_name).first()
# #  defensive programming
if country is not None:
    print("Country found: ", country.name)
    confirmation = input("Are you sure you want to delete this record (y/n) ")
    if confirmation.lower() == "y":
        session.delete(country)
        session.commit()
        print("Country has been deleted")
else:
    print("No records found.")

# commit our session to the database
session.commit()

countries = session.query(Country)
for country in countries:
    print(
        country.id,
        country.name,
        country.capital,
        country.currency,
        country.population,
        country.language,
        sep = " | "
    )