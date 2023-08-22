from typing import Dict, List

from regast.parsing.ast_node import ASTNode

class Core:
    def __init__(self, node: ASTNode):
        self.__class__.__hash__ = Core.__hash__

        self._ast_node: ASTNode = node 
        self._core_type_to_instances: Dict[type, Core] = None

    @property
    def ast_node(self) -> ASTNode:
        return self._ast_node

    @property
    def children(self) -> List:
        return []

    def is_ancestor_of(self, core_object: "Core") -> bool:
        return self.ast_node.is_ancestor_of(core_object.ast_node)
    
    def is_descendant_of(self, core_object: "Core") -> bool:
        return self.ast_node.is_descendant_of(core_object.ast_node)

    def get_instances_of(self, core_type: type) -> List["Core"]:
        """
        Get all core objects are of core_type
        """
        return [obj for obj in self._core_type_to_instances[core_type] if self.is_ancestor_of(obj)]

    def __hash__(self):
        return hash(self.ast_node)