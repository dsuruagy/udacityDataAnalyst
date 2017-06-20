#!/usr/bin/env python
# -*- coding: utf-8 -*-
from write_json import process_map
import pprint

if __name__ == "__main__":
    data = process_map('rio-sample.osm', True)
    pprint.pprint(data[0])
