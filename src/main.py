import argparse
import json

DATA_TYPES_PROPERTIES = {
    "object": [
        ("description", str, False),
        ("properties", dict, True),
        ("required", list, False),
    ],
    "string": [("description", str), ("values", list)],
    "number": [("minimum", int), ("maximum", int)],
    "array": [("items", dict)],
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


def convert_type(data: any):
    if type(data) == dict:
        return "object"
    elif type(data) == str:
        return "string"
    elif type(data) == int or type(data) == float:
        return "number"
    elif type(data) == list:
        return "array"
    else:
        raise JSONSchemaValidationError(
            f"Data type {data} does not found. Please use one of the following types: `dict`, `str`, `int`, `float`, `list`."
        )


def validate_object(data: dict):
    keys = data.keys()
    data_type = convert_type(data)
    data_type_properties = DATA_TYPES_PROPERTIES[data_type]

    for name, type_exp, required in data_type_properties:
        if name in keys:
            value = data[name]

            if type_exp != type(value):
                raise JSONSchemaValidationError(
                    f"Data type expected for property `{name}` was {type_exp} but received {type(value)}."
                )

        else:
            if required:
                raise JSONSchemaValidationError(f"Required Key `{name}` not found.")


def validate_header(data: dict):
    keys = data.keys()

    if "type" not in keys or data["type"] != "object":
        raise JSONSchemaValidationError(f"Header type should be object not {data.type}")
    
    validate_object(data)


def validate_json_data(data: dict):
    validate_header(data)


if __name__ == "__main__":
    args = parse_args()
    print(args.file_path)

    json_data = load_file(args.file_path)
    print(json_data)

    validate_json_data(json_data)
