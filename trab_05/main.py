"""
    This is the main module.

    This module heads the inpput file and instanciates a Visitor implemented
    class that does the semantic analisys if the grammar.

    @authors: Victor Hugo, Aldemir Silva, Nilson Andrade
"""

import os
import sys

from antlr4 import CommonTokenStream, InputStream
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from visitor import Visitor

with open(sys.argv[1], "r", encoding="utf-8") as f:

    input_stream = InputStream("".join(f.readlines()))

    lexer = MiniCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniCParser(token_stream)

    tree = parser.program()

    visitor = Visitor(os.path.basename(sys.argv[1]))

    erros = visitor.visit(tree)

    for error in erros:
        print(error)
