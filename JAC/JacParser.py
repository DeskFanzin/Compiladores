# Generated from Jac.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import sys
symbol_table = []
stack_cur = 0
stack_max = 0
def emit(bytecode, delta):
    global stack_cur, stack_max
    print('    '+ bytecode + '    ; delta=' + str(delta))
    stack_cur += delta
    if stack_cur > stack_max:
        stack_max = stack_cur


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("\u0098\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\3\3\3\6\3 \n\3\r\3\16\3!\3\3\3\3\3\4\3\4\3")
        buf.write("\4\5\4)\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7")
        buf.write("\5\65\n\5\f\5\16\58\13\5\5\5:\n\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\6\7I\n\7\r\7\16\7J\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\6\t[\n\t\r\t\16\t\\\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\7\13l\n\13\f\13\16\13o\13\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\5\fw\n\f\3\f\3\f\3\f\7\f|\n\f")
        buf.write("\f\f\16\f\177\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0096")
        buf.write("\n\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\4\3\2")
        buf.write("\r\22\3\2\b\t\2\u009b\2\32\3\2\2\2\4\35\3\2\2\2\6(\3\2")
        buf.write("\2\2\b*\3\2\2\2\n>\3\2\2\2\fC\3\2\2\2\16O\3\2\2\2\20T")
        buf.write("\3\2\2\2\22a\3\2\2\2\24f\3\2\2\2\26r\3\2\2\2\30\u0095")
        buf.write("\3\2\2\2\32\33\b\2\1\2\33\34\5\4\3\2\34\3\3\2\2\2\35\37")
        buf.write("\b\3\1\2\36 \5\6\4\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2")
        buf.write("\2!\"\3\2\2\2\"#\3\2\2\2#$\b\3\1\2$\5\3\2\2\2%)\7\35\2")
        buf.write("\2&)\5\b\5\2\')\5\n\6\2(%\3\2\2\2(&\3\2\2\2(\'\3\2\2\2")
        buf.write(")\7\3\2\2\2*+\7\4\2\2+9\7\23\2\2,-\b\5\1\2-.\5\24\13\2")
        buf.write(".\66\b\5\1\2/\60\7\30\2\2\60\61\b\5\1\2\61\62\5\24\13")
        buf.write("\2\62\63\b\5\1\2\63\65\3\2\2\2\64/\3\2\2\2\658\3\2\2\2")
        buf.write("\66\64\3\2\2\2\66\67\3\2\2\2\67:\3\2\2\28\66\3\2\2\29")
        buf.write(",\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\7\24\2\2<=\b\5\1\2=\t")
        buf.write("\3\2\2\2>?\7\31\2\2?@\7\27\2\2@A\5\24\13\2AB\b\6\1\2B")
        buf.write("\13\3\2\2\2CD\7\3\2\2DE\5\16\b\2EF\b\7\1\2FH\7\25\2\2")
        buf.write("GI\5\6\4\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3")
        buf.write("\2\2\2LM\b\7\1\2MN\7\26\2\2N\r\3\2\2\2OP\5\24\13\2PQ\t")
        buf.write("\2\2\2QR\5\24\13\2RS\b\b\1\2S\17\3\2\2\2TU\7\7\2\2UV\b")
        buf.write("\t\1\2VW\5\22\n\2WX\b\t\1\2XZ\7\25\2\2Y[\5\6\4\2ZY\3\2")
        buf.write("\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^_\b\t")
        buf.write("\1\2_`\7\26\2\2`\21\3\2\2\2ab\5\24\13\2bc\t\2\2\2cd\5")
        buf.write("\24\13\2de\b\n\1\2e\23\3\2\2\2fm\5\26\f\2gh\t\3\2\2hi")
        buf.write("\5\26\f\2ij\b\13\1\2jl\3\2\2\2kg\3\2\2\2lo\3\2\2\2mk\3")
        buf.write("\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2pq\b\13\1\2q\25\3")
        buf.write("\2\2\2r}\5\30\r\2sw\7\n\2\2tw\7\13\2\2uw\7\f\2\2vs\3\2")
        buf.write("\2\2vt\3\2\2\2vu\3\2\2\2wx\3\2\2\2xy\5\30\r\2yz\b\f\1")
        buf.write("\2z|\3\2\2\2{v\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2")
        buf.write("\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0081\b\f\1\2\u0081")
        buf.write("\27\3\2\2\2\u0082\u0083\7\32\2\2\u0083\u0096\b\r\1\2\u0084")
        buf.write("\u0085\7\33\2\2\u0085\u0096\b\r\1\2\u0086\u0087\7\23\2")
        buf.write("\2\u0087\u0088\5\24\13\2\u0088\u0089\7\24\2\2\u0089\u008a")
        buf.write("\b\r\1\2\u008a\u0096\3\2\2\2\u008b\u008c\7\31\2\2\u008c")
        buf.write("\u0096\b\r\1\2\u008d\u008e\7\5\2\2\u008e\u008f\7\23\2")
        buf.write("\2\u008f\u0090\7\24\2\2\u0090\u0096\b\r\1\2\u0091\u0092")
        buf.write("\7\6\2\2\u0092\u0093\7\23\2\2\u0093\u0094\7\24\2\2\u0094")
        buf.write("\u0096\b\r\1\2\u0095\u0082\3\2\2\2\u0095\u0084\3\2\2\2")
        buf.write("\u0095\u0086\3\2\2\2\u0095\u008b\3\2\2\2\u0095\u008d\3")
        buf.write("\2\2\2\u0095\u0091\3\2\2\2\u0096\31\3\2\2\2\f!(\669J\\")
        buf.write("mv}\u0095")
        return buf.getvalue()


