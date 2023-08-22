from typing import List
import regast.parsing.tree_sitter.expressions as expressions
import regast.parsing.tree_sitter.helper as helper
import regast.parsing.tree_sitter.types as types
from regast.core.common import Visibility
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.error_parameter import ErrorParameter
from regast.core.variables.event_parameter import EventParameter
from regast.core.variables.function_type_variable import FunctionTypeVariable
from regast.core.variables.parameter import Parameter
from regast.core.variables.state_variable import StateVariable, StateVariableMutability
from regast.core.variables.struct_member import StructMember
from regast.core.variables.variable import DataLocation
from regast.exceptions import ParsingException
from regast.parsing.ast_node import ASTNode
from regast.core.variables.constant import Constant


class VariableParser:
    @staticmethod
    def parse_constant_variable_declaration(node) -> Constant:
        assert node.type == 'constant_variable_declaration'

        type_name, constant_token, name, equals_token, value = node.children
        assert constant_token.type == 'constant' and equals_token.type == '='
        assert type_name.type == 'type_name' and name.type == 'identifier'
        
        constant = Constant(node)
        constant._type = types.TypeParser.parse_type_name(type_name)
        constant._name = expressions.ExpressionParser.parse_identifier(name)
        constant._expression = expressions.ExpressionParser.parse_expression(value)

        return constant
    
    @staticmethod
    def parse_error_parameter(node) -> ErrorParameter:
        assert node.type == 'error_parameter'

        type_name = name = None
        match node.children_types:
            case ['type_name']:
                type_name, = node.children
            case ['type_name', 'identifier']:
                type_name, name = node.children
            case _:
                raise ParsingException(f'Unable to parse error_paramter: {node.text}')

        error_parameter = ErrorParameter(node)
        error_parameter._type = types.TypeParser.parse_type_name(type_name)
        if name:
            error_parameter._name = expressions.ExpressionParser.parse_identifier(name)

        return error_parameter
    
    @staticmethod
    def parse_event_parameter(node) -> EventParameter:
        assert node.type == 'event_paramater'
        
        event_parameter = EventParameter(node)

        type_name = name = None
        match node.children_types:
            case ['type_name']:
                type_name, = node.children
            case ['type_name', 'indexed']:
                type_name, _ = node.children
                event_parameter._indexed = True
            case ['type_name', 'identifier']:
                type_name, name = node.children
            case ['type_name', 'indexed', 'identifier']:
                type_name, _, name = node.children
                event_parameter._indexed = True
            case _:
                raise ParsingException(f'Unable to parse error_paramter: {node.text}')

        event_parameter._type = types.TypeParser.parse_type_name(type_name)
        if name:
            event_parameter._name = expressions.ExpressionParser.parse_identifier(name)

        return event_parameter
    
    @staticmethod
    def parse_function_type_variable(node) -> FunctionTypeVariable:
        assert node.type == 'return_parameter'

        function_type_variable = FunctionTypeVariable(node)

        type_name = None
        match node.children_types:
            case ['type_name']:
                type_name, = node.children
            case ['type_name', ('memory' | 'storage' | 'calldata')]:
                type_name, location = node.children
                function_type_variable._data_location = DataLocation(location.text)
            case _:
                raise ParsingException(f'Unable to parse function type variable: {node.text}')

        function_type_variable._type = types.TypeParser.parse_type_name(type_name)

        return function_type_variable

    @staticmethod
    def convert_parameter_to_function_type_variable(parameter: Parameter) -> FunctionTypeVariable:
        assert isinstance(parameter, Parameter)

        function_type_variable = FunctionTypeVariable(parameter.ast_node)
        function_type_variable._type = parameter.type
        function_type_variable._data_location = parameter._data_location
        function_type_variable._name = parameter.name

        return function_type_variable

    @staticmethod
    def parse_parameter(node) -> Parameter:
        assert node.type == 'parameter'
        
        type_name = location = name = None
        match node.children_types:
            case ['type_name']:
                type_name, = node.children
            case ['type_name', ('memory' | 'storage' | 'calldata')]:
                type_name, location = node.children
            case ['type_name', 'identifier']:
                type_name, name = node.children
            case ['type_name', ('memory' | 'storage' | 'calldata'), 'identifier']:
                type_name, location, name = node.children
            case _:
                raise ParsingException(f'Unable to parse parameter: {node.text}')

        parameter = Parameter(node)
        parameter._type = types.TypeParser.parse_type_name(type_name)

        if location:
            parameter._data_location = DataLocation(location.text)
        if name:
            parameter._name = expressions.ExpressionParser.parse_identifier(name)

        return parameter

    @staticmethod
    def parse_override_specifier(node: ASTNode) -> List[UserDefinedType]:
        assert node.type == 'override_specifier'

        user_defined_types, [override_token] = helper.extract_nodes_between_brackets(
            node, '(', ')',
            node_type='user_defined_type',
            parsing_function=types.TypeParser.parse_user_defined_type
        )
        assert override_token.type == 'override'
        
        return user_defined_types

    @staticmethod
    def parse_state_variable_declaration(node) -> StateVariable:
        assert node.type == 'state_variable_declaration'

        state_variable = StateVariable(node)

        type_name = name = None
        remaining_nodes = []
        match node.children_types:
            case ['type_name', *_, 'identifier', '=', _]:
                type_name, *remaining_nodes, name, _, expression = node.children
                state_variable._expression = expressions.ExpressionParser.parse_expression(expression)
            case ['type_name', *_, 'identifier']:
                type_name, *remaining_nodes, name = node.children
            case _:
                raise ParsingException(f'Unable to parse state_variable_declaration {node.text}')

        state_variable._type = types.TypeParser.parse_type_name(type_name)
        state_variable._name = expressions.ExpressionParser.parse_identifier(name)

        for child_node in remaining_nodes:
            match child_node.type:
                case 'visibility':
                    assert not state_variable.declared_visibility
                    state_variable._visibility = Visibility(child_node.text)
                case 'constant' | 'immutable':
                    assert not state_variable.declared_mutability
                    state_variable._mutability = StateVariableMutability(child_node.text)
                case 'override_specifier':
                    assert not state_variable.overrides
                    state_variable._override = True
                    state_variable._overrides = VariableParser.parse_override_specifier(child_node)
                case other:
                    raise ParsingException(f'Unknown tree-sitter node type for state_variable_declaration: {other}')

        return state_variable

    @staticmethod
    def parse_struct_member(node) -> StructMember:
        assert node.type == 'struct_member'

        type_name, name = node.children
        assert type_name.type == 'type_name' and name.type == 'identifier'

        struct_member = StructMember(node)
        struct_member._type = types.TypeParser.parse_type_name(type_name)
        struct_member._name = expressions.ExpressionParser.parse_identifier(name)

        return struct_member
        