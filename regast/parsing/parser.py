import tree_sitter as ts

from regast.exceptions import ParsingException
from regast.parsing.tree_sitter.declarations import DeclarationParser
from regast.parsing.ast_node import ASTNode
from regast.utilities.definitions import TREE_SITTER_SOLIDITY_LIBRARY_PATH


class Parser:
    def __init__(self):
        # Initialize parser
        solidity_language = ts.Language(TREE_SITTER_SOLIDITY_LIBRARY_PATH, 'solidity')
        parser = ts.Parser()
        parser.set_language(solidity_language)

        self.parser = parser

    def parse(self, fname: str):
        with open(fname, 'rb') as f:
            data = f.read()

        try:
            tree_sitter_tree = self.parser.parse(data)
        except Exception as e:
            raise ParsingException(f"Failed to parse {fname}, throws: {e}")

        root_node = ASTNode.from_tree_sitter_node(fname, tree_sitter_tree.root_node)
        source_unit = DeclarationParser.parse_source_unit(root_node, fname)

        return source_unit