class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'print'", "'readint'", "'readstr'", 
                     "'while'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'>'", "'>='", "'<'", "'<='", "'('", "')'", 
                     "'{'", "'}'", "'='", "','" ]

    symbolicNames = [ "<INVALID>", "IF", "PRINT", "READINT", "READSTR", 
                      "WHILE", "PLUS", "MINUS", "TIMES", "OVER", "REM", 
                      "EQ", "NE", "GT", "GE", "LT", "LE", "OP_PAR", "CL_PAR", 
                      "OP_CUR", "CL_CUR", "ATTRIB", "COMMA", "NAME", "NUMBER", 
                      "STRING", "COMMENT", "NL", "SPACE", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_st_if = 5
    RULE_comparison_if = 6
    RULE_st_while = 7
    RULE_comparison_while = 8
    RULE_expression = 9
    RULE_term = 10
    RULE_factor = 11

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "st_if", "comparison_if", "st_while", "comparison_while", 
                   "expression", "term", "factor" ]

    EOF = Token.EOF
    IF=1
    PRINT=2
    READINT=3
    READSTR=4
    WHILE=5
    PLUS=6
    MINUS=7
    TIMES=8
    OVER=9
    REM=10
    EQ=11
    NE=12
    GT=13
    GE=14
    LT=15
    LE=16
    OP_PAR=17
    CL_PAR=18
    OP_CUR=19
    CL_CUR=20
    ATTRIB=21
    COMMA=22
    NAME=23
    NUMBER=24
    STRING=25
    COMMENT=26
    NL=27
    SPACE=28
    INDENT=29
    DEDENT=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(JacParser.MainContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_program




    def program(self):

        localctx = JacParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    print('.source Test.src')
                    print('.class  public Test')
                    print('.super  java/lang/Object\n')
                    print('.method public <init>()V')
                    print('    aload_0')
                    print('    invokenonvirtual java/lang/Object/<init>()V')
                    print('    return')
                    print('.end method\n')
                
            self.state = 25
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_main




    def main(self):

        localctx = JacParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.statement()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    print('    return')
                    print('.limit stack 10')
                    print('.end method')
                    print('\n; symbol_table:', symbol_table)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(JacParser.NL, 0)

        def st_print(self):
            return self.getTypedRuleContext(JacParser.St_printContext,0)


        def st_attrib(self):
            return self.getTypedRuleContext(JacParser.St_attribContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.NL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(JacParser.NL)
                pass
            elif token in [JacParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.st_print()
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.st_attrib()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e1 = None # ExpressionContext

        def PRINT(self):
            return self.getToken(JacParser.PRINT, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.COMMA)
            else:
                return self.getToken(JacParser.COMMA, i)

        def getRuleIndex(self):
            return JacParser.RULE_st_print




    def st_print(self):

        localctx = JacParser.St_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_st_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(JacParser.PRINT)
            self.state = 41
            self.match(JacParser.OP_PAR)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                if 1:
                        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 43
                localctx.e1 = self.expression()
                if 1:
                        if localctx.e1.type == 'i':
                            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                        elif localctx.e1.type == 's':
                            emit ('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                        else:
                            print('*****HELP*****')
                    
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JacParser.COMMA:
                    self.state = 45
                    self.match(JacParser.COMMA)
                    if 1:
                            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                            
                    self.state = 47
                    self.expression()
                    if 1:
                            emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                            
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 57
            self.match(JacParser.CL_PAR)
            if 1:
                    emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    emit('    invokevirtual java/io/PrintStream/println()V\n', -1)
                    
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_attribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def ATTRIB(self):
            return self.getToken(JacParser.ATTRIB, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_st_attrib




    def st_attrib(self):

        localctx = JacParser.St_attribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(JacParser.NAME)
            self.state = 61
            self.match(JacParser.ATTRIB)
            self.state = 62
            self.expression()
            if 1:
                    print('    istore 0')
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(JacParser.IF, 0)

        def comparison_if(self):
            return self.getTypedRuleContext(JacParser.Comparison_ifContext,0)


        def OP_CUR(self):
            return self.getToken(JacParser.OP_CUR, 0)

        def CL_CUR(self):
            return self.getToken(JacParser.CL_CUR, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_st_if




    def st_if(self):

        localctx = JacParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(JacParser.IF)
            self.state = 66
            self.comparison_if()
            if 1:
                    global x 
                    local_x = x
                    x += 1
                
            self.state = 68
            self.match(JacParser.OP_CUR)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.statement()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    print('NOT_IF_' + str(local_x) + ':')
                
            self.state = 75
            self.match(JacParser.CL_CUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(JacParser.EQ, 0)

        def NE(self):
            return self.getToken(JacParser.NE, 0)

        def GT(self):
            return self.getToken(JacParser.GT, 0)

        def GE(self):
            return self.getToken(JacParser.GE, 0)

        def LT(self):
            return self.getToken(JacParser.LT, 0)

        def LE(self):
            return self.getToken(JacParser.LE, 0)

        def getRuleIndex(self):
            return JacParser.RULE_comparison_if




    def comparison_if(self):

        localctx = JacParser.Comparison_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.expression()
            self.state = 78
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 79
            self.expression()
            if 1:
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.EQ:
                        emit ('if_icmpne NOT_IF_' + str(x), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.NE:
                        emit ('if_icmpeq NOT_IF_' + str(x), -2)    
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GT:
                        emit ('if_icmple NOT_IF_' + str(x), -2)      
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GE:
                        emit ('if_icmplt NOT_IF_' + str(x), -2)   
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LT:
                        emit ('if_icmpge NOT_IF_' + str(x), -2)     
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LE:
                        emit ('if_icmpgt NOT_IF_' + str(x), -2)                 
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(JacParser.WHILE, 0)

        def comparison_while(self):
            return self.getTypedRuleContext(JacParser.Comparison_whileContext,0)


        def OP_CUR(self):
            return self.getToken(JacParser.OP_CUR, 0)

        def CL_CUR(self):
            return self.getToken(JacParser.CL_CUR, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_st_while




    def st_while(self):

        localctx = JacParser.St_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_st_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(JacParser.WHILE)
            if 1:
                    global y 
                    local_y = y
                    print('BEGIN_WHILE_' + str(local_y) + ':')
                
            self.state = 84
            self.comparison_while()
            if 1:
                    y += 1
                
            self.state = 86
            self.match(JacParser.OP_CUR)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.statement()
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    emit('goto BEGIN_WHILE_' + str(local_y), 0)
                    print('END_WHILE_' + str(local_y) + ':')
                
            self.state = 93
            self.match(JacParser.CL_CUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(JacParser.EQ, 0)

        def NE(self):
            return self.getToken(JacParser.NE, 0)

        def GT(self):
            return self.getToken(JacParser.GT, 0)

        def GE(self):
            return self.getToken(JacParser.GE, 0)

        def LT(self):
            return self.getToken(JacParser.LT, 0)

        def LE(self):
            return self.getToken(JacParser.LE, 0)

        def getRuleIndex(self):
            return JacParser.RULE_comparison_while




    def comparison_while(self):

        localctx = JacParser.Comparison_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparison_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.expression()
            self.state = 96
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 97
            self.expression()
            if 1:
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.EQ:
                        emit ('if_icmpne END_WHILE_' + str(x), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.NE:
                        emit ('if_icmpeq END_WHILE_' + str(x), -2)    
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GT:
                        emit ('if_icmple END_WHILE_' + str(x), -2)      
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GE:
                        emit ('if_icmplt END_WHILE_' + str(x), -2)   
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LT:
                        emit ('if_icmpge END_WHILE_' + str(x), -2)     
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LE:
                        emit ('if_icmpgt END_WHILE_' + str(x), -2)                 
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.t1 = None # TermContext
            self.op = None # Token
            self.t2 = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.TermContext)
            else:
                return self.getTypedRuleContext(JacParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.PLUS)
            else:
                return self.getToken(JacParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.MINUS)
            else:
                return self.getToken(JacParser.MINUS, i)

        def getRuleIndex(self):
            return JacParser.RULE_expression




    def expression(self):

        localctx = JacParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            localctx.t1 = self.term()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.PLUS or _la==JacParser.MINUS:
                self.state = 101
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==JacParser.PLUS or _la==JacParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 102
                localctx.t2 = self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            print('    iadd')
                        else:
                            print('    isub')    
                    
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    localctx.type = localctx.t1.type
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self._factor = None # FactorContext
            self.op = None # Token

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.FactorContext)
            else:
                return self.getTypedRuleContext(JacParser.FactorContext,i)


        def OVER(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.OVER)
            else:
                return self.getToken(JacParser.OVER, i)

        def REM(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.REM)
            else:
                return self.getToken(JacParser.REM, i)

        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.TIMES)
            else:
                return self.getToken(JacParser.TIMES, i)

        def getRuleIndex(self):
            return JacParser.RULE_term




    def term(self):

        localctx = JacParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            localctx._factor = self.factor()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0):
                self.state = 116
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JacParser.TIMES]:
                    self.state = 113
                    localctx.op = self.match(JacParser.TIMES)
                    pass
                elif token in [JacParser.OVER]:
                    self.state = 114
                    self.match(JacParser.OVER)
                    pass
                elif token in [JacParser.REM]:
                    self.state = 115
                    self.match(JacParser.REM)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 118
                localctx._factor = self.factor()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                            print('    imul')
                        elif (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                            print('    idiv')
                        else:
                            print('    irem')
                    
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    localctx.type = localctx._factor.type
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self._NUMBER = None # Token
            self._STRING = None # Token
            self.e = None # ExpressionContext

        def NUMBER(self):
            return self.getToken(JacParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(JacParser.STRING, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def READINT(self):
            return self.getToken(JacParser.READINT, 0)

        def READSTR(self):
            return self.getToken(JacParser.READSTR, 0)

        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                        localctx.type = 'i'

                    
                pass
            elif token in [JacParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                localctx._STRING = self.match(JacParser.STRING)
                if 1:
                        emit('ldc ' + (None if localctx._STRING is None else localctx._STRING.text), +1)
                        localctx.type = 's'
                    
                pass
            elif token in [JacParser.OP_PAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(JacParser.OP_PAR)
                self.state = 133
                localctx.e = self.expression()
                self.state = 134
                self.match(JacParser.CL_PAR)
                if 1:
                        localctx.type = e.type
                    
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 4)
                self.state = 137
                self.match(JacParser.NAME)
                if 1:
                        pass
                    
                pass
            elif token in [JacParser.READINT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.match(JacParser.READINT)
                self.state = 140
                self.match(JacParser.OP_PAR)
                self.state = 141
                self.match(JacParser.CL_PAR)
                if 1:
                        #geração de código de leitura de inteiro
                        emit('    invokestatic Runtime/readInt()I', +1)
                        localctx.type = 'i'
                    
                pass
            elif token in [JacParser.READSTR]:
                self.enterOuterAlt(localctx, 6)
                self.state = 143
                self.match(JacParser.READSTR)
                self.state = 144
                self.match(JacParser.OP_PAR)
                self.state = 145
                self.match(JacParser.CL_PAR)
                if 1:
                        #geração de código de leitura de string
                        emit('    invokestatic Runtime/readString()Ljava/lang/String;', +1)
                        localctx.type = 's'
                    
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





