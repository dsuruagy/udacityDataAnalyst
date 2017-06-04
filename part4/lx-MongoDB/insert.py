#!/usr/bin/env python
""" 
Add a single line of code to the insert_autos function that will insert the
automobile data into the 'autos' collection. The data variable that is
returned from the process_file function is a list of dictionaries, as in the
example in the previous video.
"""

from autos import process_file
from cities import process_cities_file
import pprint

def insert_autos(infile, db):
    data = process_file(infile)
    # Add your code here. Insert the data in one command.
    db.autos.insert(data)
  
def insert_cities(infile, db):
    data = process_cities_file(infile)
    db.cities.insert(data)
  
if __name__ == "__main__":
    # Code here is for local use on your own computer.
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    if False:
        insert_autos('autos-small.csv', db)
        pprint.pprint(db.autos.find_one())
        
    if True:
        insert_cities('cities.csv', db)
        pprint.pprint(db.cities.find_one())
        
