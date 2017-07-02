#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

postcode_re = re.compile(r'^[0-9]{5}-[0-9]{3}$')

def audit_postcode(postcode_value):
    return audit_code(None, postcode_value)

def audit_code(incorrect_postcodes, postcode_value):
    # audit if postcode starts with a five digits, a '-' and 3 digits, defined in regex
    m = postcode_re.search(postcode_value)
    new_postcode = None
    
    # If the postcode pattern does not apply to this value
    if not m:
        if incorrect_postcodes != None:
            incorrect_postcodes.append(postcode_value)

        #Remove non numeric characters
        postcode_value = re.sub(r'\D','',postcode_value)
                
        # Verify if the postcode is a number
        if int(postcode_value):
            while len(postcode_value) < 8:
                # complete code with zeroes until the correct length
                postcode_value = postcode_value + '0'
            
            # Convert to the correct pattern    
            new_postcode = postcode_value[0:5] + '-' + postcode_value[5:8]

        postcode_value = new_postcode

    return postcode_value
        

def is_postcode(elem):
    return (elem.attrib['k'] == 'addr:postcode')


def audit(osmfile):
    osm_file = open(osmfile, 'r')
    incorrect_postcodes = []
    
    for event, elem in ET.iterparse(osm_file, events=('start',)):

        if elem.tag == 'node' or elem.tag == 'way':
            for tag in elem.iter('tag'):
                if is_postcode(tag):
                    audit_code(incorrect_postcodes, tag.attrib['v'])
    osm_file.close()
    return incorrect_postcodes

if __name__ == '__main__':
    incorrect_postcodes = audit('rio-de-janeiro_brazil.osm')
    
    print 'Incorrect postcodes:'
    pprint.pprint(incorrect_postcodes)

