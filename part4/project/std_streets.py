#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "rio-sample.osm"
#street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
street_type_re = re.compile(r'^\S+\.?\b', re.IGNORECASE)

expected = ["Alameda", "Avenida", "Beco", "Caminho", "Estrada", "Ladeira", "Largo", "Praça", "Praia", "Rodovia", "Rua", "Travessa"]

# UPDATE THIS VARIABLE
mapping = { "Est.": "Estrada",
            "estrada": "Estrada",
            "Pça.": "Praça",
            "Pca.": "Praça",
            "Praca": "Praça",
            "Av.": "Avenida",
            "Av": "Avenida",
            "Rod.": "Rodovia",
            "R." : "Rua"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type.encode('utf8') not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):

    # YOUR CODE HERE
    m = street_type_re.search(name)
    street_type = m.group()

    new_road_name = mapping[street_type]
    name = street_type_re.sub(new_road_name, name)

    return name


def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))
    #assert len(st_types) == 3

"""
    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"
"""

if __name__ == '__main__':
    test()
