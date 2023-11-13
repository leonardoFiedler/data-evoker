import pytest
from data_evoker.data_evoker import DataEvoker, JSONSchemaValidationError


def test_invalid_header_type():
    with pytest.raises(JSONSchemaValidationError) as e_info:
        de = DataEvoker("""
        {
            "type": "array",
            "properties": {
                "first_name": { "type": "string" },
                "last_name": { "type": "string" },
                "age": { "type": "integer" }
            }
        }
        """, 1)
        
        de.validate_header()

def test_missing_header_property():
    with pytest.raises(JSONSchemaValidationError) as e_info:
        de = DataEvoker("""
        {
            "properties": {
                "first_name": { "type": "string" },
                "last_name": { "type": "string" },
                "age": { "type": "integer" }
            }
        }
        """, 1)
        
        de.validate_header()

def test_missing_properties():
    with pytest.raises(JSONSchemaValidationError) as e_info:
        de = DataEvoker("""
        {
            "type": "object"
        }
        """, 1)
        
        de.validate_header()

def test_property_missing_type():
    with pytest.raises(JSONSchemaValidationError) as e_info:
        de = DataEvoker("""
        {
            "properties": {
                "first_name": { "description": "xablau" },
                "last_name": { "type": "string" },
                "age": { "type": "integer" }
            }
        }
        """, 1)
        
        de.validate_header()