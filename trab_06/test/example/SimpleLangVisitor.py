# Generated from SimpleLang.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#prog.
    def visitProg(self, ctx:SimpleLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#stat.
    def visitStat(self, ctx:SimpleLangParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifStat.
    def visitIfStat(self, ctx:SimpleLangParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#whileStat.
    def visitWhileStat(self, ctx:SimpleLangParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignStat.
    def visitAssignStat(self, ctx:SimpleLangParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#exprStat.
    def visitExprStat(self, ctx:SimpleLangParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:SimpleLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#IdExpr.
    def visitIdExpr(self, ctx:SimpleLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#NotExpr.
    def visitNotExpr(self, ctx:SimpleLangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#IntExpr.
    def visitIntExpr(self, ctx:SimpleLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:SimpleLangParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ParenExpr.
    def visitParenExpr(self, ctx:SimpleLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:SimpleLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#LogicalExpr.
    def visitLogicalExpr(self, ctx:SimpleLangParser.LogicalExprContext):
        return self.visitChildren(ctx)



del SimpleLangParser