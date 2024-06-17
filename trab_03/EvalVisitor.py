from math import factorial
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class EvalVisitor(ExprVisitor):
    def visitRoot(self, ctx: ExprParser.RootContext):
        return self.visit(ctx.expr())

    def visitParent(self, ctx: ExprParser.ParentContext):
        return self.visit(ctx.expr())

    def visitPot(self, ctx: ExprParser.PotContext):
        left, right = self.exprLeftRight(ctx)
        return left**right

    def visitMultDiv(self, ctx: ExprParser.MultDivContext):
        left, right = self.exprLeftRight(ctx)
        if ctx.getChild(1).getText() == "*":
            return left * right
        elif ctx.getChild(1).getText() == "/":
            return left / right

    def visitSomaSub(self, ctx: ExprParser.SomaSubContext):
        left, right = self.exprLeftRight(ctx)
        if ctx.getChild(1).getText() == "+":
            return left + right
        elif ctx.getChild(1).getText() == "-":
            return left - right

    def visitFunc(self, ctx: ExprParser.FuncContext):
        if ctx.abs_():
            return self.visit(ctx.abs_())
        elif ctx.fact():
            return self.visit(ctx.fact())

    def visitAbs_(self, ctx: ExprParser.Abs_Context):
        value = self.visit(ctx.expr())
        return abs(value)

    def visitFact(self, ctx: ExprParser.FactContext):
        value = self.visit(ctx.expr())
        return factorial(int(value))

    def visitNumber(self, ctx: ExprParser.NumberContext):
        number = float(ctx.NUM().getText())
        if ctx.getChild(0).getText() == "-":
            number = -number
        return number

    def exprLeftRight(self, ctx: ExprParser.ExprContext):
        return (self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
