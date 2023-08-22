import regast.parsing.tree_sitter.expressions as expressions
import regast.parsing.tree_sitter.variables as variables
from regast.core.common import StateMutability, Visibility
from regast.core.types.array_type import ArrayType
from regast.core.types.function_type import FunctionType
from regast.core.types.mapping_type import MappingType
from regast.core.types.elementary_type import ElementaryType, ElementaryTypeName, NonElementaryType
from regast.core.types.type import Type
from regast.core.types.user_defined_type import UserDefinedType
from regast.exceptions import ParsingException


class TypeParser:
    @staticmethod
    def parse_type_name(node) -> Type:
        assert node.type == 'type_name'

        match node.children_types:
            case ['primitive_type']:
                return TypeParser.parse_primitive_type(node.children[0])
            case ['user_defined_type']:
                return TypeParser.parse_user_defined_type(node.children[0])
            case ['mapping', *_]:
                return TypeParser.parse_mapping(node)
            case ['type_name', *_]:
                return TypeParser.parse_array_type(node)
            case ['function', *_]:
                return TypeParser.parse_function_type(node)
        
        raise ParsingException(f'Unknown tree-sitter node type for type_name: {node.text}')
    
    @staticmethod
    def parse_primitive_type(node) -> ElementaryType:
        assert node.type == 'primitive_type'

        elementary_type = ElementaryType(node)
        match node.children_types:
            case ['address', 'payable']:
                elementary_type._type = 'address'
                elementary_type._payable = True
            case [t]:
                if t not in ElementaryTypeName:
                    raise NonElementaryType(f"Failed to parse ElementaryType: {t}")
            
                if t == "uint":
                    t = "uint256"
                elif t == "int":
                    t = "int256"
                elif t == "byte":
                    t = "bytes1"

                elementary_type._type = t

        return elementary_type

    @staticmethod
    def parse_user_defined_type(node) -> UserDefinedType:
        assert node.type in ['user_defined_type', 'type_alias']

        user_defined_type = UserDefinedType(node)
        for child_node in node.children:
            match child_node.type:
                case 'identifier':
                    identifier = expressions.ExpressionParser.parse_identifier(child_node)
                    user_defined_type._identifiers.append(identifier)
                case '.':
                    pass
                case _:
                    raise ParsingException(f'Unknown tree-sitter node type in user_defined_type {node.type}')

        return user_defined_type

    @staticmethod
    def parse_mapping(node) -> MappingType:
        assert node.type == 'type_name'

        mapping_token, open_bracket_token, key, arrow_token, value, close_bracket_token = node.children
        assert (
            mapping_token.type == 'mapping' and
            open_bracket_token.type == '(' and
            arrow_token.type == '=>' and
            close_bracket_token.type == ')'
        )
        assert value.type == 'type_name'

        mapping_type = MappingType(node)
        mapping_type._value_type = TypeParser.parse_type_name(value)

        match key.type:
            case 'primitive_type':
                mapping_type._key_type = TypeParser.parse_primitive_type(key)
            case 'user_defined_type':
                mapping_type._key_type = TypeParser.parse_user_defined_type(key)
            case other:
                raise ParsingException(f'Unknown tree-sitter node type for mapping key: {other}')

        return mapping_type
    
    @staticmethod
    def parse_array_type(node) -> ArrayType:
        assert node.type == 'type_name'
        
        type_name = expression = None
        match node.children_types:
            case ['type_name', '[', ']']:
                type_name, _, _ = node.children
            case ['type_name', '[', _, ']']:
                type_name, _, expression, _ = node.children
            case _:
                raise ParsingException(f'Unable to parse array type: {node.text}')

        array_type = ArrayType(node)
        array_type._type = TypeParser.parse_type_name(type_name)

        if expression:
            array_type._expression = expressions.ExpressionParser.parse_expression(expression) 

        return array_type
    
    @staticmethod
    def parse_function_type(node) -> FunctionType:
        assert node.type == 'type_name'

        function_type = FunctionType(node)
        for child_node in node.children:
            match child_node.type:
                case 'parameter':
                    parameter = variables.VariableParser.parse_parameter(child_node)
                    function_type_variable = variables.VariableParser.convert_parameter_to_function_type_variable(parameter)
                    function_type._parameters.append(function_type_variable)
                    
                case 'return_parameter':
                    return_parameter = variables.VariableParser.parse_function_type_variable(child_node)
                    function_type._return_parameters.append(return_parameter)
                    
                case 'visibility':
                    assert not function_type.visibility
                    function_type._visibility = Visibility(child_node.text)

                case 'state_mutability':
                    assert not function_type.mutability
                    function._mutability = StateMutability(child_node.text)

                case 'function' | 'returns' | '(' | ')' | ',':
                    pass

                case other:
                    raise ParsingException(f'Unknown tree-sitter node type in function type: {other}')

        return function_type



