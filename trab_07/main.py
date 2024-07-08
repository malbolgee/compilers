"""
    This is the main module.

    This module heads the inpput file and instanciates a Visitor implemented
    class that does the semantic analysis if the grammar.

    @authors: Victor Hugo, Aldemir Silva, Nilson Andrade
"""

import os
import sys

from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener
from codegen import GenAssemblyMIPS
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from visitor import IntermediateCodeVisitor, SemanticVisitor


class SyntaxErrorListener(ErrorListener):
    def __init__(self, file_name: str) -> None:
        super().__init__()
        self.__file_name = file_name

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e) -> None:
        print(
            f"{self.__file_name}:{line}:{column}: \033[91merror:\033[00m {msg}",
            file=sys.stderr,
        )
        self.__underlineError(recognizer, offendingSymbol, line, column)

    def __underlineError(self, recognizer, offendingToken, line, colmun):
        tokens = recognizer.getInputStream()
        input = str(tokens.tokenSource.inputStream)
        lines = input.split("\n")
        errorLine = lines[line - 1]
        print(
            errorLine.replace(
                offendingToken.text, f"\033[91m{offendingToken.text}\033[00m"
            ),
            file=sys.stderr,
        )
        print("\033[91m" + ("~" * colmun), file=sys.stderr, end="")
        start = offendingToken.start
        stop = offendingToken.stop
        if start >= 0 and stop >= 0:
            print(("^" * ((stop - start) + 1)) + "\033[00m", file=sys.stderr)


def main():

    input_stream = FileStream(sys.argv[1])
    lexer = MiniCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniCParser(token_stream)

    file_name: str = os.path.basename(sys.argv[1])

    parser.removeErrorListeners()
    parser.addErrorListener(SyntaxErrorListener(file_name))

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        return

    errors = SemanticVisitor(file_name).visit(tree)

    for error in errors:
        print(error, file=sys.stderr)

    intermediate_file_name = os.path.splitext(file_name)[0] + ".i"
    assembly_file_name = os.path.splitext(file_name)[0] + ".s"
    if len(errors) == 0:
        with open(intermediate_file_name, "w+", encoding="utf-8") as out:
            IntermediateCodeVisitor(out).visit(tree)

        with open(assembly_file_name, "w+", encoding="utf-8") as out:
            GenAssemblyMIPS(intermediate_file_name, out).generate()


if __name__ == "__main__":
    main()
