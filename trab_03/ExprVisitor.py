# Generated from Expr.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Number.
    def visitNumber(self, ctx:ExprParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Pot.
    def visitPot(self, ctx:ExprParser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Parent.
    def visitParent(self, ctx:ExprParser.ParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Func.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SomaSub.
    def visitSomaSub(self, ctx:ExprParser.SomaSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MultDiv.
    def visitMultDiv(self, ctx:ExprParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#abs_.
    def visitAbs_(self, ctx:ExprParser.Abs_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fact.
    def visitFact(self, ctx:ExprParser.FactContext):
        return self.visitChildren(ctx)



del ExprParser