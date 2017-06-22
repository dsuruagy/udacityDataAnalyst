#!/usr/bin/env python
# -*- coding: utf-8 -*-
from write_json import process_map
from pymongo import MongoClient
import json

OSMFILE  = 'rio-sample.osm'
DATABASE = 'examples'
COLLECT  = 'rio_osm'

def insert_data(data, col):

    for reg in data:
        col.insert_one(reg)


if __name__ == "__main__":
    
    print '*** Writing JSON file...'
    data = process_map(OSMFILE, False)
    
    print '*** Importing JSON content to MongoDB...'
    client = MongoClient("mongodb://localhost:27017")
    db = client[DATABASE]
    col = db[COLLECT]

    with open("{0}.json".format(OSMFILE)) as f:
        data = json.loads(f.read())
        insert_data(data, col)
        print col.find_one()

