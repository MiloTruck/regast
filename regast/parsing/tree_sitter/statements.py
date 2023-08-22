"""
No throw statement
"""

from typing import Union
from regast.core.expressions.expression import Expression
from regast.core.statements.assembly_statement import AssemblyStatement
from regast.core.statements.block import Block
from regast.core.statements.break_statement import BreakStatement
from regast.core.statements.continue_statement import ContinueStatement
from regast.core.statements.do_while_statement import DoWhileStatement
from regast.core.statements.emit_statement import EmitStatement
from regast.core.statements.for_statement import ForStatement
from regast.core.statements.if_statement import IfStatement
from regast.core.statements.return_statement import ReturnStatement
from regast.core.statements.revert_statement import RevertStatement
from regast.core.statements.statement import Statement
from regast.core.statements.try_statement import CatchClause, TryStatement
from regast.core.statements.variable_declaration_statement import VariableDeclarationFromTupleStatement, VariableDeclarationStatement, VariableDeclarationWithVarStatement
from regast.core.statements.while_statement import WhileStatement
from regast.core.variables.local_variable import LocalVariable
from regast.core.variables.variable import DataLocation
from regast.exceptions import ParsingException
from regast.parsing.tree_sitter.expressions import ExpressionParser
from regast.parsing.tree_sitter.helper import extract_call_arguments, extract_nodes_between_brackets, extract_parameters
from regast.parsing.tree_sitter.types import TypeParser


