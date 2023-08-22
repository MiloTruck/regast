
from typing import Callable, List, Optional, Tuple
from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments
from regast.core.variables.parameter import Parameter
from regast.exceptions import ParsingException
from regast.parsing.ast_node import ASTNode
import regast.parsing.tree_sitter.expressions as expressions
import regast.parsing.tree_sitter.variables as variables

def extract_nodes_between_brackets(
    node: ASTNode,
    open_bracket: str,
    close_bracket: str,
    comma_separated: bool = True,
    node_type: Optional[str] = None,
    parsing_function: Optional[Callable] = None,
) -> Tuple[List[ASTNode], List[ASTNode]]:
    """
    Iterate through child nodes of `node` and parse child nodes of `node_type` between `open_bracket` and `close_bracket`.
    """
    try:
        open_bracket_index = node.children_types.index(open_bracket)
        close_bracket_index = node.children_types.index(close_bracket)
    except ValueError:
        return [], node.children

    between_nodes = node.children[open_bracket_index:close_bracket_index+1]
    remaining_nodes = node.children[:open_bracket_index] + node.children[close_bracket_index+1:]

    parsed_nodes = []
    for child_node in between_nodes:
        if child_node.type in [open_bracket, close_bracket] or comma_separated and child_node.type == ',':
            continue

        if node_type and child_node.type != node_type:
            ParsingException(f'Unknown tree-sitter node type while parsing {node.type}: {child_node.type}')

        parsed_node = parsing_function(child_node) if parsing_function else child_node
        parsed_nodes.append(parsed_node)

    return parsed_nodes, remaining_nodes

def extract_call_arguments(node: ASTNode) -> Tuple[List[ASTNode], List[Expression], Optional[StructArguments]]:
    call_argument_nodes, remaining_nodes = extract_nodes_between_brackets(
        node, '(', ')',
        node_type='call_argument',
    )

    arguments = []
    struct_arguments = None

    for node in call_argument_nodes:
        call_argument = expressions.ExpressionParser.parse_call_argument(node)
        
        match call_argument:
            case Expression():
                arguments.append(call_argument)
            case StructArguments():
                assert not struct_arguments
                struct_arguments = call_argument
            case _:
                raise ParsingException(f'Unknown resulting argument from call_argument: {node.text}')

    return arguments, struct_arguments, remaining_nodes

def extract_parameters(node: ASTNode) -> Tuple[List[ASTNode], List[Parameter]]:
    return extract_nodes_between_brackets(
        node, '(', ')',
        node_type='parameter',
        parsing_function=variables.VariableParser.parse_parameter
    )