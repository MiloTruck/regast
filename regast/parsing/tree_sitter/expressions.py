from typing import Tuple, Union
from regast.core.expressions.array_access import ArrayAccess
from regast.core.expressions.assignment_operation import AssignmentOperation, AssignmentOperator
from regast.core.expressions.binary_operation import BinaryOperation, BinaryOperator
from regast.core.expressions.call_expression import CallExpression
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.expressions.inline_array_expression import InlineArrayExpression
from regast.core.expressions.literal import Literal, LiteralType
from regast.core.expressions.member_access import MemberAccess
from regast.core.expressions.new_expression import NewExpression
from regast.core.expressions.parenthesized_expression import ParenthesizedExpression
from regast.core.expressions.payable_conversion_expression import PayableConversionExpression
from regast.core.expressions.slice_access import SliceAccess
from regast.core.expressions.struct_expression import StructArguments, StructExpression
from regast.core.expressions.conditional_expression import ConditionalExpression
from regast.core.expressions.tuple_expression import TupleExpression
from regast.core.expressions.type_cast_expression import TypeCastExpression
from regast.core.expressions.type_expression import TypeExpression
from regast.core.expressions.unary_operation import UnaryOperation, UnaryOperator
from regast.core.expressions.update_operation import UpdateOperation, UpdateOperator
from regast.exceptions import ParsingException
from regast.parsing.tree_sitter.helper import extract_call_arguments, extract_nodes_between_brackets
from regast.parsing.tree_sitter.types import TypeParser


