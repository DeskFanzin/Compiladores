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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write("\u00a6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\6\3$\n\3\r\3\16\3")
        buf.write("%\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\61\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5=\n\5\f\5\16\5@")
        buf.write("\13\5\5\5B\n\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\6\7Q\n\7\r\7\16\7R\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\6\tc\n\t\r\t\16\td")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\7\rz\n\r\f\r\16\r}\13\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\5\16\u0085\n\16\3\16\3\16\3\16")
        buf.write("\7\16\u008a\n\16\f\16\16\16\u008d\13\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00a4\n\17\3")
        buf.write("\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\4\3\2")
        buf.write("\17\24\3\2\n\13\2\u00ab\2\36\3\2\2\2\4!\3\2\2\2\6\60\3")
        buf.write("\2\2\2\b\62\3\2\2\2\nF\3\2\2\2\fK\3\2\2\2\16W\3\2\2\2")
        buf.write("\20\\\3\2\2\2\22i\3\2\2\2\24n\3\2\2\2\26q\3\2\2\2\30t")
        buf.write("\3\2\2\2\32\u0080\3\2\2\2\34\u00a3\3\2\2\2\36\37\b\2\1")
        buf.write("\2\37 \5\4\3\2 \3\3\2\2\2!#\b\3\1\2\"$\5\6\4\2#\"\3\2")
        buf.write("\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\b\3\1")
        buf.write("\2(\5\3\2\2\2)\61\7\37\2\2*\61\5\b\5\2+\61\5\n\6\2,\61")
        buf.write("\5\f\7\2-\61\5\20\t\2.\61\5\24\13\2/\61\5\26\f\2\60)\3")
        buf.write("\2\2\2\60*\3\2\2\2\60+\3\2\2\2\60,\3\2\2\2\60-\3\2\2\2")
        buf.write("\60.\3\2\2\2\60/\3\2\2\2\61\7\3\2\2\2\62\63\7\4\2\2\63")
        buf.write("A\7\25\2\2\64\65\b\5\1\2\65\66\5\30\r\2\66>\b\5\1\2\67")
        buf.write("8\7\32\2\289\b\5\1\29:\5\30\r\2:;\b\5\1\2;=\3\2\2\2<\67")
        buf.write("\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?B\3\2\2\2@>\3\2")
        buf.write("\2\2A\64\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7\26\2\2DE\b\5")
        buf.write("\1\2E\t\3\2\2\2FG\7\33\2\2GH\7\31\2\2HI\5\30\r\2IJ\b\6")
        buf.write("\1\2J\13\3\2\2\2KL\7\3\2\2LM\5\16\b\2MN\b\7\1\2NP\7\27")
        buf.write("\2\2OQ\5\6\4\2PO\3\2\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2")
        buf.write("ST\3\2\2\2TU\b\7\1\2UV\7\30\2\2V\r\3\2\2\2WX\5\30\r\2")
        buf.write("XY\t\2\2\2YZ\5\30\r\2Z[\b\b\1\2[\17\3\2\2\2\\]\7\7\2\2")
        buf.write("]^\b\t\1\2^_\5\22\n\2_`\b\t\1\2`b\7\27\2\2ac\5\6\4\2b")
        buf.write("a\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\b")
        buf.write("\t\1\2gh\7\30\2\2h\21\3\2\2\2ij\5\30\r\2jk\t\2\2\2kl\5")
        buf.write("\30\r\2lm\b\n\1\2m\23\3\2\2\2no\7\b\2\2op\b\13\1\2p\25")
        buf.write("\3\2\2\2qr\7\t\2\2rs\b\f\1\2s\27\3\2\2\2t{\5\32\16\2u")
        buf.write("v\t\3\2\2vw\5\32\16\2wx\b\r\1\2xz\3\2\2\2yu\3\2\2\2z}")
        buf.write("\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177")
        buf.write("\b\r\1\2\177\31\3\2\2\2\u0080\u008b\5\34\17\2\u0081\u0085")
        buf.write("\7\f\2\2\u0082\u0085\7\r\2\2\u0083\u0085\7\16\2\2\u0084")
        buf.write("\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2")
        buf.write("\u0085\u0086\3\2\2\2\u0086\u0087\5\34\17\2\u0087\u0088")
        buf.write("\b\16\1\2\u0088\u008a\3\2\2\2\u0089\u0084\3\2\2\2\u008a")
        buf.write("\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\b")
        buf.write("\16\1\2\u008f\33\3\2\2\2\u0090\u0091\7\34\2\2\u0091\u00a4")
        buf.write("\b\17\1\2\u0092\u0093\7\35\2\2\u0093\u00a4\b\17\1\2\u0094")
        buf.write("\u0095\7\25\2\2\u0095\u0096\5\30\r\2\u0096\u0097\7\26")
        buf.write("\2\2\u0097\u0098\b\17\1\2\u0098\u00a4\3\2\2\2\u0099\u009a")
        buf.write("\7\33\2\2\u009a\u00a4\b\17\1\2\u009b\u009c\7\5\2\2\u009c")
        buf.write("\u009d\7\25\2\2\u009d\u009e\7\26\2\2\u009e\u00a4\b\17")
        buf.write("\1\2\u009f\u00a0\7\6\2\2\u00a0\u00a1\7\25\2\2\u00a1\u00a2")
        buf.write("\7\26\2\2\u00a2\u00a4\b\17\1\2\u00a3\u0090\3\2\2\2\u00a3")
        buf.write("\u0092\3\2\2\2\u00a3\u0094\3\2\2\2\u00a3\u0099\3\2\2\2")
        buf.write("\u00a3\u009b\3\2\2\2\u00a3\u009f\3\2\2\2\u00a4\35\3\2")
        buf.write("\2\2\f%\60>ARd{\u0084\u008b\u00a3")
        return buf.getvalue()


