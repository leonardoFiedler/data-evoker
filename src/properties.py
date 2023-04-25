from enum import Enum

MINIMUM_VALUE = -999999999
MAXIMUM_VALUE = 999999999


class ETypeData(Enum):
    OBJECT = ("OBJECT",)
    STRING = ("STRING",)
    INTEGER = ("INTEGER",)
    NUMBER = ("NUMBER",)
    ARRAY = "ARRAY"


class ObjectType(object):
    def __init__(self, props: list, required: list = []) -> None:
        self.__props = props
        self.__required = required


class BaseProperty(object):
    def __init__(self, name: str, type: ETypeData, values: list = []) -> None:
        self.__name = name
        self.__type = type
        self.__values = values


class StringProperty(BaseProperty):
    def __init__(self, name: str, values: list = []) -> None:
        super().__init__(name, values, ETypeData.STRING)


class NumberProperty(BaseProperty):
    def __init__(
        self,
        name: str,
        type: ETypeData,
        values: list = [],
        minimum: int = MINIMUM_VALUE,
        maximum: int = MAXIMUM_VALUE,
    ) -> None:
        super().__init__(name, values, type)
        self.__minimum = minimum
        self.__maximum = maximum
