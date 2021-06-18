import csv, sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pirmas import Projektas, engine

Session = sessionmaker(bind=engine)
session = Session()


with open('auto.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    line_count = 1
    for row in csv_reader:
        make = row[0]
        model = row[1]
        color = row[2]
        year = row[3]
        price = row[4]
        car1 = Projektas(make, model, color, year, price)
        session.add(car1)
        session.commit()
        session.close()
        print(make, model, color, year, price)



