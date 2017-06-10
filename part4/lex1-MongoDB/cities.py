import csv
from datetime import datetime

FIELDS = {
	'URI' : 'URI',
	'elevation' : 'elevation',
	'name' : 'name',
	'point' : 'point',
	'populationTotal' : 'population',
	'utcOffset' : 'utcOffset', 
	'country_label' : 'country',
	'isPartOf_label' : 'isPartOf',
	'timeZone_label' : 'timeZone',
	'postalCode' : 'postalCode',
	'foundingDate' : 'foundingDate',
	'wgs84_pos#lat' : 'lat',
	'wgs84_pos#long' : 'lon'

	}

def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return v

def parse_array2(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return (True, v_array)
    return (False, v)

def ensure_not_array(v):
    (is_array, v) = parse_array2(v)
    if is_array:
        return v[0]
    return v

def ensure_array(v):
    (is_array, v) = parse_array2(v)
    if is_array:
        return v
    return [v]

def ensure_float(v):
    if is_number(v):
        return float(v)

def ensure_int(v):
    if is_number(v):
        return int(v)

def empty_val(val):
    val = val.strip()
    return (val == "NULL") or (val == "")

def process_cities_file(input_file):
	input_data = csv.DictReader(open(input_file))
    #pprint.pprint(input_data.fieldnames)

	keys = FIELDS.keys()
	cities = []
	skip_lines(input_data, 3)
	for row in input_data:
		city = {}

		for field, val in row.iteritems():
			if not field in keys:
				continue
			else:
				field = FIELDS[field]
		
			if empty_val(val):
				continue
			if field in ["foundingDate"] and "{" not in val:
                #doc["foundingDate"] = datetime.strptime(doc["foundingDate"], "%Y-%m-%d")
                #city["foundingDate"] = datetime.strptime(val, "%Y-%m-%d")
				val = datetime.strptime(val, "%Y-%m-%d")

			elif field in ['elevation', 'population', 'lat', 'lon']:
				if val.startswith('{'):
					val = parse_array(val)
					val = max([ensure_float(v) for v in val])
				else:
					val = ensure_float(val)
			else:
				val = val.strip()
				val = parse_array(val)

			city[field] = val
		cities.append(city)
	return cities

