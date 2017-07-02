#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import re
import codecs
import os
import json
from audit_streets import audit_street_name
from audit_postcodes import audit_postcode

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]
ROOT_KEYS = ["id", "visible", "type", "pos", "amenity", "cuisine", "name", "phone", "node_refs"]

def shape_element(element):
    node = {}

    if element.tag == "node" or element.tag == "way" :
        node['type'] = element.tag

        # attributes in the CREATED array should be added under a key "created"
        created_values = {}
        for attr in element.keys():
            if attr in CREATED:
                created_values[attr] = element.get(attr)
            elif attr in ROOT_KEYS:
                node[attr] = element.get(attr)

        node['created'] = created_values

        # attributes for latitude and longitude should be added to a "pos" array
        lat = element.get('lat')
        lon = element.get('lon')

        if lat != None and lon != None:
            node['pos'] = [float(lat), float(lon)]

        addr_values = {}

        for tag in element.findall("tag"):
            key = tag.get("k")
            value = tag.get("v")

            # if the second level tag "k" value contains problematic
            # characters, it should be ignored
            if problemchars.match(key):
                continue

            # if the second level tag "k" value does not start with "addr:"
            elif lower.match(key) and key in ROOT_KEYS:
                node[key] = value

            # if it is an address
            elif lower_colon.match(key):
                if key.startswith('addr:'):
                    try:
                        # take only the second part of address
                        key = re.match(r'^([a-z]*):([a-z_]*)$', key).group(2)
                    except AttributeError:
                        print 'Error on key ', key
                        
                    if key == 'street':
                        value = audit_street_name(value)
                        
                    if key == 'postcode':
                        value = audit_postcode(value)

                    # fills address dictionary
                    addr_values[key] = value

        if len(addr_values) > 0:
            node['address'] = addr_values

        # Process Node tags
        nd_values = [nd.get('ref') for nd in element.findall("nd")]

        if len(nd_values) > 0:
            node['node_refs'] = nd_values

        return node
    else:
        return None


def process_map(file_in, pretty = False):
    print 'Input file size:  {0}MB'.format(os.stat(file_in).st_size/(1024**2))

    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w", encoding='utf8') as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                #data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2, ensure_ascii=False)+"\n")
                else:
                    fo.write(json.dumps(el, ensure_ascii=False) + "\n")
    print 'Output file size: {0}MB'.format(os.stat(file_out).st_size/(1024**2))

    return data
    
OSMFILE  = 'rio-de-janeiro_brazil.osm'
#OSMFILE  = 'rio-sample.osm'

if __name__ == "__main__":
    
    print '*** Writing JSON file...'
    data = process_map(OSMFILE, False)
