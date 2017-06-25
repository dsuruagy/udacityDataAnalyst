#!/usr/bin/env python 
from pymongo import MongoClient

DB_NAME = 'examples'
COLLECTION_NAME = 'rio_osm'

def get_col(db_name, col_name):
    client = MongoClient('127.0.0.1:27017')
    db = client[db_name]
    return db[col_name]
    
def aggregate(pipeline):
    return [doc for doc in collection.aggregate(pipeline)]
    
def get_one_result(pipeline, key):
    return aggregate(pipeline)[0][key]
    
'''
    number of unique users
    number of nodes and ways
    number of chosen type of nodes, like cafes, shops etc. 
'''
def query_statistics():
    
    print 'Count:', collection.count()
    
    '''
    pip_top_users = [{'$group' : {'_id': '$created.user', 'total' : {'$sum' : 1}}},
                    {'$sort' : {'total' : -1}}]
    top_users = [doc for doc in collection.aggregate(pip_top_users)]
    '''
    
    pip_unique_users = [{'$group' : {'_id' : '$created.user'}},
                        {'$count' : 'num'}]
    num_unique_users = get_one_result(pip_unique_users, 'num')
    print 'Unique users:', num_unique_users

    pip_number_nodes_ways = [{'$match' : {'type' : {'$in' : ['node', 'way']}}},
                        {'$group' : {'_id' : '$type', 'total' : {'$sum' : 1}}}]
    number_nodes_ways = aggregate(pip_number_nodes_ways)
    print 'Number of nodes and ways:', number_nodes_ways
    
    chosen_nodes = ['fast_food', 'pharmacy', 'restaurant', 'bank']
    pip_number_chosen_nodes = [{'$match' : {'type' : 'node', 'amenity' : {'$in' : chosen_nodes}}},
                             {'$group' : {'_id' : '$amenity', 'total' : {'$sum' : 1}}}]
    
    number_chosen_nodes = aggregate(pip_number_chosen_nodes)
    print 'Number of chosen type of nodes:', number_chosen_nodes
    
if __name__ == '__main__':
    collection = get_col(DB_NAME, COLLECTION_NAME)
    
    query_statistics()
