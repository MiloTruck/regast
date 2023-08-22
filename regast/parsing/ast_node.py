import tree_sitter
from typing import List, Optional


class ASTNode:
    def __init__(self, fname: str):
        self._fname: str = fname
        self._tree_sitter_node: Optional[tree_sitter.Node] = None
        
        self.start_line = self.end_line = self.start_column = self.end_column = None
        self._children: List[ASTNode] = []
        self._children_types: List[str] = []
        self._comments: List[ASTNode] = []
        self._errors: List[ASTNode] = []

    @staticmethod
    def from_tree_sitter_node(fname: str, node: tree_sitter.Node) -> 'ASTNode':
        ast_node = ASTNode(fname)
        ast_node._tree_sitter_node = node
        ast_node.start_line, ast_node.start_column = node.start_point
        ast_node.end_line, ast_node.end_column = node.end_point
        
        for child_node in node.children:
            child_ast_node = ASTNode.from_tree_sitter_node(fname, child_node)
            match child_node.type:
                case 'comment':
                    ast_node._comments.append(child_ast_node)
                case 'ERROR':
                    ast_node._errors.append(child_ast_node)
                case other:
                    ast_node._children_types.append(other)
                    ast_node._children.append(child_ast_node)
        
        return ast_node

    @property
    def fname(self) -> str:
        return self._fname

    @property
    def tree_sitter_node(self) -> Optional[tree_sitter.Node]:
        return self._tree_sitter_node

    @property
    def type(self) -> str:
        return self._tree_sitter_node.type

    @property
    def text(self) -> str:
        return self._tree_sitter_node.text.decode()
    
    @property
    def comments(self) -> List["ASTNode"]:
        return list(self._comments)

    @property
    def errors(self) -> List["ASTNode"]:
        return list(self._errors)

    @property
    def children(self) -> List["ASTNode"]:
        return list(self._children)

    @property
    def children_types(self) -> List[str]:
        return list(self._children_types)
    
    def is_ancestor_of(self, node: tree_sitter.Node) -> bool:
        """
        Check if this node is an ancestor of node  
        """
        start_point_is_before = (
            self.start_line < node.start_line or
            self.start_line == node.start_line and
            self.start_column <= node.start_column
        )
        
        end_point_is_after = (
            self.end_line > node.end_line or
            self.end_line == node.end_line and
            self.end_column >= node.end_column
        )

        return start_point_is_before and end_point_is_after
    
    def is_descendant_of(self, node: tree_sitter.Node) -> bool:
        """
        Check if this node is a descendant of node 
        """
        return node.is_ancestor_of(self)