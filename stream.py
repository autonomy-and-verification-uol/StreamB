
from builder import *

def parse(pattern):
    lexer = StreamLexer(InputStream(pattern))
    stream = CommonTokenStream(lexer)
    parser = StreamParser(stream)
    tree = parser.propertyExpr()

    builder = StreamBuilder()
    builder.visit(tree)
    builder.createLaunch()
