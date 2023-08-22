from enum import Enum
from typing import Optional, Union

from regast.core.expressions.expression import Expression
from regast.exceptions import RegastException
from regast.parsing.ast_node import ASTNode
from regast.utilities.math import convert_string_to_fraction, convert_subdenomination

class LiteralType(Enum):
    BOOLEAN = 0
    NUMBER = 1
    HEX_STRING = 2
    STRING = 3

    @staticmethod
    def literal_type_from_node_type(node_type: str) -> "LiteralType":
        match node_type:
            case 'number_literal': return LiteralType.NUMBER
            case 'boolean_literal': return LiteralType.BOOLEAN
            case 'hex_string_literal': return LiteralType.HEX_STRING
            case 'string_literal' | 'unicode_string_literal': return LiteralType.STRING
        
        raise RegastException(f'Unknown tree-sitter node type for LiteralType: {node_type}')
        

class Literal(Expression):
    def __init__(self, node: ASTNode):
        """
        Using "2 ether" as an example:
        - declared_value = "2"
        - literal_type = LiteralType.NUMBER
        - unit = "ether"
        - value = 2000000000000000000
        """

        super().__init__(node)

        self._literal_type: LiteralType = None
        self._declared_value: str = None
        self._unit: Optional[str] = None

    @property
    def type(self) -> LiteralType:
        return self._literal_type

    @property
    def declared_value(self) -> str:
        return self._declared_value

    @property
    def unit(self) -> Optional[str]:
        return self._unit

    @property
    def value(self) -> Union[str, bool , int]:
        if self.type == LiteralType.STRING:
            return self._declared_value
        elif self.type == LiteralType.BOOLEAN:
            return self._declared_value == "true"
        
        v = self._declared_value
        if self.type == LiteralType.HEX_STRING:
            v = '0x' + self._declared_value.strip('hex').replace('\'', '').replace('\"', '')

        if self._unit:
            return convert_subdenomination(v, self._unit)
        
        return int(convert_string_to_fraction(v))

    def __str__(self):
        s = self._declared_value 
        if self._unit:
            s += " " + self._unit
        return s

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        elif isinstance(other, bool) and self.type == LiteralType.BOOLEAN:
            return self.value == other
        elif isinstance(other, int) and self.type in [LiteralType.NUMBER, LiteralType.HEX]:
            return self.value == other 
        elif isinstance(other, Literal):
            return self.value == other.value
        return False




    