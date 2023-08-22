import os
from tree_sitter import Language

from regast.utilities.definitions import PACKAGE_DIR, TREE_SITTER_SOLIDITY_LIBRARY_PATH

def setup_treesitter():
    tree_sitter_solidity_path = os.path.join(PACKAGE_DIR, 'third_party', 'tree-sitter-solidity')
    
    if not os.path.exists(TREE_SITTER_SOLIDITY_LIBRARY_PATH):
        Language.build_library(TREE_SITTER_SOLIDITY_LIBRARY_PATH, [tree_sitter_solidity_path])

def initialize_dependencies():
    setup_treesitter()