class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'print'", "'readint'", "'readstr'", 
                     "'while'", "'break'", "'continue'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'>'", "'>='", "'<'", 
                     "'<='", "'('", "')'", "'{'", "'}'", "'='", "','" ]

    symbolicNames = [ "<INVALID>", "IF", "PRINT", "READINT", "READSTR", 
                      "WHILE", "BREAK", "CONTINUE", "PLUS", "MINUS", "TIMES", 
                      "OVER", "REM", "EQ", "NE", "GT", "GE", "LT", "LE", 
                      "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", 
                      "COMMA", "NAME", "NUMBER", "STRING", "COMMENT", "NL", 
                      "SPACE", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_st_if = 5
    RULE_comparison_if = 6
    RULE_st_while = 7
    RULE_comparison_while = 8
    RULE_st_break = 9
    RULE_st_continue = 10
    RULE_expression = 11
    RULE_term = 12
    RULE_factor = 13

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "st_if", "comparison_if", "st_while", "comparison_while", 
                   "st_break", "st_continue", "expression", "term", "factor" ]

    EOF = Token.EOF
    IF=1
    PRINT=2
    READINT=3
    READSTR=4
    WHILE=5
    BREAK=6
    CONTINUE=7
    PLUS=8
    MINUS=9
    TIMES=10
    OVER=11
    REM=12
    EQ=13
    NE=14
    GT=15
    GE=16
    LT=17
    LE=18
    OP_PAR=19
    CL_PAR=20
    OP_CUR=21
    CL_CUR=22
    ATTRIB=23
    COMMA=24
    NAME=25
    NUMBER=26
    STRING=27
    COMMENT=28
    NL=29
    SPACE=30
    INDENT=31
    DEDENT=32

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
                
            self.state = 29
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
                
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statement()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
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


        def st_if(self):
            return self.getTypedRuleContext(JacParser.St_ifContext,0)


        def st_while(self):
            return self.getTypedRuleContext(JacParser.St_whileContext,0)


        def st_break(self):
            return self.getTypedRuleContext(JacParser.St_breakContext,0)


        def st_continue(self):
            return self.getTypedRuleContext(JacParser.St_continueContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.NL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(JacParser.NL)
                pass
            elif token in [JacParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.st_print()
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.st_attrib()
                pass
            elif token in [JacParser.IF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.st_if()
                pass
            elif token in [JacParser.WHILE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.st_while()
                pass
            elif token in [JacParser.BREAK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.st_break()
                pass
            elif token in [JacParser.CONTINUE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.st_continue()
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
            self.state = 48
            self.match(JacParser.PRINT)
            self.state = 49
            self.match(JacParser.OP_PAR)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                if 1:
                        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 51
                localctx.e1 = self.expression()
                if 1:
                        if localctx.e1.type == 'i':
                            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                        elif localctx.e1.type == 's':
                            emit ('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                        else:
                            print('*****HELP*****')
                    
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JacParser.COMMA:
                    self.state = 53
                    self.match(JacParser.COMMA)
                    if 1:
                            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                            
                    self.state = 55
                    self.expression()
                    if 1:
                            emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                            
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 65
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
            self.state = 68
            self.match(JacParser.NAME)
            self.state = 69
            self.match(JacParser.ATTRIB)
            self.state = 70
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
            self.state = 73
            self.match(JacParser.IF)
            self.state = 74
            self.comparison_if()
            if 1:
                    global x 
                    local_x = x
                    x += 1
                
            self.state = 76
            self.match(JacParser.OP_CUR)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.statement()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    print('NOT_IF_' + str(local_x) + ':')
                
            self.state = 83
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
            self.state = 85
            self.expression()
            self.state = 86
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 87
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
            self.state = 90
            self.match(JacParser.WHILE)
            if 1:
                    global y 
                    local_y = y
                    print('BEGIN_WHILE_' + str(local_y) + ':')
                
            self.state = 92
            self.comparison_while()
            if 1:
                    y += 1
                
            self.state = 94
            self.match(JacParser.OP_CUR)
            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 95
                self.statement()
                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    emit('goto BEGIN_WHILE_' + str(local_y), 0)
                    print('END_WHILE_' + str(local_y) + ':')
                
            self.state = 101
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
            self.state = 103
            self.expression()
            self.state = 104
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 105
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


    class St_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(JacParser.BREAK, 0)

        def getRuleIndex(self):
            return JacParser.RULE_st_break




    def st_break(self):

        localctx = JacParser.St_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_st_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(JacParser.BREAK)
            if 1:
                    print('goto END_WHILE_' + str(y-1))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(JacParser.CONTINUE, 0)

        def getRuleIndex(self):
            return JacParser.RULE_st_continue




    def st_continue(self):

        localctx = JacParser.St_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_st_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(JacParser.CONTINUE)
            if 1:
                    print('goto BEGIN_WHILE_' + str(y-1))
                
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
        self.enterRule(localctx, 22, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            localctx.t1 = self.term()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.PLUS or _la==JacParser.MINUS:
                self.state = 115
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==JacParser.PLUS or _la==JacParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                localctx.t2 = self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            print('    iadd')
                        else:
                            print('    isub')    
                    
                self.state = 123
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
        self.enterRule(localctx, 24, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            localctx._factor = self.factor()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0):
                self.state = 130
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JacParser.TIMES]:
                    self.state = 127
                    localctx.op = self.match(JacParser.TIMES)
                    pass
                elif token in [JacParser.OVER]:
                    self.state = 128
                    self.match(JacParser.OVER)
                    pass
                elif token in [JacParser.REM]:
                    self.state = 129
                    self.match(JacParser.REM)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 132
                localctx._factor = self.factor()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                            print('    imul')
                        elif (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                            print('    idiv')
                        else:
                            print('    irem')
                    
                self.state = 139
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
        self.enterRule(localctx, 26, self.RULE_factor)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                        localctx.type = 'i'

                    
                pass
            elif token in [JacParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                localctx._STRING = self.match(JacParser.STRING)
                if 1:
                        emit('ldc ' + (None if localctx._STRING is None else localctx._STRING.text), +1)
                        localctx.type = 's'
                    
                pass
            elif token in [JacParser.OP_PAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.match(JacParser.OP_PAR)
                self.state = 147
                localctx.e = self.expression()
                self.state = 148
                self.match(JacParser.CL_PAR)
                if 1:
                        localctx.type = e.type
                    
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.match(JacParser.NAME)
                if 1:
                        print('    iload 0')
                        localctx.type = 'i'
                    
                pass
            elif token in [JacParser.READINT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 153
                self.match(JacParser.READINT)
                self.state = 154
                self.match(JacParser.OP_PAR)
                self.state = 155
                self.match(JacParser.CL_PAR)
                if 1:
                        #geração de código de leitura de inteiro
                        emit('    invokestatic Runtime/readInt()I', +1)
                        localctx.type = 'i'
                    
                pass
            elif token in [JacParser.READSTR]:
                self.enterOuterAlt(localctx, 6)
                self.state = 157
                self.match(JacParser.READSTR)
                self.state = 158
                self.match(JacParser.OP_PAR)
                self.state = 159
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





