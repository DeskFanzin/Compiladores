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
symbolTable = []
typeOfTable = []
usedVariables = []
funcTable = []
funcParameters = []
returnFunc = []
x = 0
y = 0
Loop = False
curStack = 0
maxOfStacks = 0
def emit(bytecode, delta):
    global curStack, maxOfStacks
    print('    '+ bytecode + '    ; delta=' + str(delta))
    curStack += delta
    if curStack > maxOfStacks:
        maxOfStacks = curStack

def resetFunctionMetrics():
    global symbolTable
    global typeOfTable
    global usedVariables
    global maxOfStacks
    global curStack

    symbolTable = []
    typeOfTable = []
    usedTables = []
    maxOfStacks = 0
    curStack = 0



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%")
        buf.write("\u00ef\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\7\2+\n\2\f\2\16\2.\13\2\3\2\3\2\3\3")
        buf.write("\3\3\6\3\64\n\3\r\3\16\3\65\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4C\n\4\3\5\3\5\3\5\3\5\5\5I\n\5\3")
        buf.write("\5\3\5\3\5\5\5N\n\5\3\5\3\5\3\5\7\5S\n\5\f\5\16\5V\13")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\7\6^\n\6\f\6\16\6a\13\6\3\7")
        buf.write("\3\7\3\7\5\7f\n\7\3\7\3\7\3\7\3\b\3\b\3\b\7\bn\n\b\f\b")
        buf.write("\16\bq\13\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u0081\n\n\f\n\16\n\u0084\13\n\5\n\u0086")
        buf.write("\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\6\f\u0096\n\f\r\f\16\f\u0097\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\6\16\u00a9\n\16\r\16\16\16\u00aa\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\7\22\u00c0\n\22\f\22\16\22\u00c3")
        buf.write("\13\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\7\23\u00cc\n")
        buf.write("\23\f\23\16\23\u00cf\13\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00e9\n")
        buf.write("\24\3\24\3\24\5\24\u00ed\n\24\3\24\2\2\25\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&\2\5\3\2\21\26\3\2\f\r")
        buf.write("\3\2\16\20\2\u00f8\2(\3\2\2\2\4\61\3\2\2\2\6B\3\2\2\2")
        buf.write("\bD\3\2\2\2\nZ\3\2\2\2\fb\3\2\2\2\16j\3\2\2\2\20r\3\2")
        buf.write("\2\2\22v\3\2\2\2\24\u008a\3\2\2\2\26\u008f\3\2\2\2\30")
        buf.write("\u009c\3\2\2\2\32\u00a1\3\2\2\2\34\u00af\3\2\2\2\36\u00b4")
        buf.write("\3\2\2\2 \u00b7\3\2\2\2\"\u00ba\3\2\2\2$\u00c6\3\2\2\2")
        buf.write("&\u00ec\3\2\2\2(,\b\2\1\2)+\5\b\5\2*)\3\2\2\2+.\3\2\2")
        buf.write("\2,*\3\2\2\2,-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\5\4\3\2")
        buf.write("\60\3\3\2\2\2\61\63\b\3\1\2\62\64\5\6\4\2\63\62\3\2\2")
        buf.write("\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2")
        buf.write("\2\2\678\b\3\1\28\5\3\2\2\29C\7\"\2\2:C\5\22\n\2;C\5\24")
        buf.write("\13\2<C\5\26\f\2=C\5\32\16\2>C\5\36\20\2?C\5 \21\2@C\5")
        buf.write("\f\7\2AC\5\20\t\2B9\3\2\2\2B:\3\2\2\2B;\3\2\2\2B<\3\2")
        buf.write("\2\2B=\3\2\2\2B>\3\2\2\2B?\3\2\2\2B@\3\2\2\2BA\3\2\2\2")
        buf.write("C\7\3\2\2\2DE\7\n\2\2EF\7\36\2\2FH\7\27\2\2GI\5\n\6\2")
        buf.write("HG\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\7\30\2\2KM\7\33\2\2L")
        buf.write("N\7\36\2\2ML\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\b\5\1\2PT\7")
        buf.write("$\2\2QS\5\6\4\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2")
        buf.write("\2UW\3\2\2\2VT\3\2\2\2WX\7%\2\2XY\b\5\1\2Y\t\3\2\2\2Z")
        buf.write("_\7\36\2\2[\\\7\35\2\2\\^\7\36\2\2][\3\2\2\2^a\3\2\2\2")
        buf.write("_]\3\2\2\2_`\3\2\2\2`\13\3\2\2\2a_\3\2\2\2bc\7\36\2\2")
        buf.write("ce\7\27\2\2df\5\16\b\2ed\3\2\2\2ef\3\2\2\2fg\3\2\2\2g")
        buf.write("h\7\30\2\2hi\b\7\1\2i\r\3\2\2\2jo\5\"\22\2kl\7\35\2\2")
        buf.write("ln\5\"\22\2mk\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2p\17")
        buf.write("\3\2\2\2qo\3\2\2\2rs\7\13\2\2st\5\"\22\2tu\b\t\1\2u\21")
        buf.write("\3\2\2\2vw\7\4\2\2w\u0085\7\27\2\2xy\b\n\1\2yz\5\"\22")
        buf.write("\2z\u0082\b\n\1\2{|\7\35\2\2|}\b\n\1\2}~\5\"\22\2~\177")
        buf.write("\b\n\1\2\177\u0081\3\2\2\2\u0080{\3\2\2\2\u0081\u0084")
        buf.write("\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0085x\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\7\30\2")
        buf.write("\2\u0088\u0089\b\n\1\2\u0089\23\3\2\2\2\u008a\u008b\7")
        buf.write("\36\2\2\u008b\u008c\7\34\2\2\u008c\u008d\5\"\22\2\u008d")
        buf.write("\u008e\b\13\1\2\u008e\25\3\2\2\2\u008f\u0090\7\3\2\2\u0090")
        buf.write("\u0091\5\30\r\2\u0091\u0092\b\f\1\2\u0092\u0093\7\33\2")
        buf.write("\2\u0093\u0095\7$\2\2\u0094\u0096\5\6\4\2\u0095\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\b\f\1\2")
        buf.write("\u009a\u009b\7%\2\2\u009b\27\3\2\2\2\u009c\u009d\5\"\22")
        buf.write("\2\u009d\u009e\t\2\2\2\u009e\u009f\5\"\22\2\u009f\u00a0")
        buf.write("\b\r\1\2\u00a0\31\3\2\2\2\u00a1\u00a2\7\7\2\2\u00a2\u00a3")
        buf.write("\b\16\1\2\u00a3\u00a4\5\34\17\2\u00a4\u00a5\b\16\1\2\u00a5")
        buf.write("\u00a6\7\33\2\2\u00a6\u00a8\7$\2\2\u00a7\u00a9\5\6\4\2")
        buf.write("\u00a8\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00a8\3")
        buf.write("\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad")
        buf.write("\b\16\1\2\u00ad\u00ae\7%\2\2\u00ae\33\3\2\2\2\u00af\u00b0")
        buf.write("\5\"\22\2\u00b0\u00b1\t\2\2\2\u00b1\u00b2\5\"\22\2\u00b2")
        buf.write("\u00b3\b\17\1\2\u00b3\35\3\2\2\2\u00b4\u00b5\7\b\2\2\u00b5")
        buf.write("\u00b6\b\20\1\2\u00b6\37\3\2\2\2\u00b7\u00b8\7\t\2\2\u00b8")
        buf.write("\u00b9\b\21\1\2\u00b9!\3\2\2\2\u00ba\u00c1\5$\23\2\u00bb")
        buf.write("\u00bc\t\3\2\2\u00bc\u00bd\5$\23\2\u00bd\u00be\b\22\1")
        buf.write("\2\u00be\u00c0\3\2\2\2\u00bf\u00bb\3\2\2\2\u00c0\u00c3")
        buf.write("\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\b\22\1")
        buf.write("\2\u00c5#\3\2\2\2\u00c6\u00cd\5&\24\2\u00c7\u00c8\t\4")
        buf.write("\2\2\u00c8\u00c9\5&\24\2\u00c9\u00ca\b\23\1\2\u00ca\u00cc")
        buf.write("\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00d0\u00d1\b\23\1\2\u00d1%\3\2\2")
        buf.write("\2\u00d2\u00d3\7\37\2\2\u00d3\u00ed\b\24\1\2\u00d4\u00d5")
        buf.write("\7 \2\2\u00d5\u00ed\b\24\1\2\u00d6\u00d7\7\27\2\2\u00d7")
        buf.write("\u00d8\5\"\22\2\u00d8\u00d9\7\30\2\2\u00d9\u00da\b\24")
        buf.write("\1\2\u00da\u00ed\3\2\2\2\u00db\u00dc\7\36\2\2\u00dc\u00ed")
        buf.write("\b\24\1\2\u00dd\u00de\7\5\2\2\u00de\u00df\7\27\2\2\u00df")
        buf.write("\u00e0\7\30\2\2\u00e0\u00ed\b\24\1\2\u00e1\u00e2\7\6\2")
        buf.write("\2\u00e2\u00e3\7\27\2\2\u00e3\u00e4\7\30\2\2\u00e4\u00ed")
        buf.write("\b\24\1\2\u00e5\u00e6\7\36\2\2\u00e6\u00e8\7\27\2\2\u00e7")
        buf.write("\u00e9\5\16\b\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2")
        buf.write("\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\7\30\2\2\u00eb\u00ed")
        buf.write("\b\24\1\2\u00ec\u00d2\3\2\2\2\u00ec\u00d4\3\2\2\2\u00ec")
        buf.write("\u00d6\3\2\2\2\u00ec\u00db\3\2\2\2\u00ec\u00dd\3\2\2\2")
        buf.write("\u00ec\u00e1\3\2\2\2\u00ec\u00e5\3\2\2\2\u00ed\'\3\2\2")
        buf.write("\2\23,\65BHMT_eo\u0082\u0085\u0097\u00aa\u00c1\u00cd\u00e8")
        buf.write("\u00ec")
        return buf.getvalue()


