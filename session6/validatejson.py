data = '{"name": "roopesh", "age": 30, "ages": 30}'
json_schema = """{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "age": {
            "type": "integer",
            "minimum": 38
        }
    },
    "required": ["name", "age"]
}
"""
import json, jsonschema
jsonschema.validate(json.loads(data), json.loads(json_schema))
