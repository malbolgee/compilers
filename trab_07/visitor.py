"""
    This module contains the Visitor class for semantic analysis.

    NOTE: Needs Python 3.10 or grater to work

    @authors: Victor Hugo, Aldemir Silva, Nilson Andrade.
"""

from __future__ import annotations

import sys
from typing import Dict, List

from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl
from MiniCParser import MiniCParser
from MiniCVisitor import MiniCVisitor


class ErrorMessages:

    @staticmethod
    def error() -> str:
        return "\033[91merror:\033[00m"

    @staticmethod
    def var_not_defined_error(var_id: str) -> str:
        return f"{ErrorMessages.error()} variable '{var_id}' is not defined."

    @staticmethod
    def arg_not_defined_error(arg_id: str) -> str:
        return ErrorMessages.var_not_defined_error(arg_id)

    @staticmethod
    def var_type_error(var_id: str, expt_type: str | None, rcv_type: str | None) -> str:
        return f"{ErrorMessages.error()} variable '{var_id}' expected type '{expt_type}' but got '{rcv_type}'."

    @staticmethod
    def fun_call_arg_type_error(
        fun_id: str, arg_type: str | None, param_id: str, recv_type: str | None
    ) -> str:
        return f"{ErrorMessages.error()} function '{fun_id}' expected '{arg_type}' for param '{param_id}' but got '{recv_type}'."

    @staticmethod
    def fun_call_not_defined_error(fun_id: str) -> str:
        return f"{ErrorMessages.error()} function '{fun_id}' is not defined."

    @staticmethod
    def fun_arg_count_error(fun_id: str, expt_count: int, rcv_count: int) -> str:
        return f"{ErrorMessages.error()} function '{fun_id}' expected '{expt_count}' arguments but got '{rcv_count}'."

    @staticmethod
    def fun_ret_type_error(fun_id: str, fun_type: str, rcv_type: str) -> str:
        return f"{ErrorMessages.error()} function '{fun_id}' return type is '{fun_type}' but is returning type '{rcv_type}'."

    @staticmethod
    def fun_not_ret_error(fun_id: str, fun_type: str) -> str:
        return f"{ErrorMessages.error()} function '{fun_id}' has return type '{fun_type}' but is missing a 'return' statement."

    @staticmethod
    def var_redeclaration_error(var_id: str) -> str:
        return f"{ErrorMessages.error()} variable '{var_id}' is already declared."

    @staticmethod
    def expression_type_mismatch_error(fun_id: str) -> str:
        return f"{ErrorMessages.error()} in function '{fun_id}' found type mismatch in expression."


class BaseSymbol:
    """
    This is the base symbol for the Symbol classes
    """

    def __init__(self, _id: str, _type: str | None = None) -> None:
        self.id = _id
        self.type = _type


class Symbol(BaseSymbol):
    """
    This class represents a symbol in the language
    """

    def __init__(self, _id: str, scope: str, _type: str | None = None):
        super().__init__(_id, _type)
        self.scope = scope

    def __hash__(self) -> int:
        return hash(self.id + ":" + self.scope)

    def __str__(self) -> str:
        return (
            "<"
            + self.id
            + ":"
            + self.scope
            + (":" + self.type if self.type else "")
            + ">"
        )

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Symbol):
            return False

        if value is None:
            return False

        return hash(self) == hash(value)


class FunctionSymbol(BaseSymbol):
    """
    This class represents a function symbol.
    """

    def __init__(self, _id: str, _type: str = "int") -> None:
        super().__init__(_id, _type)
        self.args: List[Symbol] = []

    def __str__(self) -> str:
        return (
            "<"
            + self.id
            + ":"
            + str(self.type)
            + ":"
            + "["
            + " ".join(str(x) for x in self.args)
            + "]"
            + ">"
        )


class SymbolTable:
    """
    This class represents a symbol table of the Symbol types
    """

    def __init__(self) -> None:
        self.table: Dict[int, Symbol] = {}

    def add(self, sym: Symbol) -> None:
        """Adds a new symbol to the table"""
        self.table[hash(sym)] = sym

    def get(self, sym: Symbol) -> Symbol | None:
        """Get a symbol from the table"""
        return self.table.get(hash(sym))

    def __getitem__(self, value: Symbol) -> Symbol | None:
        return self.get(value)

    def __str__(self) -> str:
        return " ".join(str(x) for x in self.table.values())


