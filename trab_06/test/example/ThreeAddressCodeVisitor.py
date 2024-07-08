from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor


class ThreeAddressCoedVisitor(SimpleLangVisitor):
    temp_count = 0

    def __new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def visitProg(self, ctx: SimpleLangParser.ProgContext):
        for stat in ctx.stat():
            self.visit(stat)

    def visitStat(self, ctx: SimpleLangParser.StatContext):
        return self.visitChildren(ctx)

    def visitIfStat(self, ctx: SimpleLangParser.IfStatContext):
        cond = self.visit(ctx.expr())
        then_label = self.__new_temp()
        end_label = self.__new_temp()
        print(f"if {cond} goto {then_label}\ngoto {end_label}\n{then_label}: ")
        self.visit(ctx.stat())
        print(f"{end_label}:")
        return

    def visitWhileStat(self, ctx: SimpleLangParser.WhileStatContext):
        start_label = self.__new_temp()
        middle_label = self.__new_temp()
        end_label = self.__new_temp()
        print(f"{start_label}: ")
        cond = self.visit(ctx.expr())
        print(f"if {cond} goto {middle_label}\ngoto {end_label}\n{middle_label}:")
        self.visit(ctx.stat())
        print(f"goto {start_label}\n{end_label}")
        return

    def visitAssignStat(self, ctx: SimpleLangParser.AssignStatContext):
        value = self.visit(ctx.expr())
        code = f"{ctx.ID().getText()} = {value};"
        print(code)
        return code

    def visitExprStat(self, ctx: SimpleLangParser.ExprStatContext):
        expr = self.visit(ctx.expr())
        print(f"{expr};")
        return expr

    def visitMulDivExpr(self, ctx: SimpleLangParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        temp = self.__new_temp()
        print(f"{temp} = {left} {op} {right}")
        return temp

    def visitAddSubExpr(self, ctx: SimpleLangParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        temp = self.__new_temp()
        print(f"{temp} = {left} {op} {right}")
        return temp

    def visitRelationalExpr(self, ctx: SimpleLangParser.RelationalExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        temp = self.__new_temp()
        print(f"{temp} = {left} {op} {right}")
        return temp

    def visitLogicalExpr(self, ctx: SimpleLangParser.LogicalExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        temp = self.__new_temp()
        print(f"{temp} = {left} {op} {right}")
        return temp

    def visitNotExpr(self, ctx: SimpleLangParser.NotExprContext):
        expr = self.visit(ctx.expr())
        temp = self.__new_temp()
        print(f"{temp} = !{expr}")
        return temp

    def visitIdExpr(self, ctx: SimpleLangParser.IdExprContext):
        return ctx.ID().getText()

    def visitIntExpr(self, ctx: SimpleLangParser.IntExprContext):
        return ctx.INT().getText()

    def visitParenExpr(self, ctx: SimpleLangParser.ParenExprContext):
        return self.visit(ctx.expr())
