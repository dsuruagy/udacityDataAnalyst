#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

street_type_re = re.compile(r'^\S+\.?', re.IGNORECASE)
commas_present_re = re.compile(r'([\s\w]*),(\S*)', re.UNICODE)

expected = ['Alameda', 'Avenida', 'Auto', 'Beco', 'Boulevard', 'Campo', 'Caminho',
            'Estrada', 'Ladeira', 'Largo', 'Parque', u'Praça', 'Praia', 'Quadra',
            'Rodovia', 'Rua', 'Travessa', 'Via']

mapping = { 'Est.': 'Estrada',
            'estrada': 'Estrada',
            u'Pça.': u'Praça',
            'Pca.': u'Praça',
            'Praca': u'Praça',
            'Av.': 'Avenida',
            'Av': 'Avenida',
            'Rod.': 'Rodovia',
            'R.' : 'Rua',
            'rua' : 'Rua',
            'RUA' : 'Rua'
            }

def audit_street_name(street_name):
    street_name = audit_street_type(None, street_name)
    street_name = audit_comma_present(None, street_name) 
    
    return street_name
     
def audit_street_type(street_types, street_name):
    # audit if street name starts with a name and a dot, defined in regex
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        
        # if the first name is not in expected, it need to be adjusted
        if street_type not in expected:
            
            if street_types != None:
                street_types[street_type].add(street_name)

            # Verifying if the unexpected street type can be mapped to a known value
            ##print 'Name before: ', street_name
            if street_type in mapping.keys():
                street_name = update_name(street_name, mapping)
            else:
                # If there is no street type, append the name to the default value 'Rua'
                street_name = 'Rua ' + street_name
            ##print 'Name after : ', street_name
    return street_name

def audit_comma_present(streets_with_comma, street_name):
    # Search street_name, looking for commas 
    m = commas_present_re.search(street_name)
    
    if m:
        if streets_with_comma != None:
            streets_with_comma.append(street_name)
            
        # remove the content after the comma    
        street_name = commas_present_re.search(street_name).group(1)
        
        return street_name
        

def is_street_name(elem):
    return (elem.attrib['k'] == 'addr:street')


def audit(osmfile):
    osm_file = open(osmfile, 'r')
    street_types = defaultdict(set)
    streets_with_comma = []
    for event, elem in ET.iterparse(osm_file, events=('start',)):

        if elem.tag == 'node' or elem.tag == 'way':
            for tag in elem.iter('tag'):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
                    audit_comma_present(streets_with_comma, tag.attrib['v'])
    osm_file.close()
    return street_types, streets_with_comma


def update_name(name, mapping):

    m = street_type_re.search(name)
    street_type = m.group()
    new_road_name = mapping[street_type]
    name = street_type_re.sub(new_road_name, name)

    return name


if __name__ == '__main__':
    st_types, st_comma = audit('rio-sample.osm')
    print 'Commas present:'
    pprint.pprint(st_comma)
    print '\nType issues:'
    pprint.pprint(dict(st_types))