class SemanticVisitor(MiniCVisitor):
    """
    This class does the semantic analysis for the MiniC grammar.
    """

    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.sym_table: SymbolTable = SymbolTable()
        self.fun_sym_table: Dict[str, FunctionSymbol] = {}
        self.errors: List[str] = []
        self.current_scope: str = "global"

    def __print_fun_sym_table(self):
        return " ".join(str(x) for x in self.fun_sym_table.values())

    def __add_error(self, message: str, ctx: ParserRuleContext):
        """Add an encountered error to the error list"""
        self.errors.append(
            f"{self.file_name}:{ctx.start.line}:{ctx.start.column}: {message}"
        )

    def visitProgram(self, ctx: MiniCParser.ProgramContext):
        for child in ctx.getChildren():
            self.visit(child)

        return self.errors

    def visitDefinition(self, ctx: MiniCParser.DefinitionContext):
        self.current_scope = "global"
        return self.visitChildren(ctx)

    def visitData_definition(self, ctx: MiniCParser.Data_definitionContext):
        _type = ctx.TYPE().getText()

        for _id in ctx.IDENTIFIER():
            n_sym = Symbol(_id.getText(), self.current_scope, _type)
            sym = self.sym_table[n_sym]

            # the variable being declared cannot be redeclare in the same scope
            if sym is not None and sym.scope == self.current_scope:
                self.__add_error(ErrorMessages.var_redeclaration_error(_id), ctx)
            else:
                self.sym_table.add(n_sym)

    def visitFunction_definition(self, ctx: MiniCParser.Function_definitionContext):
        _type = ctx.TYPE().getText() if ctx.TYPE() else "int"
        _id = ctx.function_header().IDENTIFIER().getText()

        args = ctx.function_header().parameter_list()

        self.current_scope = _id

        fsym = FunctionSymbol(_id, _type)

        if args:
            for arg in args.parameter():
                arg_id = arg.IDENTIFIER().getText()
                arg_type = arg.TYPE().getText()

                sym = Symbol(arg_id, self.current_scope, arg_type)

                fsym.args.append(sym)

                # function parameters are also variables declared
                # in the scope of the function defining them
                self.sym_table.add(sym)

        self.fun_sym_table[_id] = fsym
        return self.visitChildren(ctx)

    def visitFunction_call(self, ctx: MiniCParser.Function_callContext):
        _id = ctx.IDENTIFIER().getText()

        # Is this function even declared?
        if _id not in self.fun_sym_table:
            self.__add_error(ErrorMessages.fun_call_not_defined_error(_id), ctx)
            return None

        expected_count = len(self.fun_sym_table[_id].args)

        if ctx.argument_list():
            provided_count = len(ctx.argument_list().binary())

            if provided_count != expected_count:
                self.__add_error(
                    ErrorMessages.fun_arg_count_error(
                        _id, expected_count, provided_count
                    ),
                    ctx,
                )
                return None

            for i in range(provided_count):
                binary = ctx.argument_list().binary(i)
                arg_sym = self.fun_sym_table[_id].args[i]

                if binary.binary(0) and binary.binary(1):
                    expr_type = self.visit(binary)
                    if arg_sym.type != expr_type:
                        self.__add_error(
                            ErrorMessages.fun_call_arg_type_error(
                                _id, arg_sym.type, arg_sym.id, expr_type
                            ),
                            ctx,
                        )
                    continue

                if binary.unary().PLUS_PLUS() or binary.unary().MINUS_MINUS():
                    arg_id = binary.unary().IDENTIFIER().getText()
                    sym = self.sym_table[Symbol(arg_id, self.current_scope)]

                    if sym is None:
                        self.__add_error(
                            ErrorMessages.var_not_defined_error(arg_id), ctx
                        )
                        return None

                    continue

                primary: MiniCParser.PrimaryContext = binary.unary().primary()
                arg = primary.getText()

                if primary.IDENTIFIER():
                    sym = self.__get_symbol(arg)
                    if sym is None:
                        self.__add_error(ErrorMessages.arg_not_defined_error(arg), ctx)
                        continue

                    provided_type = sym.type

                    if arg_sym.type != provided_type:
                        self.__add_error(
                            ErrorMessages.fun_call_arg_type_error(
                                _id, arg_sym.type, arg_sym.id, provided_type
                            ),
                            ctx,
                        )

                elif primary.CONSTANT_INT():
                    if arg_sym.type != "int":
                        self.__add_error(
                            ErrorMessages.fun_call_arg_type_error(
                                _id, arg_sym.type, arg_sym.id, "int"
                            ),
                            ctx,
                        )

                elif primary.CONSTANT_CHAR():
                    if arg_sym.type != "char":
                        self.__add_error(
                            ErrorMessages.fun_call_arg_type_error(
                                _id, arg_sym.type, arg_sym.id, "char"
                            ),
                            ctx,
                        )

                elif primary.expression():
                    expr_type = self.visit(primary.expression())

                    if arg_sym.type != expr_type:
                        self.__add_error(
                            ErrorMessages.fun_call_arg_type_error(
                                _id, arg_sym.type, arg_sym.id, expr_type
                            ),
                            ctx,
                        )

                elif primary.function_call():
                    arg_fun_id = primary.function_call().IDENTIFIER().getText()

                    if arg_fun_id not in self.fun_sym_table:
                        self.__add_error(
                            ErrorMessages.fun_call_not_defined_error(arg_fun_id), ctx
                        )
                        continue

                    arg_fun_type = self.fun_sym_table[arg_fun_id].type

                    if arg_sym.type != arg_fun_type:
                        self.__add_error(
                            ErrorMessages.fun_call_arg_type_error(
                                _id, arg_sym.type, arg_sym.id, arg_fun_type
                            ),
                            ctx,
                        )

        return self.fun_sym_table[_id].type

    def __get_symbol(self, _id: str) -> Symbol | None:
        for scope in [self.current_scope, "global"]:
            sym = self.sym_table[Symbol(_id, scope)]
            if sym is not None:
                return sym

        return None

    def visitAssignment_statement(self, ctx: MiniCParser.Assignment_statementContext):
        _id = ctx.IDENTIFIER().getText()
        sym = self.__get_symbol(_id)

        if sym is None:
            self.__add_error(ErrorMessages.var_not_defined_error(_id), ctx)
            return

        expr_type = self.visit(ctx.expression())
        expected_type = sym.type

        if expr_type is None or expr_type != expected_type:
            self.__add_error(
                ErrorMessages.var_type_error(_id, expected_type, expr_type), ctx
            )

    def visitExpression(self, ctx: MiniCParser.ExpressionContext):
        return self.visit(ctx.binary())

    def visitUnary(self, ctx: MiniCParser.UnaryContext):
        if ctx.PLUS_PLUS() or ctx.MINUS_MINUS():
            _id = ctx.IDENTIFIER().getText()
            sym = self.sym_table[Symbol(_id, self.current_scope)]
            if sym is None:
                self.__add_error(ErrorMessages.var_not_defined_error(_id), ctx)
                return None

            return sym.type

        return self.visit(ctx.primary())

    def visitBinary(self, ctx: MiniCParser.BinaryContext):
        if ctx.binary(0) and ctx.binary(1):
            l_type = self.visit(ctx.binary(0))
            r_type = self.visit(ctx.binary(1))

            if l_type != r_type:
                self.__add_error(
                    ErrorMessages.expression_type_mismatch_error(self.current_scope),
                    ctx,
                )
                return None

            return l_type
        return self.visitChildren(ctx)

    def visitPrimary(self, ctx: MiniCParser.PrimaryContext):
        if ctx.IDENTIFIER():
            var_id = ctx.IDENTIFIER().getText()
            sym = self.__get_symbol(var_id)

            if sym is None:
                self.__add_error(ErrorMessages.var_not_defined_error(var_id), ctx)
                return None

            return sym.type

        if ctx.CONSTANT_INT():
            return "int"

        if ctx.CONSTANT_CHAR():
            return "char"

        if ctx.function_call():
            fun_id = ctx.function_call().IDENTIFIER().getText()

            if fun_id not in self.fun_sym_table:
                self.__add_error(ErrorMessages.fun_call_not_defined_error(fun_id), ctx)
                return None

            return self.visit(ctx.function_call())

        if ctx.expression():
            return self.visit(ctx.expression())

        return None


