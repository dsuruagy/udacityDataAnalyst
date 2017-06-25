#!/usr/bin/env python
# -*- coding: utf-8 -*-
from write_json import process_map

OSMFILE  = 'rio-de-janeiro_brazil.osm'


if __name__ == "__main__":
    
    print '*** Writing JSON file...'
    data = process_map(OSMFILE, False)

