# Generated from Expr.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#root.
    def enterRoot(self, ctx:ExprParser.RootContext):
        pass

    # Exit a parse tree produced by ExprParser#root.
    def exitRoot(self, ctx:ExprParser.RootContext):
        pass


    # Enter a parse tree produced by ExprParser#Number.
    def enterNumber(self, ctx:ExprParser.NumberContext):
        pass

    # Exit a parse tree produced by ExprParser#Number.
    def exitNumber(self, ctx:ExprParser.NumberContext):
        pass


    # Enter a parse tree produced by ExprParser#Pot.
    def enterPot(self, ctx:ExprParser.PotContext):
        pass

    # Exit a parse tree produced by ExprParser#Pot.
    def exitPot(self, ctx:ExprParser.PotContext):
        pass


    # Enter a parse tree produced by ExprParser#Parent.
    def enterParent(self, ctx:ExprParser.ParentContext):
        pass

    # Exit a parse tree produced by ExprParser#Parent.
    def exitParent(self, ctx:ExprParser.ParentContext):
        pass


    # Enter a parse tree produced by ExprParser#Func.
    def enterFunc(self, ctx:ExprParser.FuncContext):
        pass

    # Exit a parse tree produced by ExprParser#Func.
    def exitFunc(self, ctx:ExprParser.FuncContext):
        pass


    # Enter a parse tree produced by ExprParser#SomaSub.
    def enterSomaSub(self, ctx:ExprParser.SomaSubContext):
        pass

    # Exit a parse tree produced by ExprParser#SomaSub.
    def exitSomaSub(self, ctx:ExprParser.SomaSubContext):
        pass


    # Enter a parse tree produced by ExprParser#MultDiv.
    def enterMultDiv(self, ctx:ExprParser.MultDivContext):
        pass

    # Exit a parse tree produced by ExprParser#MultDiv.
    def exitMultDiv(self, ctx:ExprParser.MultDivContext):
        pass


    # Enter a parse tree produced by ExprParser#abs_.
    def enterAbs_(self, ctx:ExprParser.Abs_Context):
        pass

    # Exit a parse tree produced by ExprParser#abs_.
    def exitAbs_(self, ctx:ExprParser.Abs_Context):
        pass


    # Enter a parse tree produced by ExprParser#fact.
    def enterFact(self, ctx:ExprParser.FactContext):
        pass

    # Exit a parse tree produced by ExprParser#fact.
    def exitFact(self, ctx:ExprParser.FactContext):
        pass



del ExprParser