class IntermediateCodeVisitor(MiniCVisitor):
    def __init__(self, file=sys.stderr):
        self.__tmp = -1
        self.__label = -1
        self.__file = file
        self.__symbol = {"*=": "*", "/=": "/", "%=": "%", "+=": "+", "-=": "-"}

    def __write(self, line: str, end: str = "\n") -> None:
        print(line, file=self.__file, end=end)

    def __new_label(self) -> str:
        self.__label += 1
        return f"L{self.__label}"

    def __new_tmp(self) -> str:
        self.__tmp += 1
        return f"t{self.__tmp}"

    def visitAssignment_statement(self, ctx: MiniCParser.Assignment_statementContext):
        _id = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        op = ctx.getChild(1)

        if op.getPayload().text == "=":
            self.__write(f"{_id} {op} {value}")
            return

        self.__write(f"{_id} = {_id} {self.__symbol[op.getPayload().text]} {value}")

    def visitExpression(self, ctx: MiniCParser.ExpressionContext):
        return self.visit(ctx.binary())

    def visitBinary(self, ctx: MiniCParser.BinaryContext):
        if ctx.binary(0) and ctx.binary(1):
            left = self.visit(ctx.binary(0))
            right = self.visit(ctx.binary(1))
            op = ctx.getChild(1).getText()
            tmp = self.__new_tmp()
            self.__write(f"{tmp} = {left} {op} {right}")
            return tmp

        return self.visitChildren(ctx)

    def visitUnary(self, ctx: MiniCParser.UnaryContext):
        if ctx.PLUS_PLUS():
            var = ctx.IDENTIFIER().getText()
            self.__write(f"{var} = {var} + 1")
            return var

        if ctx.MINUS_MINUS():
            var = ctx.IDENTIFIER().getText()
            self.__write(f"{var} = {var} - 1")
            return var

        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: MiniCParser.PrimaryContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()

        if ctx.CONSTANT_INT():
            return ctx.CONSTANT_INT().getText()

        if ctx.CONSTANT_CHAR():
            return str(ord(ctx.CONSTANT_CHAR().getText()[1]))

        if ctx.function_call():
            return self.visit(ctx.function_call())

        if ctx.expression():
            return self.visit(ctx.expression())

    def visitFunction_definition(self, ctx: MiniCParser.Function_definitionContext):
        _id = ctx.function_header().IDENTIFIER().getText()
        args = ctx.function_header().parameter_list()
        arg_list = []

        if args:
            for arg in args.parameter():
                arg_id = arg.IDENTIFIER().getText()
                arg_list.append(arg_id)

        arg_list_str = ", ".join(arg_list)
        self.__write(f"{_id}({arg_list_str}):")
        self.visit(ctx.function_body())

    def visitFunction_body(self, ctx: MiniCParser.Function_bodyContext):
        return self.visitChildren(ctx)

    def visitFunction_call(self, ctx: MiniCParser.Function_callContext):

        args = []
        if ctx.argument_list():

            for arg in ctx.argument_list().binary():

                if arg.binary(0) and arg.binary(1):
                    args.append(self.visit(arg))
                    continue

                if arg.unary().PLUS_PLUS() or arg.unary().MINUS_MINUS():
                    args.append(self.visit(arg.unary()))
                    continue

                primary: MiniCParser.PrimaryContext = arg.unary().primary()

                if primary.IDENTIFIER():
                    args.append(primary.getText())

                elif primary.CONSTANT_INT():
                    args.append(primary.CONSTANT_INT().getText())

                elif primary.CONSTANT_CHAR():
                    args.append(str(ord(primary.CONSTANT_CHAR().getText()[1])))

                elif primary.expression():
                    args.append(self.visit(primary.expression()))

                elif primary.function_call():
                    tmp = self.__new_tmp()
                    self.__write(f"{tmp} = {self.visit(primary.function_call())}")
                    args.append(tmp)

        _id = ctx.IDENTIFIER().getText()
        args_str = ", ".join(args)
        call = f"{_id}({args_str})"

        return call

    def visitStatement(self, ctx: MiniCParser.StatementContext):
        for child in ctx.getChildren():
            if isinstance(child, TerminalNodeImpl):
                continue

            if child.getRuleIndex() == MiniCParser.RULE_expression:
                tmp = self.__new_tmp()
                expr = self.visit(child)
                self.__write(f"{tmp} = {expr}")
                self.__write(f"return {tmp}")
                continue

            self.visit(child)

    def visitWhile_statement(self, ctx: MiniCParser.While_statementContext):
        s_label = self.__new_label()
        m_label = self.__new_label()
        e_label = self.__new_label()
        self.__write(f"{s_label}:")
        cond = self.visit(ctx.expression())
        self.__write(f"if {cond} goto {m_label}, goto {e_label}\n{m_label}:")
        self.visit(ctx.statement())
        self.__write(f"goto {s_label}\n{e_label}:")

    def visitIf_statement(self, ctx: MiniCParser.If_statementContext):
        cond = self.visit(ctx.expression())
        if_label = self.__new_label()
        else_label = self.__new_label()
        end_label = self.__new_label()
        self.__write(f"if {cond} goto {if_label}, goto {else_label}\n{if_label}:")
        self.visit(ctx.statement(0))
        if ctx.ELSE():
            self.__write(f"goto {end_label}")

        self.__write(f"{else_label}:")
        if ctx.ELSE():
            self.visit(ctx.statement(1))
            self.__write(f"{end_label}:")
