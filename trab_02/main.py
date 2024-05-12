from antlr4 import *
from MinCLexer import MinCLexer
from MinCParser import MinCParser

file_name = input('? ')

with open(file_name, 'r') as f:

    input_stream = InputStream(''.join(f.readlines()))

    lexer = MinCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MinCParser(token_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))