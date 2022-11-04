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
        4,1,11,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,4,1,20,8,1,11,1,12,1,21,1,1,1,1,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,38,8,4,1,4,1,4,1,4,5,4,
        43,8,4,10,4,12,4,46,9,4,1,5,1,5,1,5,1,5,3,5,52,8,5,1,5,1,5,1,5,5,
        5,57,8,5,10,5,12,5,60,9,5,1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,
        0,0,63,0,14,1,0,0,0,2,17,1,0,0,0,4,25,1,0,0,0,6,27,1,0,0,0,8,34,
        1,0,0,0,10,47,1,0,0,0,12,61,1,0,0,0,14,15,6,0,-1,0,15,16,3,2,1,0,
        16,1,1,0,0,0,17,19,6,1,-1,0,18,20,3,4,2,0,19,18,1,0,0,0,20,21,1,
        0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,6,1,-1,0,24,
        3,1,0,0,0,25,26,3,6,3,0,26,5,1,0,0,0,27,28,5,1,0,0,28,29,5,7,0,0,
        29,30,6,3,-1,0,30,31,3,8,4,0,31,32,5,8,0,0,32,33,6,3,-1,0,33,7,1,
        0,0,0,34,44,3,10,5,0,35,38,5,2,0,0,36,38,5,3,0,0,37,35,1,0,0,0,37,
        36,1,0,0,0,38,39,1,0,0,0,39,40,3,10,5,0,40,41,6,4,-1,0,41,43,1,0,
        0,0,42,37,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,9,
        1,0,0,0,46,44,1,0,0,0,47,58,3,12,6,0,48,52,5,4,0,0,49,52,5,5,0,0,
        50,52,5,6,0,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,53,1,
        0,0,0,53,54,3,12,6,0,54,55,6,5,-1,0,55,57,1,0,0,0,56,51,1,0,0,0,
        57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,11,1,0,0,0,60,58,1,
        0,0,0,61,62,5,9,0,0,62,63,6,6,-1,0,63,13,1,0,0,0,5,21,37,44,51,58
    ]

class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "PLUS", "MINUS", "TIMES", "OVER", 
                      "REM", "OP_PAR", "CL_PAR", "NUMBER", "SPACE", "COOMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_expression = 4
    RULE_term = 5
    RULE_factor = 6

    ruleNames =  [ "program", "main", "statement", "st_print", "expression", 
                   "term", "factor" ]

    EOF = Token.EOF
    PRINT=1
    PLUS=2
    MINUS=3
    TIMES=4
    OVER=5
    REM=6
    OP_PAR=7
    CL_PAR=8
    NUMBER=9
    SPACE=10
    COOMENT=11

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
                
            self.state = 15
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
                
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
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


        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.st_print()
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
            self.state = 27
            self.match(JacParser.PRINT)
            self.state = 28
            self.match(JacParser.OP_PAR)
            if 1:
                    print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
                
            self.state = 30
            self.expression()
            self.state = 31
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
        self.enterRule(localctx, 8, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.term()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 37
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 35
                    localctx.op = self.match(JacParser.PLUS)
                    pass
                elif token in [3]:
                    self.state = 36
                    self.match(JacParser.MINUS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 39
                self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            print('    iadd')
                        else:
                            print('    isub')    
                    
                self.state = 46
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
        self.enterRule(localctx, 10, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.factor()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0:
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 48
                    localctx.op = self.match(JacParser.TIMES)
                    pass
                elif token in [5]:
                    self.state = 49
                    self.match(JacParser.OVER)
                    pass
                elif token in [6]:
                    self.state = 50
                    self.match(JacParser.REM)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 53
                self.factor()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                            print('    imul')
                        elif (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                            print('    idiv')
                        else:
                            print('    irem')
                    
                self.state = 60
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

        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            localctx._NUMBER = self.match(JacParser.NUMBER)
            if 1:
                    print('    ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text))
                    # symbol_table.append((None if localctx._NUMBER is None else localctx._NUMBER.text))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





