This README file, presents the files used to run audit and cleaning on Brazilian cities:

- audit_streets.py          - This file is used to do the real audit and cleaning. Street names are adjusted and commas are removed from street names.
- generate_sample_file.py   - This file is used to create a sample from the original OSM file.
- write_json.py             - This is the main file which users may run to audit and create the JSON file, to be imported on MongoDB.

Example: 

daniel $ python write_json.py
*** Writing JSON file...
Input file size:  9MB
Output file size: 10MB

