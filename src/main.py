import argparse
import json
from typing import Union

DATA_TYPES_PROPERTIES = {
    "object": [
        ("description", str, False),
        ("properties", dict, True),
        ("required", list, False),
    ],
    "string": [("type", str), ("description", str), ("values", list)],
    "number": [("type", str), ("minimum", int), ("maximum", int), ("values", list)],
    "integer": [("type", str), ("minimum", int), ("maximum", int), ("values", list)],
    "array": [("type", str, True), ("items", dict, True)],
}


class JSONSchemaValidationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    return parser.parse_args()


def load_file(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)


def convert_type(data: Union[dict, list]):
    if type(data) == dict:
        d_type = data["type"]

        if d_type in ["object", "string", "integer", "number", "array"]:
            return d_type
        else:
            raise JSONSchemaValidationError(
                f"Data type `{d_type}` does not found. Please use one of the following types: `dict`, `str`, `int`, `float`, `array`."
            )
    elif type(data) == list:
        return "array"
    else:
        raise JSONSchemaValidationError(
            f"Data type {data} does not found. Please use one of the following types: `dict`, `str`, `int`, `float`, `array`."
        )


def validate_object(data: dict, keys: list, data_type_properties: list):
    for name, type_exp, required in data_type_properties:
        if name in keys:
            value = data[name]

            if type_exp != type(value):
                raise JSONSchemaValidationError(
                    f"Data type expected for property `{name}` was {type_exp} but received {type(value)}."
                )
        else:
            if required:
                raise JSONSchemaValidationError(
                    f"Required Key `{name}` not found for type `{type_exp}`."
                )
    
    # Validate children
    if data['type'] == 'array' and (data['items'] == 'array' or data['items'] == 'object'):
        validate_children(data)

# TODO: Continues here
def validate_children(data: dict):
    has_child = True

    while has_child:
        if data['items'] == 'array':
            pass
        elif data['items'] == 'object':
            pass
        else:



def validate_data_type_object(prop_name: str, keys: list, data_type_properties: list):
    for k in keys:
        c = [(type, clazz) for type, clazz in data_type_properties if type == k]
        if len(c) <= 0:
            raise JSONSchemaValidationError(
                f"Constraint `{k}` not allowed for property `{prop_name}`."
            )


def validate(prop_name: str, prop_data: dict):
    keys = prop_data.keys()
    data_type = convert_type(prop_data)
    data_type_properties = DATA_TYPES_PROPERTIES[data_type]

    if data_type in ["object", "array"]:
        return validate_object(prop_data, keys, data_type_properties)
    elif data_type in ["string", "integer", "number"]:
        return validate_data_type_object(prop_name, keys, data_type_properties)
    else:
        raise JSONSchemaValidationError(
            f"Data Type `{data_type}` not supported for property {prop_name}."
        )


def validate_header(data: dict):
    keys = data.keys()

    if "type" not in keys or data["type"] != "object":
        raise JSONSchemaValidationError(f"Header type should be object not {data.type}")

    validate("Header", data)


def validate_property(prop_name: str, prop_data: dict):
    validate(prop_name, prop_data)


def validate_json_data(data: dict):
    validate_header(data)

    for prop_name in data["properties"]:
        prop_data = data["properties"][prop_name]
        print(prop_name, prop_data)

        validate_property(prop_name, prop_data)


if __name__ == "__main__":
    args = parse_args()
    print(args.file_path)

    json_data = load_file(args.file_path)
    print(json_data)

    validate_json_data(json_data)
