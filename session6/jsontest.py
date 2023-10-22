import json
v = '{"name": "roopesh", "age": 30}'
print(type(v))

# convert string to python object
python_obj = json.loads(v)
print(type(python_obj))
print(python_obj["name"])

# convert python object to json string
json_string = json.dumps(python_obj)
print(type(json_string))
print(json_string["name"])

b = {"name": "Nikhita", "dateofbirth": "30-oct-2005"}
