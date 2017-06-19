#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]
ROOT_KEYS = ["id", "visible", "type", "pos", "amenity", "cuisine", "name", "phone", "node_refs"]

def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        # YOUR CODE HERE
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

            # if the second level tag "k" value contains problematic characters, it should be ignored
            if problemchars.match(key):
                continue

            elif lower.match(key) and key in ROOT_KEYS:
                node[key] = value

            # if the second level tag "k" value does not start with "addr:"
            elif lower_colon.match(key):
                if key.startswith('addr:'):
                    key = re.match(r'^([a-z]*):([a-z]*)$', key).group(2)
                    addr_values[key] = value

        if len(addr_values) > 0:
            node['address'] = addr_values

        nd_values = [nd.get('ref') for nd in element.findall("nd")]

        if len(nd_values) > 0:
            node['node_refs'] = nd_values

        return node
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w", encoding='utf8') as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    #fo.write(unicode(json.dumps(el, indent=2, ensure_ascii=False))+"\n")
                    fo.write(json.dumps(el, indent=2, ensure_ascii=False)+"\n")
                else:
                    #fo.write(unicode(json.dumps(el, ensure_ascii=False)) + "\n")
                    fo.write(json.dumps(el, ensure_ascii=False) + "\n")
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset,
    # call the process_map procedure with pretty=False. The pretty=True option adds
    # additional spaces to the output, making it significantly larger.
    data = process_map('rio-sample.osm', True)
    #pprint.pprint(data)
    pprint.pprint(data[0])
    '''
    correct_first_elem = {
        "id": "261114295",
        "visible": "true",
        "type": "node",
        "pos": [41.9730791, -87.6866303],
        "created": {
            "changeset": "11129782",
            "user": "bbmiller",
            "version": "7",
            "uid": "451048",
            "timestamp": "2012-03-28T18:31:23Z"
        }
    }
    assert data[0] == correct_first_elem
    assert data[-1]["address"] == {
                                    "street": "West Lexington St.",
                                    "housenumber": "1412"
                                      }
    assert data[-1]["node_refs"] == [ "2199822281", "2199822390",  "2199822392", "2199822369",
                                    "2199822370", "2199822284", "2199822281"]
    '''

if __name__ == "__main__":
    test()
