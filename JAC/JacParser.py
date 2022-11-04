# Generated from Jac.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


# symbol_table = []

def serializedATN():
    return [
        4,1,13,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,4,1,22,8,1,11,1,12,1,23,1,1,1,1,1,
        2,1,2,3,2,30,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,3,5,47,8,5,1,5,1,5,1,5,5,5,52,8,5,10,5,12,5,55,9,5,1,
        6,1,6,1,6,1,6,3,6,61,8,6,1,6,1,6,1,6,5,6,66,8,6,10,6,12,6,69,9,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,79,8,7,1,7,0,0,8,0,2,4,6,8,10,
        12,14,0,0,81,0,16,1,0,0,0,2,19,1,0,0,0,4,29,1,0,0,0,6,31,1,0,0,0,
        8,38,1,0,0,0,10,43,1,0,0,0,12,56,1,0,0,0,14,78,1,0,0,0,16,17,6,0,
        -1,0,17,18,3,2,1,0,18,1,1,0,0,0,19,21,6,1,-1,0,20,22,3,4,2,0,21,
        20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,
        0,25,26,6,1,-1,0,26,3,1,0,0,0,27,30,3,6,3,0,28,30,3,8,4,0,29,27,
        1,0,0,0,29,28,1,0,0,0,30,5,1,0,0,0,31,32,5,1,0,0,32,33,5,7,0,0,33,
        34,6,3,-1,0,34,35,3,10,5,0,35,36,5,8,0,0,36,37,6,3,-1,0,37,7,1,0,
        0,0,38,39,5,10,0,0,39,40,5,9,0,0,40,41,3,10,5,0,41,42,6,4,-1,0,42,
        9,1,0,0,0,43,53,3,12,6,0,44,47,5,2,0,0,45,47,5,3,0,0,46,44,1,0,0,
        0,46,45,1,0,0,0,47,48,1,0,0,0,48,49,3,12,6,0,49,50,6,5,-1,0,50,52,
        1,0,0,0,51,46,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,
        54,11,1,0,0,0,55,53,1,0,0,0,56,67,3,14,7,0,57,61,5,4,0,0,58,61,5,
        5,0,0,59,61,5,6,0,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,
        62,1,0,0,0,62,63,3,14,7,0,63,64,6,6,-1,0,64,66,1,0,0,0,65,60,1,0,
        0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,13,1,0,0,0,69,67,
        1,0,0,0,70,71,5,11,0,0,71,79,6,7,-1,0,72,73,5,7,0,0,73,74,3,10,5,
        0,74,75,5,8,0,0,75,79,1,0,0,0,76,77,5,10,0,0,77,79,6,7,-1,0,78,70,
        1,0,0,0,78,72,1,0,0,0,78,76,1,0,0,0,79,15,1,0,0,0,7,23,29,46,53,
        60,67,78
    ]

class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>", "PRINT", "PLUS", "MINUS", "TIMES", "OVER", 
                      "REM", "OP_PAR", "CL_PAR", "ATTRIB", "NAME", "NUMBER", 
                      "SPACE", "COOMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_expression = 5
    RULE_term = 6
    RULE_factor = 7

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "expression", "term", "factor" ]

    EOF = Token.EOF
    PRINT=1
    PLUS=2
    MINUS=3
    TIMES=4
    OVER=5
    REM=6
    OP_PAR=7
    CL_PAR=8
    ATTRIB=9
    NAME=10
    NUMBER=11
    SPACE=12
    COOMENT=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
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
                
            self.state = 17
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
                
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==10):
                    break

            if 1:
                    print('    return')
                    print('.limit stack 10')
                    print('.end method')
                    # print('\n; symbol_table:', symbol_table)
                
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
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.st_print()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
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

        def PRINT(self):
            return self.getToken(JacParser.PRINT, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def getRuleIndex(self):
            return JacParser.RULE_st_print




    def st_print(self):

        localctx = JacParser.St_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_st_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(JacParser.PRINT)
            self.state = 32
            self.match(JacParser.OP_PAR)
            if 1:
                    print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
                
            self.state = 34
            self.expression()
            self.state = 35
            self.match(JacParser.CL_PAR)
            if 1:
                    print('    invokevirtual java/io/PrintStream/println(I)V\n')
                
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
            self.state = 38
            self.match(JacParser.NAME)
            self.state = 39
            self.match(JacParser.ATTRIB)
            self.state = 40
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.TermContext)
            else:
                return self.getTypedRuleContext(JacParser.TermContext,i)


        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.MINUS)
            else:
                return self.getToken(JacParser.MINUS, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.PLUS)
            else:
                return self.getToken(JacParser.PLUS, i)

        def getRuleIndex(self):
            return JacParser.RULE_expression




    def expression(self):

        localctx = JacParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.term()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 46
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 44
                    localctx.op = self.match(JacParser.PLUS)
                    pass
                elif token in [3]:
                    self.state = 45
                    self.match(JacParser.MINUS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 48
                self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            print('    iadd')
                        else:
                            print('    isub')    
                    
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.factor()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0:
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 57
                    localctx.op = self.match(JacParser.TIMES)
                    pass
                elif token in [5]:
                    self.state = 58
                    self.match(JacParser.OVER)
                    pass
                elif token in [6]:
                    self.state = 59
                    self.match(JacParser.REM)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 62
                self.factor()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                            print('    imul')
                        elif (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                            print('    idiv')
                        else:
                            print('    irem')
                    
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self._NUMBER = None # Token

        def NUMBER(self):
            return self.getToken(JacParser.NUMBER, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        print('    ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text))
                        # symbol_table.append((None if localctx._NUMBER is None else localctx._NUMBER.text))
                    
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(JacParser.OP_PAR)
                self.state = 73
                self.expression()
                self.state = 74
                self.match(JacParser.CL_PAR)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.match(JacParser.NAME)
                if 1:
                        print('    iload 0')
                    
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