class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'print'", "'readint'", "'readstr'", 
                     "'while'", "'break'", "'continue'", "'def'", "'return'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>'", "'>='", "'<'", "'<='", "'('", "')'", "'{'", 
                     "'}'", "':'", "'='", "','" ]

    symbolicNames = [ "<INVALID>", "IF", "PRINT", "READINT", "READSTR", 
                      "WHILE", "BREAK", "CONTINUE", "DEF", "RETURN", "PLUS", 
                      "MINUS", "TIMES", "OVER", "REM", "EQ", "NE", "GT", 
                      "GE", "LT", "LE", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", 
                      "COLON", "ATTRIB", "COMMA", "NAME", "NUMBER", "STRING", 
                      "COMMENT", "NL", "SPACE", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_function = 3
    RULE_parameters = 4
    RULE_st_call = 5
    RULE_arguments = 6
    RULE_st_return = 7
    RULE_st_print = 8
    RULE_st_attrib = 9
    RULE_st_if = 10
    RULE_comparison_if = 11
    RULE_st_while = 12
    RULE_comparison_while = 13
    RULE_st_break = 14
    RULE_st_continue = 15
    RULE_expression = 16
    RULE_term = 17
    RULE_factor = 18

    ruleNames =  [ "program", "main", "statement", "function", "parameters", 
                   "st_call", "arguments", "st_return", "st_print", "st_attrib", 
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
    DEF=8
    RETURN=9
    PLUS=10
    MINUS=11
    TIMES=12
    OVER=13
    REM=14
    EQ=15
    NE=16
    GT=17
    GE=18
    LT=19
    LE=20
    OP_PAR=21
    CL_PAR=22
    OP_CUR=23
    CL_CUR=24
    COLON=25
    ATTRIB=26
    COMMA=27
    NAME=28
    NUMBER=29
    STRING=30
    COMMENT=31
    NL=32
    SPACE=33
    INDENT=34
    DEDENT=35

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


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.FunctionContext)
            else:
                return self.getTypedRuleContext(JacParser.FunctionContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_program




    def program(self):

        localctx = JacParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    print('.source Test')
                    print('.class  public Test')
                    print('.super  java/lang/Object\n')
                    print('.method public <init>()V')
                    print('    aload_0')
                    print('    invokenonvirtual java/lang/Object/<init>()V')
                    print('    return')
                    print('.end method\n')
                
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.DEF:
                self.state = 39
                self.function()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
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
                    print('.method public static main([Ljava/lang/String;)V')
                
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.statement()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.RETURN) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    for i in range(len(usedVariables)):
                        if usedVariables[i] == False:
                            try:
                                sys.stderr.write('WARNING: Variable ' + symbolTable[i] + ' was declared but not used\n')
                            except IndexError:
                                pass
                    print('    return')
                    if len(symbolTable) != 0:
                        print('.limit locals ' + str(len(symbolTable)))
                    else:
                        print('.limit locals 1')
                    print('.limit stack ' + str(maxOfStacks))
                    print('.end method')
                    print('\n; symbol_tabe:', symbolTable)
                    print('; typeOfTable:', typeOfTable)
                    print('; usedVariables:', usedVariables)

                
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


        def st_call(self):
            return self.getTypedRuleContext(JacParser.St_callContext,0)


        def st_return(self):
            return self.getTypedRuleContext(JacParser.St_returnContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(JacParser.NL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.st_print()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.st_attrib()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.st_if()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.st_while()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.st_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 61
                self.st_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 62
                self.st_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 63
                self.st_return()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token
            self.p = None # ParametersContext
            self.ft = None # Token
            self.st = None # StatementContext

        def DEF(self):
            return self.getToken(JacParser.DEF, 0)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.NAME)
            else:
                return self.getToken(JacParser.NAME, i)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def COLON(self):
            return self.getToken(JacParser.COLON, 0)

        def INDENT(self):
            return self.getToken(JacParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(JacParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def parameters(self):
            return self.getTypedRuleContext(JacParser.ParametersContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_function




    def function(self):

        localctx = JacParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(JacParser.DEF)
            self.state = 67
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 68
            self.match(JacParser.OP_PAR)

            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JacParser.NAME:
                self.state = 69
                localctx.p = self.parameters()


            self.state = 72
            self.match(JacParser.CL_PAR)
            self.state = 73
            self.match(JacParser.COLON)

            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JacParser.NAME:
                self.state = 74
                localctx.ft = self.match(JacParser.NAME)


            if 1:
                if (None if localctx._NAME is None else localctx._NAME.text) not in funcTable:
                    parameters = (None if localctx.p is None else self._input.getText(localctx.p.start,localctx.p.stop)).split(',') if (None if localctx.p is None else self._input.getText(localctx.p.start,localctx.p.stop)) else []
                    if len(parameters) == len(set(parameters)):
                        funcTable.append((None if localctx._NAME is None else localctx._NAME.text))
                        funcParameters.append(len(parameters))
                        returnFunc.append(True if (None if localctx.ft is None else localctx.ft.text) == 'int' else False)
                        print('.method public static '+(None if localctx._NAME is None else localctx._NAME.text)+'('+('I' * len(parameters))+')'+('I' if (None if localctx.ft is None else localctx.ft.text) else 'V'))

                        for p in parameters:
                            if p not in symbolTable:
                                symbolTable.append(p)
                                typeOfTable.append('i')
                                usedVariables.append(False)
                    else:
                        sys.stderr.write('ERROR: Parameter(s) must be unique: ' + str(parameters))
                        sys.exit(1)
                else:
                    sys.stderr.write('ERROR: Function already defined: ' + (None if localctx._NAME is None else localctx._NAME.text) )
                    sys.exit(1)
              

            self.state = 78
            self.match(JacParser.INDENT)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.RETURN) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0):
                self.state = 79
                localctx.st = self.statement()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(JacParser.DEDENT)
            if 1:

                print('    return')
                print('.limit stack ' + str(maxOfStacks))
                print('.limit locals ' + str(len(symbolTable)))
                print(';symbolTable ' + str(symbolTable))
                print('.end method')
                resetFunctionMetrics()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.NAME)
            else:
                return self.getToken(JacParser.NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.COMMA)
            else:
                return self.getToken(JacParser.COMMA, i)

        def getRuleIndex(self):
            return JacParser.RULE_parameters




    def parameters(self):

        localctx = JacParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(JacParser.NAME)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.COMMA:
                self.state = 89
                self.match(JacParser.COMMA)
                self.state = 90
                self.match(JacParser.NAME)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token
            self.arg = None # ArgumentsContext

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def arguments(self):
            return self.getTypedRuleContext(JacParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_st_call




    def st_call(self):

        localctx = JacParser.St_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 97
            self.match(JacParser.OP_PAR)

            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                self.state = 98
                localctx.arg = self.arguments()


            self.state = 101
            self.match(JacParser.CL_PAR)
            if 1:

                if (None if localctx._NAME is None else localctx._NAME.text) in funcTable:
                    index = funcTable.index((None if localctx._NAME is None else localctx._NAME.text))
                    arguments = (None if localctx.arg is None else self._input.getText(localctx.arg.start,localctx.arg.stop)) if (None if localctx.arg is None else self._input.getText(localctx.arg.start,localctx.arg.stop)) else ""
                    if not returnFunc[index]:
                        if '"' not in arguments:
                            real_arguments = arguments.split(',') if len(arguments) > 0 else []
                            if len(real_arguments) == funcParameters[index]:
                                func_I = "I" * funcParameters[index]
                                emit('invokestatic Test/' + (None if localctx._NAME is None else localctx._NAME.text) + '(' + func_I + ')V', 0)
                            else:
                                sys.stderr.write('ERROR: Wrong number of arguments: '+ (None if localctx._NAME is None else localctx._NAME.text) + '\n')
                        else:
                            sys.stderr.write('ERROR: all arguments must be integer: ' + (None if localctx._NAME is None else localctx._NAME.text) + '\n')
                    else:
                       sys.stderr.write('ERROR: Function missing return statement: ' + (None if localctx._NAME is None else localctx._NAME.text) + '\n')
                else:
                    sys.stderr.write('ERROR: Function not defined: ' + (None if localctx._NAME is None else localctx._NAME.text) + '\n')

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return JacParser.RULE_arguments




    def arguments(self):

        localctx = JacParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.expression()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.COMMA:
                self.state = 105
                self.match(JacParser.COMMA)
                self.state = 106
                self.expression()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ex = None # ExpressionContext

        def RETURN(self):
            return self.getToken(JacParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_st_return




    def st_return(self):

        localctx = JacParser.St_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_st_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(JacParser.RETURN)
            self.state = 113
            localctx.ex = self.expression()
            if 1:
                if localctx.ex.type == 'i':
                    emit('ireturn', 0)
                else:
                    sys.stderr.write('ERROR: Return type must be integer: '+ (None if localctx.ex is None else self._input.getText(localctx.ex.start,localctx.ex.stop)) + ' is ' + '"' + localctx.ex.type +'"' + '\n')

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
            self.e2 = None # ExpressionContext

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
        self.enterRule(localctx, 16, self.RULE_st_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(JacParser.PRINT)
            self.state = 117
            self.match(JacParser.OP_PAR)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                if 1:
                        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 119
                localctx.e1 = self.expression()
                if 1:
                        if localctx.e1.type == 'i':
                            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                        elif localctx.e1.type == 's':
                            emit ('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                        else:
                            sys.stderr.write('ERROR: Invalid type for print')
                            sys.exit(1)
                    
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JacParser.COMMA:
                    self.state = 121
                    self.match(JacParser.COMMA)
                    if 1:
                                emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                            
                    self.state = 123
                    localctx.e2 = self.expression()
                    if 1:
                                if localctx.e2.type == 'i':
                                    emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                                elif localctx.e2.type == 's':
                                    emit ('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                                else:
                                    sys.stderr.write('ERROR: Invalid type for print')
                                    sys.exit(1)
                            
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 133
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
            self._NAME = None # Token
            self.op = None # ExpressionContext
            self._expression = None # ExpressionContext

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
        self.enterRule(localctx, 18, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 137
            self.match(JacParser.ATTRIB)
            self.state = 138
            localctx.op = localctx._expression = self.expression()
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) not in symbolTable:
                        symbolTable.append((None if localctx._NAME is None else localctx._NAME.text))
                        typeOfTable.append(localctx._expression.type)
                        usedVariables.append(False)

                    index = str(symbolTable.index((None if localctx._NAME is None else localctx._NAME.text)))
                    type  = typeOfTable[int(index)]
                    if(type == localctx.op.type):
                        if(type == 'i'):
                            emit('istore ' + str(index), -1)
                        elif(type == 's'):
                            emit('astore ' + str(index), -1)
                    if(type == 'i' and localctx.op.type == 's'):
                        sys.stderr.write('ERROR: Expected type int for assignment in variable ' + (None if localctx._NAME is None else localctx._NAME.text) + ' in line ' + str((0 if localctx._NAME is None else localctx._NAME.line)) + '\n')
                    if(type == 's' and localctx.op.type == 'i'):
                        sys.stderr.write('ERROR: Expected type string for assignment in variable ' + (None if localctx._NAME is None else localctx._NAME.text) + ' in line ' + str((0 if localctx._NAME is None else localctx._NAME.line)) + '\n')
                
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


        def COLON(self):
            return self.getToken(JacParser.COLON, 0)

        def INDENT(self):
            return self.getToken(JacParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(JacParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_st_if




    def st_if(self):

        localctx = JacParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(JacParser.IF)
            self.state = 142
            self.comparison_if()
            if 1:
                    global x 
                    local_x = x
                    x += 1
                
            self.state = 144
            self.match(JacParser.COLON)
            self.state = 145
            self.match(JacParser.INDENT)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.statement()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.RETURN) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    print('NOT_IF_' + str(local_x) + ':')
                
            self.state = 152
            self.match(JacParser.DEDENT)
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
            self.ex = None # ExpressionContext
            self.op = None # Token
            self.ex1 = None # ExpressionContext

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
        self.enterRule(localctx, 22, self.RULE_comparison_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            localctx.ex = self.expression()
            self.state = 155
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 156
            localctx.ex1 = self.expression()
            if 1:
                    if localctx.ex.type == 's' or localctx.ex1.type == 's':
                        sys.stderr.write('ERROR: Operator cannot use string type: ' + str((None if localctx.op is None else localctx.op.text)) + '\n')
                        sys.exit(1)
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.EQ:
                        emit ('if_icmpne NOT_IF_' + str(x), -2)
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.NE:
                        emit ('if_icmpeq NOT_IF_' + str(x), -2)    
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.GT:
                        emit ('if_icmple NOT_IF_' + str(x), -2)      
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.GE:
                        emit ('if_icmplt NOT_IF_' + str(x), -2)   
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.LT:
                        emit ('if_icmpge NOT_IF_' + str(x), -2)     
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.LE:
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


        def COLON(self):
            return self.getToken(JacParser.COLON, 0)

        def INDENT(self):
            return self.getToken(JacParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(JacParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_st_while




    def st_while(self):

        localctx = JacParser.St_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_st_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(JacParser.WHILE)
            if 1:
                    global y
                    global Loop
                    Loop = True
                    local_y = y
                    print('BEGIN_WHILE_' + str(local_y) + ':')
                
            self.state = 161
            self.comparison_while()
            if 1:
                    y += 1
                
            self.state = 163
            self.match(JacParser.COLON)
            self.state = 164
            self.match(JacParser.INDENT)
            self.state = 166 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 165
                self.statement()
                self.state = 168 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.RETURN) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    emit('goto BEGIN_WHILE_' + str(local_y), 0)
                    emit('END_WHILE_' + str(local_y) + ':', 0)
                    Loop = False
                
            self.state = 171
            self.match(JacParser.DEDENT)
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
            self.ex = None # ExpressionContext
            self.op = None # Token
            self.ex1 = None # ExpressionContext

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
        self.enterRule(localctx, 26, self.RULE_comparison_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            localctx.ex = self.expression()
            self.state = 174
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 175
            localctx.ex1 = self.expression()
            if 1:
                    if localctx.ex.type == 's' or localctx.ex1.type == 's':
                        sys.stderr.write('ERROR: Operator cannot use string type: ' + str((None if localctx.op is None else localctx.op.text)) + '\n')
                        sys.exit(1)
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.EQ:
                        emit ('if_icmpne END_WHILE_' + str(y), -2)
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.NE:
                        emit ('if_icmpeq END_WHILE_' + str(y), -2)    
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.GT:
                        emit ('if_icmple END_WHILE_' + str(y), -2)      
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.GE:
                        emit ('if_icmplt END_WHILE_' + str(y), -2)   
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.LT:
                        emit ('if_icmpge END_WHILE_' + str(y), -2)     
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.LE:
                        emit ('if_icmpgt END_WHILE_' + str(y), -2)
                
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
        self.enterRule(localctx, 28, self.RULE_st_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(JacParser.BREAK)
            if 1:
                    global y
                    global Loop
                    if Loop == True: 
                        print('goto END_WHILE_' + str(y-1))
                    else:
                        sys.stderr.write('ERROR: Break without while')
                        sys.exit(1)
                
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
        self.enterRule(localctx, 30, self.RULE_st_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(JacParser.CONTINUE)
            if 1:
                    global y
                    global Loop
                    if Loop == True: 
                        print('goto BEGIN_WHILE_' + str(y-1))
                    else:
                        sys.stderr.write('ERROR: Continue without while')
                        sys.exit(1)
                
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
        self.enterRule(localctx, 32, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            localctx.t1 = self.term()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.PLUS or _la==JacParser.MINUS:
                self.state = 185
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==JacParser.PLUS or _la==JacParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                localctx.t2 = self.term()
                if 1:
                        if localctx.t1.type == 's' or localctx.t2.type == 's':
                            sys.stderr.write('ERROR: Operators cannot use string type: ' + (None if localctx.op is None else localctx.op.text) + '\n')
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            emit('    iadd', -1)
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.MINUS:
                            emit('    isub', -1)
                        
                    
                self.state = 193
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
            self.f = None # FactorContext
            self._factor = None # FactorContext
            self.op = None # Token
            self.f1 = None # FactorContext

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.FactorContext)
            else:
                return self.getTypedRuleContext(JacParser.FactorContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.TIMES)
            else:
                return self.getToken(JacParser.TIMES, i)

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

        def getRuleIndex(self):
            return JacParser.RULE_term




    def term(self):

        localctx = JacParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            localctx.f = localctx._factor = self.factor()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0):
                self.state = 197
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 198
                localctx.f1 = localctx._factor = self.factor()
                if 1:
                        if localctx.f.type == 's' or localctx.f1.type == 's':
                            sys.stderr.write('ERROR: Operator cannot use string type: ' + (None if localctx.op is None else localctx.op.text) + '\n')
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES: 
                            emit('imul',     -1)
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:  
                            emit('idiv',     -1)
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.REM:   
                            emit('irem',     -1)
                    
                self.state = 205
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
            self._NAME = None # Token
            self.arg = None # ArgumentsContext

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

        def arguments(self):
            return self.getTypedRuleContext(JacParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                        localctx.type = 'i'

                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                localctx._STRING = self.match(JacParser.STRING)
                if 1:
                        emit('ldc ' + (None if localctx._STRING is None else localctx._STRING.text), +1)
                        localctx.type = 's'
                    
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.match(JacParser.OP_PAR)
                self.state = 213
                localctx.e = self.expression()
                self.state = 214
                self.match(JacParser.CL_PAR)
                if 1:
                        localctx.type = localctx.e.type
                    
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                localctx._NAME = self.match(JacParser.NAME)
                if 1:
                        try:
                            index = str(symbolTable.index((None if localctx._NAME is None else localctx._NAME.text)))
                        except ValueError:
                            sys.stderr.write('ERROR: Variable ' + (None if localctx._NAME is None else localctx._NAME.text) + ' not defined in line ' + str((0 if localctx._NAME is None else localctx._NAME.line))  )
                            sys.exit(1)
                        usedVariables[int(index)] = True    
                        type  = typeOfTable[int(index)]
                        if(type == 'i'):
                            emit('iload ' + str(index), +1)
                        elif(type == 's'):
                            emit('aload ' + str(index), +1)
                        localctx.type = type

                    
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 219
                self.match(JacParser.READINT)
                self.state = 220
                self.match(JacParser.OP_PAR)
                self.state = 221
                self.match(JacParser.CL_PAR)
                if 1:
                        #geração de código de leitura de inteiro
                        emit('    invokestatic Runtime/readInt()I', +1)
                        localctx.type = 'i'
                    
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 223
                self.match(JacParser.READSTR)
                self.state = 224
                self.match(JacParser.OP_PAR)
                self.state = 225
                self.match(JacParser.CL_PAR)
                if 1:
                        #geração de código de leitura de string
                        emit('    invokestatic Runtime/readString()Ljava/lang/String;', +1)
                        localctx.type = 's'
                    
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 227
                localctx._NAME = self.match(JacParser.NAME)
                self.state = 228
                self.match(JacParser.OP_PAR)

                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                    self.state = 229
                    localctx.arg = self.arguments()


                self.state = 232
                self.match(JacParser.CL_PAR)
                if 1:
                        if (None if localctx._NAME is None else localctx._NAME.text) in funcTable:
                            index = funcTable.index((None if localctx._NAME is None else localctx._NAME.text))
                            arguments = (None if localctx.arg is None else self._input.getText(localctx.arg.start,localctx.arg.stop)) if (None if localctx.arg is None else self._input.getText(localctx.arg.start,localctx.arg.stop)) else ""
                            if returnFunc[index]:
                                if '"' not in arguments:
                                    real_arguments = arguments.split(',') if len(arguments) > 0 else []
                                    if len(real_arguments) == funcParameters[index]:

                                        func_I = "I" * funcParameters[index]
                                        emit('invokestatic Test/' + (None if localctx._NAME is None else localctx._NAME.text) + '(' + func_I + ')I', 0)
                                        localctx.type = 'i'
                                    else:
                                        sys.stderr.write('ERROR: Wrong number of arguments: '+ str(real_arguments) + ' ' + (None if localctx._NAME is None else localctx._NAME.text) + '\n' )
                                else:
                                    sys.stderr.write('ERROR: All arguments must be integer: ' + (None if localctx._NAME is None else localctx._NAME.text) + '\n')
                            else:
                                sys.stderr.write('ERROR: Function Void must not return: ' + (None if localctx._NAME is None else localctx._NAME.text) + '\n')
                        else:
                            sys.stderr.write('ERROR: Function not defined: ' + (None if localctx._NAME is None else localctx._NAME.text) + '\n')
                    
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





