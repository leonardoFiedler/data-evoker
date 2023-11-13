import json

class JSONSchemaValidationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class DataEvoker:
    def __init__(
        self,
        schema: str,
        count: int = 1,
    ) -> None:
        """ Data Evoker class. Generates sample data based on a valid schema.

        Args:
            schema (str): Schema str that should generate data
            count (int, optional): number of samples to generate. Defaults to 1.            
        """
        self.__schema = json.loads(schema.lower())
        self.__count = count
    
    def is_schema_valid(self):
        print("Validating Schema")
        self.validate_header()
        
        return True
    
    def generate_samples(self):
        print("Generating Samples")
        pass
    
    def run(self):
        self.is_schema_valid()
        self.generate_samples()
    
    def validate_child_object(self, child_elems: list):
        for ce in child_elems:
            keys = ce.keys()
            
            if "type" not in keys or self.__schema["type"] != "object":
                raise JSONSchemaValidationError(f"Schema should have `type` property and it must be `object`")
    
    def validate_required_props(self, element: dict, element_name: str):
        if "type" not in element.keys():
            raise JSONSchemaValidationError(f"{element_name} should have `type`")
    
    # TODO: continu validate header and required props
    def validate_header(self):
        keys = self.__schema.keys()

        self.validate_required_props(self.__schema, "root")
        
        if "properties" not in keys:
            raise JSONSchemaValidationError(f"`Properties` must be passed")

        
