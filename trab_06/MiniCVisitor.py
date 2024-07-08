# Generated from MiniC.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#program.
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#definition.
    def visitDefinition(self, ctx:MiniCParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#data_definition.
    def visitData_definition(self, ctx:MiniCParser.Data_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function.
    def visitFunction(self, ctx:MiniCParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_definition.
    def visitFunction_definition(self, ctx:MiniCParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_header.
    def visitFunction_header(self, ctx:MiniCParser.Function_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameter.
    def visitParameter(self, ctx:MiniCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameter_list.
    def visitParameter_list(self, ctx:MiniCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_call.
    def visitFunction_call(self, ctx:MiniCParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_body.
    def visitFunction_body(self, ctx:MiniCParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#argument_list.
    def visitArgument_list(self, ctx:MiniCParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statement.
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#compound_statement.
    def visitCompound_statement(self, ctx:MiniCParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expression_statement.
    def visitExpression_statement(self, ctx:MiniCParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#while_statement.
    def visitWhile_statement(self, ctx:MiniCParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#if_statement.
    def visitIf_statement(self, ctx:MiniCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expression.
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MiniCParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#binary.
    def visitBinary(self, ctx:MiniCParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unary.
    def visitUnary(self, ctx:MiniCParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#primary.
    def visitPrimary(self, ctx:MiniCParser.PrimaryContext):
        return self.visitChildren(ctx)



del MiniCParser