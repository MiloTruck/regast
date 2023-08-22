from regast.core.core import Core
from regast.parsing.ast_node import ASTNode

class Comment(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

    @property
    def text(self) -> str:
        return self.ast_node.text
    
    def __str__(self):
        return self.text()