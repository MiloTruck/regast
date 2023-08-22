from typing import List, Dict, Optional, Union

from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.parsing.ast_node import ASTNode

class Import(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._import_path: str = None
        self._alias: Optional[Identifier] = None
        self._imported: List[Identifier] = []
        self._renaming: Dict[Identifier, Identifier] = {}

    @property
    def import_path(self) -> str:
        return self._import_path

    @property
    def imported_objects(self) -> List[Identifier]:
        return list(self._imported)

    @property
    def alias(self) -> Optional[Identifier]:
        return self._alias

    @property
    def renaming(self) -> Dict[Identifier, Identifier]:
        return dict(self._renaming)

    @property
    def imported_object_to_alias(self, imported_object: Union[str, Identifier]) -> Optional[Identifier]:
        if imported_object in self._renaming:
            return self._renaming[imported_object]

    @property
    def children(self) -> List:
        children = self.imported_objects + list(self.renaming.values())
        if self.alias:
            children.append(self.alias)
        return children
            
    def __eq__(self, other):
        if isinstance(other, Import):
            return self.import_path == other.import_path and self.imported_objects == other.imported_objects and self.alias == other.alias and self.renaming == other.renaming
        return False