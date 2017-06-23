#!/usr/bin/env python
# -*- coding: utf-8 -*-
from write_json import process_map
from pymongo import MongoClient
import json

OSMFILE  = 'rio-de-janeiro_brazil.osm'

def insert_data(data, col):

    for reg in data:
        col.insert_one(reg)


if __name__ == "__main__":
    
    print '*** Writing JSON file...'
    data = process_map(OSMFILE, False)

