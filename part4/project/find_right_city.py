#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
REFERENCES:
https://stackoverflow.com/questions/6159074/given-the-lat-long-coordinates-how-can-we-find-out-the-city-country
https://developers.google.com/maps/documentation/geocoding/start?csw=1#reverse_geocode
'''

import sys
import googlemaps
from pymongo import MongoClient

DB_NAME = 'examples'
COLLECTION_NAME = 'rio_osm'
API_KEY='use_your_key'

def find_correct_city(coords_array):
    gmaps = googlemaps.Client(key=API_KEY)

    # Look up an address with reverse geocoding
    rev_geocode = gmaps.reverse_geocode((coords_array[0], coords_array[1]))
    addr_components = rev_geocode[0]['address_components']
    #print 'addr_components:', addr_components
    for comp in addr_components:
        if 'locality' in comp['types']:
            # returns city name
            print 'Right name:', comp['long_name']

def get_col(db_name, col_name):
    client = MongoClient('127.0.0.1:27017')
    db = client[db_name]
    return db[col_name]
    
def find_wrong_city_coords(name):
    print 'Wrong name:', name
    nodes = [node for node in collection.find({'address.city' : name})]

    # If node type is Way, take cordinates of one node_ref
    if nodes[0]['type'] == 'way':
        nodes = [node for node in collection.find({'id' : nodes[0]['node_refs'][0]})]

    return nodes[0]['pos']
      
    
if __name__ == '__main__':
    collection = get_col(DB_NAME, COLLECTION_NAME)
        
    if len(sys.argv) != 2:
        print 'ERROR'
    else:
        coords = find_wrong_city_coords(str(sys.argv[1]))
        geo = find_correct_city(coords)
    
