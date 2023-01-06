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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u00ad\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\6\30\u0082\n\30\r\30\16")
        buf.write("\30\u0083\3\31\6\31\u0087\n\31\r\31\16\31\u0088\3\32\3")
        buf.write("\32\7\32\u008d\n\32\f\32\16\32\u0090\13\32\3\32\3\32\3")
        buf.write("\33\3\33\7\33\u0096\n\33\f\33\16\33\u0099\13\33\3\33\3")
        buf.write("\33\3\34\5\34\u009e\n\34\3\34\3\34\7\34\u00a2\n\34\f\34")
        buf.write("\16\34\u00a5\13\34\3\35\6\35\u00a8\n\35\r\35\16\35\u00a9")
        buf.write("\3\35\3\35\2\2\36\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36\3\2\5\3\2")
        buf.write("$$\3\2\f\f\4\2\13\13\"\"\2\u00b3\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\3")
        buf.write(";\3\2\2\2\5>\3\2\2\2\7D\3\2\2\2\tL\3\2\2\2\13T\3\2\2\2")
        buf.write("\rZ\3\2\2\2\17\\\3\2\2\2\21^\3\2\2\2\23`\3\2\2\2\25b\3")
        buf.write("\2\2\2\27d\3\2\2\2\31g\3\2\2\2\33j\3\2\2\2\35l\3\2\2\2")
        buf.write("\37o\3\2\2\2!q\3\2\2\2#t\3\2\2\2%v\3\2\2\2\'x\3\2\2\2")
        buf.write(")z\3\2\2\2+|\3\2\2\2-~\3\2\2\2/\u0081\3\2\2\2\61\u0086")
        buf.write("\3\2\2\2\63\u008a\3\2\2\2\65\u0093\3\2\2\2\67\u009d\3")
        buf.write("\2\2\29\u00a7\3\2\2\2;<\7k\2\2<=\7h\2\2=\4\3\2\2\2>?\7")
        buf.write("r\2\2?@\7t\2\2@A\7k\2\2AB\7p\2\2BC\7v\2\2C\6\3\2\2\2D")
        buf.write("E\7t\2\2EF\7g\2\2FG\7c\2\2GH\7f\2\2HI\7k\2\2IJ\7p\2\2")
        buf.write("JK\7v\2\2K\b\3\2\2\2LM\7t\2\2MN\7g\2\2NO\7c\2\2OP\7f\2")
        buf.write("\2PQ\7u\2\2QR\7v\2\2RS\7t\2\2S\n\3\2\2\2TU\7y\2\2UV\7")
        buf.write("j\2\2VW\7k\2\2WX\7n\2\2XY\7g\2\2Y\f\3\2\2\2Z[\7-\2\2[")
        buf.write("\16\3\2\2\2\\]\7/\2\2]\20\3\2\2\2^_\7,\2\2_\22\3\2\2\2")
        buf.write("`a\7\61\2\2a\24\3\2\2\2bc\7\'\2\2c\26\3\2\2\2de\7?\2\2")
        buf.write("ef\7?\2\2f\30\3\2\2\2gh\7#\2\2hi\7?\2\2i\32\3\2\2\2jk")
        buf.write("\7@\2\2k\34\3\2\2\2lm\7@\2\2mn\7?\2\2n\36\3\2\2\2op\7")
        buf.write(">\2\2p \3\2\2\2qr\7>\2\2rs\7?\2\2s\"\3\2\2\2tu\7*\2\2")
        buf.write("u$\3\2\2\2vw\7+\2\2w&\3\2\2\2xy\7}\2\2y(\3\2\2\2z{\7\177")
        buf.write("\2\2{*\3\2\2\2|}\7?\2\2},\3\2\2\2~\177\7.\2\2\177.\3\2")
        buf.write("\2\2\u0080\u0082\4c|\2\u0081\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\60\3\2\2\2\u0085\u0087\4\62;\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\62\3\2\2\2\u008a\u008e\7$\2\2\u008b\u008d\n\2\2")
        buf.write("\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0091\u0092\7$\2\2\u0092\64\3\2\2\2\u0093")
        buf.write("\u0097\7%\2\2\u0094\u0096\n\3\2\2\u0095\u0094\3\2\2\2")
        buf.write("\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3")
        buf.write("\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b")
        buf.write("\b\33\2\2\u009b\66\3\2\2\2\u009c\u009e\7\17\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a3\7\f\2\2\u00a0\u00a2\7\"\2\2\u00a1\u00a0\3")
        buf.write("\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a48\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8")
        buf.write("\t\4\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\b\35\2\2\u00ac:\3\2\2\2\n\2\u0083\u0088\u008e")
        buf.write("\u0097\u009d\u00a3\u00a9\3\b\2\2")
        return buf.getvalue()


class JacLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    PRINT = 2
    READINT = 3
    READSTR = 4
    WHILE = 5
    PLUS = 6
    MINUS = 7
    TIMES = 8
    OVER = 9
    REM = 10
    EQ = 11
    NE = 12
    GT = 13
    GE = 14
    LT = 15
    LE = 16
    OP_PAR = 17
    CL_PAR = 18
    OP_CUR = 19
    CL_CUR = 20
    ATTRIB = 21
    COMMA = 22
    NAME = 23
    NUMBER = 24
    STRING = 25
    COMMENT = 26
    NL = 27
    SPACE = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'print'", "'readint'", "'readstr'", "'while'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>'", "'>='", "'<'", 
            "'<='", "'('", "')'", "'{'", "'}'", "'='", "','" ]

    symbolicNames = [ "<INVALID>",
            "IF", "PRINT", "READINT", "READSTR", "WHILE", "PLUS", "MINUS", 
            "TIMES", "OVER", "REM", "EQ", "NE", "GT", "GE", "LT", "LE", 
            "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", "COMMA", "NAME", 
            "NUMBER", "STRING", "COMMENT", "NL", "SPACE" ]

    ruleNames = [ "IF", "PRINT", "READINT", "READSTR", "WHILE", "PLUS", 
                  "MINUS", "TIMES", "OVER", "REM", "EQ", "NE", "GT", "GE", 
                  "LT", "LE", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", 
                  "COMMA", "NAME", "NUMBER", "STRING", "COMMENT", "NL", 
                  "SPACE" ]

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