class StatementParser:
    @staticmethod
    def parse_statement(node) -> Statement:
        match node.type:
            case 'block_statement': return StatementParser.parse_block_statement(node)
            case 'expression_statement': return StatementParser.parse_expression_statement(node)
            case 'variable_declaration_statement': return StatementParser.parse_variable_declaration_statement(node)
            case 'if_statement': return StatementParser.parse_if_statement(node)
            case 'for_statement': return StatementParser.parse_for_statement(node)
            case 'while_statement': return StatementParser.parse_while_statement(node)
            case 'do_while_statement': return StatementParser.parse_do_while_statement(node)
            case 'continue_statement': return StatementParser.parse_continue_statement(node)
            case 'break_statement': return StatementParser.parse_break_statement(node)
            case 'try_statement': return StatementParser.parse_try_statement(node)
            case 'return_statement': return StatementParser.parse_return_statement(node)
            case 'emit_statement': return StatementParser.parse_emit_statement(node)
            case 'assembly_statement': return StatementParser.parse_assembly_statement(node)
            case 'revert_statement': return StatementParser.parse_revert_statement(node)
    
            case other:
                raise ParsingException(f'Unknown tree-sitter node type for statement: {other}')

    @staticmethod    
    def parse_block_statement(node) -> Block:
        assert node.type in ['function_body', 'block_statement']

        block = Block(node)

        statements = []
        match node.children_types:
            case ['{', *_, '}']:
                _, *statements, _ = node.children

            case ['unchecked', '{', *_, '}']:
                _, _, *statements, _ = node.children
                block._unchecked = True

            case _:
                raise ParsingException(f'Unable to parse block_statement: {node.text}')

        for child_node in statements:
            statement = StatementParser.parse_statement(child_node)
            block._statements.append(statement)

        return block

    @staticmethod    
    def parse_expression_statement(node) -> Expression:
        assert node.type == 'expression_statement'
        return ExpressionParser.parse_expression(node.children[0])

    @staticmethod    
    def parse_variable_declaration_statement(node) -> Union[VariableDeclarationStatement, VariableDeclarationFromTupleStatement, VariableDeclarationWithVarStatement]:
        assert node.type == 'variable_declaration_statement'

        def parse_variable_declaration(node) -> LocalVariable:
            assert node.type == 'variable_declaration'

            type_name = location = name = None
            match node.children_types:
                case ['type_name', 'identifier']:
                    type_name, name = node.children
                case ['type_name', ('memory' | 'storage' | 'calldata'), 'identifier']:
                    type_name, location, name = node.children
                case _:
                    raise ParsingException(f'Unable to parse variable_declaration: {node.text}')

            local_variable = LocalVariable(node)
            local_variable._type = TypeParser.parse_type_name(type_name)
            local_variable._name = ExpressionParser.parse_identifier(name)
            if location:
                local_variable._data_location = DataLocation(location.text)

            return local_variable

        match node.children_types:
            case ['variable_declaration', *remaining_types]:
                variable_declaration, *remaining_nodes = node.children

                local_variable = parse_variable_declaration(variable_declaration)

                match remaining_types:
                    # uint256 a;
                    case []:
                        pass
                    
                    # uint256 a = 10;
                    case ['=', _]:
                        _, expression = remaining_nodes
                        local_variable._expression = ExpressionParser.parse_expression(expression)

                return VariableDeclarationStatement(local_variable)

            case ['variable_declaration_tuple', '=', _]:
                variable_declaration_tuple, _, expression = node.children

                match variable_declaration_tuple.children_types:
                    # (uint256 a, uint256 b) = f()
                    case ['(', *_, ')']:
                        local_variables, _ = extract_nodes_between_brackets(
                            variable_declaration_tuple, '(', ')',
                            node_type='variable_declaration',
                            parsing_function=parse_variable_declaration
                        )

                        expression = ExpressionParser.parse_expression(expression)
                        for local_variable in local_variables:
                            local_variable._expression = expression

                        return VariableDeclarationFromTupleStatement(local_variables)

                    case ['var', '(', *_, ')']:
                        # var (a, b, c) = f()
                        _, _, *identifiers, _ = variable_declaration_tuple.children
                        statement = VariableDeclarationWithVarStatement(node)
                        statement._expression = ExpressionParser.parse_expression(expression)

                        for child_node in identifiers:
                            match child_node.type:
                                case 'identifier':
                                    identifier = ExpressionParser.parse_identifier(identifier)
                                    statement._names.append(identifier)
                                case ',':
                                    pass
                                case other:
                                    raise ParsingException(f'Unknown tree-sitter node type in variable_declaration_tuple: {other}')

                        return statement

        raise ParsingException(f'Unable to parse variable_declaration_statement: {node.text}')

    @staticmethod    
    def parse_if_statement(node) -> IfStatement:
        assert node.type == 'if_statement'

        condition = true_body = false_body = None
        match node.children_types:
            # if-statement
            case ['if', '(', _, ')', _]:
                _, _, condition, _, true_body = node.children
            
            # if-statement with else clause
            case ['if', '(', _, ')', _, 'else', _]:
                _, _, condition, _, true_body, _, false_body = node.children

        if_statement = IfStatement(node)
        if_statement._condition = ExpressionParser.parse_expression(condition)
        if_statement._true_body = StatementParser.parse_statement(true_body)
        if false_body:
            if_statement._false_body = StatementParser.parse_statement(false_body)
        
        return if_statement

    @staticmethod    
    def parse_for_statement(node) -> ForStatement:
        assert node.type == 'for_statement'
        
        initial = condition = update = body = None
        match node.children_types:
            case ['for', '(', _, _, _, ')', _]:
                _, _, initial, condition, update, _, body = node.children
            
            case ['for', '(', _, _, ')', _]:
                _, open_bracket, *statements, close_bracket, body = node.children

                # Since initial, condition and update are all optional, determine which is missing using text
                offset = node.start_column
                lo = open_bracket.start_column
                hi = close_bracket.start_column
                
                header_text = node.text[lo-offset+1:hi-offset]
                missing_index = header_text.replace(' ', '').split(';').index('')
                statements.insert(missing_index, None)

                initial, condition, update = statements

            case _:
                raise ParsingException(f'Unable to parse for_statement: {node.text}')

        for_statement = ForStatement(node)
        for_statement._body = StatementParser.parse_statement(body)

        if initial:
            match initial.type:
                case 'variable_declaration_statement':
                    for_statement._initialization = StatementParser.parse_variable_declaration_statement(initial)
                case 'expression_statement':
                    for_statement._initialization = StatementParser.parse_expression_statement(initial)
                case other:
                    raise ParsingException(f'Unknown tree-sitter node type for for_statement: {other}')

        if condition:
            for_statement._condition = StatementParser.parse_expression_statement(condition)

        if update:
            for_statement._iteration = ExpressionParser.parse_expression(update)

        return for_statement

    @staticmethod    
    def parse_while_statement(node) -> WhileStatement:
        assert node.type == 'while_statement'

        while_token, open_bracket_token, condition, close_bracket_token, body = node.children
        assert (
            while_token.type == 'while' and 
            open_bracket_token.type == '(' and 
            close_bracket_token.type == ')'
        )

        while_statement = WhileStatement(node)
        while_statement._condition = ExpressionParser.parse_expression(condition)
        while_statement._body = StatementParser.parse_statement(body)

        return while_statement

    @staticmethod    
    def parse_do_while_statement(node) -> DoWhileStatement:
        assert node.type == 'do_while_statement'

        do_token, body, while_token, open_bracket_token, condition, close_bracket_token = node.children
        assert (
            do_token.type == 'do' and
            while_token.type == 'while' and
            open_bracket_token.type == '(' and 
            close_bracket_token.type == ')'
        )

        do_while_statement = DoWhileStatement(node)
        do_while_statement._condition = ExpressionParser.parse_expression(condition)
        do_while_statement._body = StatementParser.parse_statement(body)

        return do_while_statement

    @staticmethod    
    def parse_continue_statement(node) -> ContinueStatement:
        assert node.type == 'continue_statement'
        return ContinueStatement(node)

    @staticmethod    
    def parse_break_statement(node) -> BreakStatement:
        assert node.type == 'break_statement'
        return BreakStatement(node)

    @staticmethod    
    def parse_try_statement(node) -> TryStatement:
        assert node.type == 'try_statement'

        def parse_catch_clause(node) -> CatchClause:
            assert node.type == 'catch_clause'
            
            parameters, remaining_nodes = extract_parameters(node)
            
            body = error = None
            match [node.type for node in remaining_nodes]:
                case ['catch', 'block_statement']:
                    _, body = remaining_nodes

                case ['catch', 'identifier', 'block_statement']:
                    _, error, body = remaining_nodes

                case _:
                    raise ParsingException(f'Unable to parse catch clause: {node.text}')

            catch_clause = CatchClause(node)
            catch_clause._body = StatementParser.parse_block_statement(body)
            catch_clause._parameters = parameters

            if error:
                catch_clause._error = ExpressionParser.parse_identifier(error) 

            return catch_clause


        parameters, remaining_nodes = extract_parameters(node)

        attempt = body = None
        catch_clauses = []
        match [node.type for node in remaining_nodes]:
            case ['try', _, 'block_statement', *_]:
                _, attempt, body, *catch_clauses = remaining_nodes

            case ['try', _, 'returns', 'block_statement', *_]:
                _, attempt, _, body, *catch_clauses = remaining_nodes

            case _:
                raise ParsingException(f'Unable to parse try_statement: {node.text}')

        try_statement = TryStatement(node)
        try_statement._try_expression = ExpressionParser.parse_expression(attempt)
        try_statement._body = StatementParser.parse_block_statement(body)
        try_statement._parameters = parameters
        try_statement._catch_clauses = [parse_catch_clause(cc) for cc in catch_clauses]

        return try_statement

    @staticmethod    
    def parse_return_statement(node) -> ReturnStatement:
        assert node.type == 'return_statement'
        
        return_statement = ReturnStatement(node)
        match node.children_types:
            case ['return']:
                pass

            case ['return', _]:
                _, expression = node.children
                return_statement._return_value = ExpressionParser.parse_expression(expression)
                
            case _:
                raise ParsingException(f'Unable to parse return_statement: {node.text}')

        return return_statement

    @staticmethod    
    def parse_emit_statement(node) -> EmitStatement:
        assert node.type == 'emit_statement'

        arguments, struct_arguments, [_, name] = extract_call_arguments(node)

        emit_statement = EmitStatement(node)
        emit_statement._event_name = ExpressionParser.parse_expression(name)
        emit_statement._struct_arguments = struct_arguments
        emit_statement._arguments = arguments

        return emit_statement

    @staticmethod    
    def parse_revert_statement(node) -> RevertStatement:
        assert node.type == 'revert_statement'

        revert_statement = RevertStatement(node)
        match node.children_types:
            case ['revert']:
                pass

            case ['revert', 'revert_arguments']:
                _, revert_arguments = node.children
                revert_statement._arguments, revert_statement._struct_arguments, _ = extract_call_arguments(revert_arguments)

            case ['revert', _]:
                _, error = node.children
                revert_statement._error_name = ExpressionParser.parse_expression(error)

            case ['revert', _, 'revert_arguments']:
                _, error, revert_arguments = node.children
                revert_statement._error_name = ExpressionParser.parse_expression(error)
                revert_statement._arguments, revert_statement._struct_arguments, _ = extract_call_arguments(revert_arguments)

            case _:
                raise ParsingException(f'Unable to parse revert_statement: {node.text}')

        return revert_statement
        
    @staticmethod    
    def parse_assembly_statement(node) -> AssemblyStatement:
        assert node.type == 'assembly_statement'

        # TODO: Implement parsing for assembly and yul-statements

        return AssemblyStatement(node)


