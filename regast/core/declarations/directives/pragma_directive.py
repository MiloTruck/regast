from typing import List, Union
from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.parsing.ast_node import ASTNode

class Pragma(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)
        
        self._name: Union[Identifier, str] = None
        self._value: str = None

    @property
    def name(self) -> Union[Identifier, str]:
        return self._name
    
    @property
    def value(self) -> str:
        return self._value

    @property
    def version(self) -> str:
        return self.value

    @property
    def is_solidity_version(self) -> bool:
        return self.name == "solidity"

    @property
    def is_abi_encoder_v2(self) -> bool:
        return self.name == "experimental" and self.value == "ABIEncoderV2"

    @property
    def children(self) -> List:
        return [self.name] if isinstance(self.name, Identifier) else []

    def __eq__(self, other):
        if isinstance(other, Pragma):
            return self.name == other.name and self.value == other.value
        return False