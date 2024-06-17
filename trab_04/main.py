import sys
from antlr4 import CommonTokenStream, InputStream
from HtmlLexer import HtmlLexer
from HtmlParser import HtmlParser
from Visitor import Visitor


with open(sys.argv[1], "r") as f:
    input_stream = InputStream("".join(f.readlines()))

lexer = HtmlLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = HtmlParser(token_stream)
tree = parser.root()

visitor = Visitor()

with open("out.html", "w") as f:
    f.write(visitor.visit(tree))
