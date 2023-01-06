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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u00a5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\6\27")
        buf.write("z\n\27\r\27\16\27{\3\30\6\30\177\n\30\r\30\16\30\u0080")
        buf.write("\3\31\3\31\7\31\u0085\n\31\f\31\16\31\u0088\13\31\3\31")
        buf.write("\3\31\3\32\3\32\7\32\u008e\n\32\f\32\16\32\u0091\13\32")
        buf.write("\3\32\3\32\3\33\5\33\u0096\n\33\3\33\3\33\7\33\u009a\n")
        buf.write("\33\f\33\16\33\u009d\13\33\3\34\6\34\u00a0\n\34\r\34\16")
        buf.write("\34\u00a1\3\34\3\34\2\2\35\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35\3\2")
        buf.write("\5\3\2$$\3\2\f\f\4\2\13\13\"\"\2\u00ab\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\39\3\2")
        buf.write("\2\2\5<\3\2\2\2\7B\3\2\2\2\tJ\3\2\2\2\13R\3\2\2\2\rT\3")
        buf.write("\2\2\2\17V\3\2\2\2\21X\3\2\2\2\23Z\3\2\2\2\25\\\3\2\2")
        buf.write("\2\27_\3\2\2\2\31b\3\2\2\2\33d\3\2\2\2\35g\3\2\2\2\37")
        buf.write("i\3\2\2\2!l\3\2\2\2#n\3\2\2\2%p\3\2\2\2\'r\3\2\2\2)t\3")
        buf.write("\2\2\2+v\3\2\2\2-y\3\2\2\2/~\3\2\2\2\61\u0082\3\2\2\2")
        buf.write("\63\u008b\3\2\2\2\65\u0095\3\2\2\2\67\u009f\3\2\2\29:")
        buf.write("\7k\2\2:;\7h\2\2;\4\3\2\2\2<=\7r\2\2=>\7t\2\2>?\7k\2\2")
        buf.write("?@\7p\2\2@A\7v\2\2A\6\3\2\2\2BC\7t\2\2CD\7g\2\2DE\7c\2")
        buf.write("\2EF\7f\2\2FG\7k\2\2GH\7p\2\2HI\7v\2\2I\b\3\2\2\2JK\7")
        buf.write("t\2\2KL\7g\2\2LM\7c\2\2MN\7f\2\2NO\7u\2\2OP\7v\2\2PQ\7")
        buf.write("t\2\2Q\n\3\2\2\2RS\7-\2\2S\f\3\2\2\2TU\7/\2\2U\16\3\2")
        buf.write("\2\2VW\7,\2\2W\20\3\2\2\2XY\7\61\2\2Y\22\3\2\2\2Z[\7\'")
        buf.write("\2\2[\24\3\2\2\2\\]\7?\2\2]^\7?\2\2^\26\3\2\2\2_`\7#\2")
        buf.write("\2`a\7?\2\2a\30\3\2\2\2bc\7@\2\2c\32\3\2\2\2de\7@\2\2")
        buf.write("ef\7?\2\2f\34\3\2\2\2gh\7>\2\2h\36\3\2\2\2ij\7>\2\2jk")
        buf.write("\7?\2\2k \3\2\2\2lm\7*\2\2m\"\3\2\2\2no\7+\2\2o$\3\2\2")
        buf.write("\2pq\7}\2\2q&\3\2\2\2rs\7\177\2\2s(\3\2\2\2tu\7?\2\2u")
        buf.write("*\3\2\2\2vw\7.\2\2w,\3\2\2\2xz\4c|\2yx\3\2\2\2z{\3\2\2")
        buf.write("\2{y\3\2\2\2{|\3\2\2\2|.\3\2\2\2}\177\4\62;\2~}\3\2\2")
        buf.write("\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2")
        buf.write("\2\u0081\60\3\2\2\2\u0082\u0086\7$\2\2\u0083\u0085\n\2")
        buf.write("\2\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0089\u008a\7$\2\2\u008a\62\3\2\2\2\u008b")
        buf.write("\u008f\7%\2\2\u008c\u008e\n\3\2\2\u008d\u008c\3\2\2\2")
        buf.write("\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3")
        buf.write("\2\2\2\u0090\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093")
        buf.write("\b\32\2\2\u0093\64\3\2\2\2\u0094\u0096\7\17\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u009b\7\f\2\2\u0098\u009a\7\"\2\2\u0099\u0098\3")
        buf.write("\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\66\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0")
        buf.write("\t\4\2\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\b\34\2\2\u00a48\3\2\2\2\n\2{\u0080\u0086")
        buf.write("\u008f\u0095\u009b\u00a1\3\b\2\2")
        return buf.getvalue()


class JacLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    PRINT = 2
    READINT = 3
    READSTR = 4
    PLUS = 5
    MINUS = 6
    TIMES = 7
    OVER = 8
    REM = 9
    EQ = 10
    NE = 11
    GT = 12
    GE = 13
    LT = 14
    LE = 15
    OP_PAR = 16
    CL_PAR = 17
    OP_CUR = 18
    CL_CUR = 19
    ATTRIB = 20
    COMMA = 21
    NAME = 22
    NUMBER = 23
    STRING = 24
    COMMENT = 25
    NL = 26
    SPACE = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'print'", "'readint'", "'readstr'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", 
            "'('", "')'", "'{'", "'}'", "'='", "','" ]

    symbolicNames = [ "<INVALID>",
            "IF", "PRINT", "READINT", "READSTR", "PLUS", "MINUS", "TIMES", 
            "OVER", "REM", "EQ", "NE", "GT", "GE", "LT", "LE", "OP_PAR", 
            "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", "COMMA", "NAME", "NUMBER", 
            "STRING", "COMMENT", "NL", "SPACE" ]

    ruleNames = [ "IF", "PRINT", "READINT", "READSTR", "PLUS", "MINUS", 
                  "TIMES", "OVER", "REM", "EQ", "NE", "GT", "GE", "LT", 
                  "LE", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", 
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


