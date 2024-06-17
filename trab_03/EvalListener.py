from ExprListener import ExprListener
from ExprParser import ExprParser
from math import factorial


class EvalListener(ExprListener):
    def __init__(self):
        self.stack = []

    def exitParent(self, ctx: ExprParser.ParentContext):
        pass

    def exitMultDiv(self, ctx: ExprParser.MultDivContext):
        right, left = self.popRightLeft()
        if ctx.getChild(1).getText() == "*":
            self.stack.append(left * right)
        elif ctx.getChild(1).getText() == "/":
            self.stack.append(left / right)

    def exitPot(self, ctx: ExprParser.PotContext):
        right, left = self.popRightLeft()
        self.stack.append(left**right)

    def exitSomaSub(self, ctx):
        right, left = self.popRightLeft()
        if ctx.getChild(1).getText() == "+":
            self.stack.append(left + right)
        elif ctx.getChild(1).getText() == "-":
            self.stack.append(left - right)

    def exitFunc(self, ctx: ExprParser.FuncContext):
        if ctx.abs_():
            value = self.stack.pop()
            self.stack.append(abs(value))
        elif ctx.fact():
            value = self.stack.pop()
            self.stack.append(factorial(int(value)))

    def exitNumber(self, ctx: ExprParser.NumberContext):
        number = float(ctx.NUM().getText())
        if ctx.getChild(0).getText() == "-":
            number = -number

        self.stack.append(number)

    def popRightLeft(self):
        return (self.stack.pop(), self.stack.pop())

    def getResult(self):
        return self.stack[-1]
