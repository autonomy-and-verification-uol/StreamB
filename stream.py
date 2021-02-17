from builder import *
from antlr4.error.ErrorListener import ErrorListener
import sys

class StreamErrorListener( ErrorListener ):

    def __init__(self):
        super(StreamErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax error: " + msg)

def resetTransducersFolder():
    folder = './transducers'
    if not os.path.exists(folder):
        os.mkdir(folder)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def parse(pattern):
    try:
        resetTransducersFolder()
        lexer = StreamLexer(InputStream(pattern))
        stream = CommonTokenStream(lexer)
        parser = StreamParser(stream)
        parser.addErrorListener(StreamErrorListener())
        tree = parser.propertyExpr()

        builder = StreamBuilder()
        builder.visit(tree)
        builder.createLaunch()
    except Exception as e:
        print(str(e))


def parseFile(file):
    with open(file, 'r') as content_file:
        pattern = content_file.read()
    parse(pattern)

def main(args):
    parseFile(args[1])

if __name__ == '__main__':
	main(sys.argv)
