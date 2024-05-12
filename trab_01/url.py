from antlr4 import *
from URLLexer import URLLexer
from URLParser import URLParser

input_stream = InputStream(input('? '))
lexer = URLLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = URLParser(token_stream)
tree = parser.program()
print(tree.toStringTree(recog=parser))