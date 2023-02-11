# Generated from Jac.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from JacParser import JacParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2#")
        buf.write("\u00d3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\6\35\u00a8\n\35\r")
        buf.write("\35\16\35\u00a9\3\36\6\36\u00ad\n\36\r\36\16\36\u00ae")
        buf.write("\3\37\3\37\7\37\u00b3\n\37\f\37\16\37\u00b6\13\37\3\37")
        buf.write("\3\37\3 \3 \7 \u00bc\n \f \16 \u00bf\13 \3 \3 \3!\5!\u00c4")
        buf.write("\n!\3!\3!\7!\u00c8\n!\f!\16!\u00cb\13!\3\"\6\"\u00ce\n")
        buf.write("\"\r\"\16\"\u00cf\3\"\3\"\2\2#\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#\3\2\5\3\2$$\3\2\f\f\4\2\13\13\"\"")
        buf.write("\2\u00d9\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\3E\3\2\2\2\5H\3\2\2\2")
        buf.write("\7N\3\2\2\2\tV\3\2\2\2\13^\3\2\2\2\rd\3\2\2\2\17j\3\2")
        buf.write("\2\2\21s\3\2\2\2\23w\3\2\2\2\25~\3\2\2\2\27\u0080\3\2")
        buf.write("\2\2\31\u0082\3\2\2\2\33\u0084\3\2\2\2\35\u0086\3\2\2")
        buf.write("\2\37\u0088\3\2\2\2!\u008b\3\2\2\2#\u008e\3\2\2\2%\u0090")
        buf.write("\3\2\2\2\'\u0093\3\2\2\2)\u0095\3\2\2\2+\u0098\3\2\2\2")
        buf.write("-\u009a\3\2\2\2/\u009c\3\2\2\2\61\u009e\3\2\2\2\63\u00a0")
        buf.write("\3\2\2\2\65\u00a2\3\2\2\2\67\u00a4\3\2\2\29\u00a7\3\2")
        buf.write("\2\2;\u00ac\3\2\2\2=\u00b0\3\2\2\2?\u00b9\3\2\2\2A\u00c3")
        buf.write("\3\2\2\2C\u00cd\3\2\2\2EF\7k\2\2FG\7h\2\2G\4\3\2\2\2H")
        buf.write("I\7r\2\2IJ\7t\2\2JK\7k\2\2KL\7p\2\2LM\7v\2\2M\6\3\2\2")
        buf.write("\2NO\7t\2\2OP\7g\2\2PQ\7c\2\2QR\7f\2\2RS\7k\2\2ST\7p\2")
        buf.write("\2TU\7v\2\2U\b\3\2\2\2VW\7t\2\2WX\7g\2\2XY\7c\2\2YZ\7")
        buf.write("f\2\2Z[\7u\2\2[\\\7v\2\2\\]\7t\2\2]\n\3\2\2\2^_\7y\2\2")
        buf.write("_`\7j\2\2`a\7k\2\2ab\7n\2\2bc\7g\2\2c\f\3\2\2\2de\7d\2")
        buf.write("\2ef\7t\2\2fg\7g\2\2gh\7c\2\2hi\7m\2\2i\16\3\2\2\2jk\7")
        buf.write("e\2\2kl\7q\2\2lm\7p\2\2mn\7v\2\2no\7k\2\2op\7p\2\2pq\7")
        buf.write("w\2\2qr\7g\2\2r\20\3\2\2\2st\7f\2\2tu\7g\2\2uv\7h\2\2")
        buf.write("v\22\3\2\2\2wx\7t\2\2xy\7g\2\2yz\7v\2\2z{\7w\2\2{|\7t")
        buf.write("\2\2|}\7p\2\2}\24\3\2\2\2~\177\7-\2\2\177\26\3\2\2\2\u0080")
        buf.write("\u0081\7/\2\2\u0081\30\3\2\2\2\u0082\u0083\7,\2\2\u0083")
        buf.write("\32\3\2\2\2\u0084\u0085\7\61\2\2\u0085\34\3\2\2\2\u0086")
        buf.write("\u0087\7\'\2\2\u0087\36\3\2\2\2\u0088\u0089\7?\2\2\u0089")
        buf.write("\u008a\7?\2\2\u008a \3\2\2\2\u008b\u008c\7#\2\2\u008c")
        buf.write("\u008d\7?\2\2\u008d\"\3\2\2\2\u008e\u008f\7@\2\2\u008f")
        buf.write("$\3\2\2\2\u0090\u0091\7@\2\2\u0091\u0092\7?\2\2\u0092")
        buf.write("&\3\2\2\2\u0093\u0094\7>\2\2\u0094(\3\2\2\2\u0095\u0096")
        buf.write("\7>\2\2\u0096\u0097\7?\2\2\u0097*\3\2\2\2\u0098\u0099")
        buf.write("\7*\2\2\u0099,\3\2\2\2\u009a\u009b\7+\2\2\u009b.\3\2\2")
        buf.write("\2\u009c\u009d\7}\2\2\u009d\60\3\2\2\2\u009e\u009f\7\177")
        buf.write("\2\2\u009f\62\3\2\2\2\u00a0\u00a1\7<\2\2\u00a1\64\3\2")
        buf.write("\2\2\u00a2\u00a3\7?\2\2\u00a3\66\3\2\2\2\u00a4\u00a5\7")
        buf.write(".\2\2\u00a58\3\2\2\2\u00a6\u00a8\4c|\2\u00a7\u00a6\3\2")
        buf.write("\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa:\3\2\2\2\u00ab\u00ad\4\62;\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af<\3\2\2\2\u00b0\u00b4\7$\2\2\u00b1")
        buf.write("\u00b3\n\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2")
        buf.write("\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b7\3")
        buf.write("\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8\7$\2\2\u00b8>\3")
        buf.write("\2\2\2\u00b9\u00bd\7%\2\2\u00ba\u00bc\n\3\2\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00c0\u00c1\b \2\2\u00c1@\3\2\2\2\u00c2\u00c4\7\17\2")
        buf.write("\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\u00c9\7\f\2\2\u00c6\u00c8\7\"\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00caB\3\2\2\2\u00cb\u00c9\3\2\2")
        buf.write("\2\u00cc\u00ce\t\4\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\u00d2\b\"\2\2\u00d2D\3\2\2\2\n\2")
        buf.write("\u00a9\u00ae\u00b4\u00bd\u00c3\u00c9\u00cf\3\b\2\2")
        return buf.getvalue()


class JacLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    PRINT = 2
    READINT = 3
    READSTR = 4
    WHILE = 5
    BREAK = 6
    CONTINUE = 7
    DEF = 8
    RETURN = 9
    PLUS = 10
    MINUS = 11
    TIMES = 12
    OVER = 13
    REM = 14
    EQ = 15
    NE = 16
    GT = 17
    GE = 18
    LT = 19
    LE = 20
    OP_PAR = 21
    CL_PAR = 22
    OP_CUR = 23
    CL_CUR = 24
    COLON = 25
    ATTRIB = 26
    COMMA = 27
    NAME = 28
    NUMBER = 29
    STRING = 30
    COMMENT = 31
    NL = 32
    SPACE = 33

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'print'", "'readint'", "'readstr'", "'while'", "'break'", 
            "'continue'", "'def'", "'return'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'('", 
            "')'", "'{'", "'}'", "':'", "'='", "','" ]

    symbolicNames = [ "<INVALID>",
            "IF", "PRINT", "READINT", "READSTR", "WHILE", "BREAK", "CONTINUE", 
            "DEF", "RETURN", "PLUS", "MINUS", "TIMES", "OVER", "REM", "EQ", 
            "NE", "GT", "GE", "LT", "LE", "OP_PAR", "CL_PAR", "OP_CUR", 
            "CL_CUR", "COLON", "ATTRIB", "COMMA", "NAME", "NUMBER", "STRING", 
            "COMMENT", "NL", "SPACE" ]

    ruleNames = [ "IF", "PRINT", "READINT", "READSTR", "WHILE", "BREAK", 
                  "CONTINUE", "DEF", "RETURN", "PLUS", "MINUS", "TIMES", 
                  "OVER", "REM", "EQ", "NE", "GT", "GE", "LT", "LE", "OP_PAR", 
                  "CL_PAR", "OP_CUR", "CL_CUR", "COLON", "ATTRIB", "COMMA", 
                  "NAME", "NUMBER", "STRING", "COMMENT", "NL", "SPACE" ]

    grammarFileName = "Jac.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class JacDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: JacLexer = lexer

        def pull_token(self):
            return super(JacLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.JacDenter(self, self.NL, JacParser.INDENT, JacParser.DEDENT, False)
        return self.denter.next_token()

    def getVariableType(self, name):
        for i in range(len(self.symbolTable)):
            if self.symbolTable[i] == name:
                return self.typeOfTable[i]

        sys.stderr.write('ERROR: Variable ' + name + ' not declared')
        sys.exit(1)