class ExpressionParser:
    @staticmethod
    def parse_expression(node) -> Expression:
        match node.type:
            case 'struct_arguments': return ExpressionParser.parse_struct_arguments(node)

            # Regular Expressions
            case 'binary_expression': return ExpressionParser.parse_binary_expression(node)    
            case 'unary_expression': return ExpressionParser.parse_unary_expression(node)
            case 'update_expression': return ExpressionParser.parse_update_expression(node)
            case 'call_expression': return ExpressionParser.parse_call_expression(node)
            case 'payable_conversion_expression': return ExpressionParser.parse_payable_conversion_expression(node)
            case 'meta_type_expression': return ExpressionParser.parse_meta_type_expression(node)
            case 'struct_expression': return ExpressionParser.parse_struct_expression(node)
            case 'ternary_expression': return ExpressionParser.parse_ternary_expression(node)
            case 'type_cast_expression': return ExpressionParser.parse_type_cast_expression(node)    

            # Primary Expressions
            case 'parenthesized_expression': return ExpressionParser.parse_parenthesized_expression(node)
            case 'member_expression': return ExpressionParser.parse_member_expression(node)
            case 'array_access': return ExpressionParser.parse_array_access(node)
            case 'slice_access': return ExpressionParser.parse_slice_access(node)
            case 'primitive_type': return TypeParser.parse_primitive_type(node)
            case 'assignment_expression': return ExpressionParser.parse_assignment_expression(node)
            case 'augmented_assignment_expression': return ExpressionParser.parse_augmented_assignment_expression(node)
            case 'user_defined_type': return TypeParser.parse_user_defined_type(node)
            case 'tuple_expression': return ExpressionParser.parse_tuple_expression(node)
            case 'inline_array_expression': return ExpressionParser.parse_inline_array_expression(node)
            case 'identifier': return ExpressionParser.parse_identifier(node)
            case 'new_expression': return ExpressionParser.parse_new_expression(node)
            
            case 'string_literal' | 'number_literal' | 'boolean_literal' | 'hex_string_literal' | 'unicode_string_literal':
                return ExpressionParser.parse_literal(node)
            
            case other: 
                raise ParsingException(f'Unknown tree-sitter node type for expression: {other}')

    @staticmethod
    def parse_call_argument(node) -> Union[Expression, StructArguments]:
        assert node.type == 'call_argument'

        match node.children_types:
            # expression (normal argument)
            case [_]:
                return ExpressionParser.parse_expression(node.children[0])

            # struct arguments
            case ['{', *_, '}']:
                return ExpressionParser.parse_struct_arguments(node)

            case _:
                raise ParsingException(f'Unable to parse call_argument: {node.text}')

    @staticmethod
    def parse_binary_expression(node) -> BinaryOperation:
        assert node.type == 'binary_expression'

        left, operator, right = node.children

        binary_operation = BinaryOperation(node)
        binary_operation._operator = BinaryOperator(operator.text)
        binary_operation._left_expression = ExpressionParser.parse_expression(left)
        binary_operation._right_expression = ExpressionParser.parse_expression(right)

        return binary_operation

    @staticmethod
    def parse_unary_expression(node) -> UnaryOperation:
        assert node.type == 'unary_expression'

        operator, argument = node.children

        unary_operation = UnaryOperation(node)
        unary_operation._operator = UnaryOperator(operator.text)
        unary_operation._expression = ExpressionParser.parse_expression(argument)

        return unary_operation

    @staticmethod
    def parse_update_expression(node) -> UpdateOperation:
        assert node.type == 'update_expression'

        update_operation = UpdateOperation(node)

        operator = argument = None
        if node.children[0].type in ['++', '--']:
            operator, argument = node.children
            update_operation._prefix = True
        else:
            assert node.children[1].type in ['++', '--']
            argument, operator = node.children

        update_operation._operator = UpdateOperator(operator.text)
        update_operation._expression = ExpressionParser.parse_expression(argument)

        return update_operation

    @staticmethod
    def parse_call_expression(node) -> CallExpression:
        assert node.type == 'call_expression'

        call_expression = CallExpression(node)
        call_expression._arguments, call_expression._struct_arguments, [function] = extract_call_arguments(node)
        call_expression._function_name = ExpressionParser.parse_expression(function)

        return call_expression

    @staticmethod
    def parse_payable_conversion_expression(node) -> PayableConversionExpression:
        assert node.type == 'payable_conversion_expression'

        payable_conversion_expression = PayableConversionExpression(node)
        payable_conversion_expression._arguments, payable_conversion_expression._struct_arguments, [payable_token] = extract_call_arguments(node)
        assert payable_token.type == 'payable'

        return payable_conversion_expression

    @staticmethod
    def parse_meta_type_expression(node) -> TypeExpression:
        assert node.type == 'meta_type_expression'

        type_token, open_bracket_token, type_name, close_bracket_token = node.children
        assert (
            type_token.type == 'type' and
            open_bracket_token.type == '(' and
            close_bracket_token.type == ')'
        )
        
        type_expression = TypeExpression(node)
        type_expression._type = TypeParser.parse_type_name(type_name)

        return type_expression

    @staticmethod
    def parse_call_struct_argument_or_struct_field_assignment(node) -> Tuple[Identifier, Expression]:
        assert node.type in ['call_struct_argument', 'struct_field_assignment']

        name, colon_token, value = node.children
        assert colon_token.type == ':' and name.type == 'identifier'

        field = ExpressionParser.parse_identifier(name)
        argument = ExpressionParser.parse_expression(value)

        return field, argument

    @staticmethod
    def parse_struct_arguments(node) -> StructArguments:
        assert node.type == 'call_argument'

        field_argument_pairs, _ = extract_nodes_between_brackets(
            node, '{', '}',
            node_type='call_struct_argument',
            parsing_function=ExpressionParser.parse_call_struct_argument_or_struct_field_assignment
        )

        struct_arguments = StructArguments(node)
        struct_arguments._field_to_argument = {f: v for f, v in field_argument_pairs}

        return struct_arguments

    @staticmethod
    def parse_struct_expression(node) -> StructExpression:
        assert node.type == 'struct_expression'

        field_argument_pairs, [struct_name] = extract_nodes_between_brackets(
            node, '{', '}',
            node_type='struct_field_assignment',
            parsing_function=ExpressionParser.parse_call_struct_argument_or_struct_field_assignment
        )

        struct_expression = StructExpression(node)
        struct_expression._struct_name = ExpressionParser.parse_expression(struct_name)
        struct_expression._struct_arguments._field_to_argument = {f: v for f, v in field_argument_pairs}

        return struct_expression

    @staticmethod
    def parse_ternary_expression(node) -> ConditionalExpression:
        assert node.type == 'ternary_expression'

        condition, question_mark_token, true_expression, colon_token, false_expression = node.children
        assert question_mark_token.type == '?' and colon_token.type == ':'

        conditional_expression = ConditionalExpression(node)
        conditional_expression._condition = ExpressionParser.parse_expression(condition)
        conditional_expression._true_expression = ExpressionParser.parse_expression(true_expression)
        conditional_expression._false_expression = ExpressionParser.parse_expression(false_expression)

        return conditional_expression

    @staticmethod
    def parse_type_cast_expression(node) -> TypeCastExpression:
        assert node.type == 'type_cast_expression'

        primitive_type, open_bracket_token, expression, close_bracket_token = node.children
        assert open_bracket_token.type == '(' and close_bracket_token.type == ')'

        type_cast_expression = TypeCastExpression(node)
        type_cast_expression._type = TypeParser.parse_primitive_type(primitive_type)
        type_cast_expression._expression = ExpressionParser.parse_expression(expression)

        return type_cast_expression

    
    # PRIMARY EXPRESSIONS
    @staticmethod
    def parse_parenthesized_expression(node) -> ParenthesizedExpression:
        assert node.type == 'parenthesized_expression'

        open_bracket_token, expression, close_bracket_token = node.children
        assert open_bracket_token.type == '(' and close_bracket_token.type == ')'

        parenthesized_expression = ParenthesizedExpression(node)
        parenthesized_expression._expression = ExpressionParser.parse_expression(expression)

        return parenthesized_expression

    @staticmethod
    def parse_member_expression(node) -> MemberAccess:
        assert node.type == 'member_expression'

        object_or_expression, period_token, member = node.children
        assert period_token.type == '.' and member.type == 'identifier'

        member_access = MemberAccess(node)
        member_access._member = ExpressionParser.parse_identifier(member)
        
        if object_or_expression.type == 'identifier':
            member_access._object = ExpressionParser.parse_identifier(object_or_expression)
        else:
            member_access._object = ExpressionParser.parse_expression(object_or_expression)

        return member_access

    @staticmethod
    def parse_array_access(node) -> ArrayAccess:
        assert node.type == 'array_access'

        base = index = None
        match node.children_types:
            case [_, '[', ']']:
                base, _, _ = node.children
            case [_, '[', _, ']']:
                base, _, index, _ = node.children
            case _:
                raise ParsingException(f'Unable to parse array_access: {node.text}')

        array_access = ArrayAccess(node)
        array_access._object = ExpressionParser.parse_expression(base)
        if index:
            array_access._index = ExpressionParser.parse_expression(index)

        return array_access

    @staticmethod
    def parse_slice_access(node) -> SliceAccess:
        assert node.type == 'slice_access'

        base = from_expression = to_expression = None
        match node.children_types:
            case [_, '[', ':', ']']:
                base, _, _, _ = node.children
            case [_, '[', _, ':', ']']:
                base, _, from_expression, _, _ = node.children
            case [_, '[', ':', _, ']']:
                base, _, _, to_expression, _ = node.children
            case [_, '[', _, ':', _, ']']:
                base, _, from_expression, _, to_expression, _ = node.children
            case _:
                raise ParsingException(f'Unable to parse slice_access: {node.text}')

        slice_access = SliceAccess(node)
        slice_access._object = ExpressionParser.parse_expression(base)

        if from_expression:
            slice_access._start = ExpressionParser.parse_expression(from_expression)    
        if to_expression:
            slice_access._stop = ExpressionParser.parse_expression(to_expression)    
        
        return slice_access

    @staticmethod
    def parse_assignment_expression(node) -> AssignmentOperation:
        assert node.type == 'assignment_expression'
        
        left, equal_token, right = node.children
        assert equal_token.type == '='

        assignment_operation = AssignmentOperation(node)
        assignment_operation._left_expression = ExpressionParser.parse_expression(left)
        assignment_operation._right_expression = ExpressionParser.parse_expression(right)
        assignment_operation._operator = AssignmentOperator.ASSIGN

        return assignment_operation

    @staticmethod
    def parse_augmented_assignment_expression(node) -> AssignmentOperation:
        assert node.type == 'augmented_assignment_expression'

        left, operator, right = node.children

        assignment_operation = AssignmentOperation(node)
        assignment_operation._left_expression = ExpressionParser.parse_expression(left)
        assignment_operation._right_expression = ExpressionParser.parse_expression(right)
        assignment_operation._operator = AssignmentOperator(operator.text)

        return assignment_operation

    @staticmethod
    def parse_tuple_expression(node) -> TupleExpression:
        assert node.type == 'tuple_expression'

        tuple_expression = TupleExpression(node)
        tuple_expression._expressions, _ = extract_nodes_between_brackets(
            node, '(', ')',
            parsing_function=ExpressionParser.parse_expression
        )
        return tuple_expression

    @staticmethod
    def parse_inline_array_expression(node) -> InlineArrayExpression:
        assert node.type == 'inline_array_expression'

        inline_array_expression = InlineArrayExpression(node)
        inline_array_expression._expressions, _ = extract_nodes_between_brackets(
            node, '[', ']',
            parsing_function=ExpressionParser.parse_expression
        )
        return inline_array_expression      

    @staticmethod
    def parse_identifier(node) -> Identifier:
        assert node.type in ['identifier', 'enum_value']
        return Identifier(node)

    @staticmethod
    def parse_literal(node) -> Literal:
        assert node.type in ['string_literal', 'number_literal', 'boolean_literal', 'hex_string_literal', 'unicode_string_literal']

        literal = Literal(node)
        literal._literal_type = LiteralType.literal_type_from_node_type(node.type)

        if node.type == 'number_literal':
            literal._declared_value, *unit = node.text.split()
            if unit:
                literal._unit = unit[0]
        else:
            literal._declared_value = node.text

        return literal

    @staticmethod
    def parse_new_expression(node) -> NewExpression:
        assert node.type == 'new_expression'

        new_expression = NewExpression(node)
        match node.children_types:
            case ['new', 'type_name']:
                _, type_name = node.children
                new_expression._type = TypeParser.parse_type_name(type_name)

            case ['new', 'type_name', _]:
                # tree-sitter-solidity has call_arguments in new_expression, but I don't think it exists in Solidity...
                raise NotImplementedError(f'Parsing new_expression with call_arguments is not implemented: {node.text}')

            case _:
                raise ParsingException(f'Unable to parse new_expression: {node.text}')
            
        return new_expression