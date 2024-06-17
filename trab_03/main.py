from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

# from EvalListener import EvalListener
from EvalVisitor import EvalVisitor

input_stream = InputStream(input("? "))

lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()

# eval_listener = EvalListener()
# walker = ParseTreeWalker()
# walker.walk(eval_listener, tree)

# print(eval_listener.getResult())

visitor = EvalVisitor()
print(visitor.visit(tree))
