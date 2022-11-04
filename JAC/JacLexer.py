# Generated from Jac.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,64,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,1,0,
        1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,
        45,8,8,11,8,12,8,46,1,9,4,9,50,8,9,11,9,12,9,51,1,9,1,9,1,10,1,10,
        5,10,58,8,10,10,10,12,10,61,9,10,1,10,1,10,0,0,11,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,2,3,0,9,10,13,13,32,32,
        1,0,10,10,66,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,
        1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,0,7,33,
        1,0,0,0,9,35,1,0,0,0,11,37,1,0,0,0,13,39,1,0,0,0,15,41,1,0,0,0,17,
        44,1,0,0,0,19,49,1,0,0,0,21,55,1,0,0,0,23,24,5,112,0,0,24,25,5,114,
        0,0,25,26,5,105,0,0,26,27,5,110,0,0,27,28,5,116,0,0,28,2,1,0,0,0,
        29,30,5,43,0,0,30,4,1,0,0,0,31,32,5,45,0,0,32,6,1,0,0,0,33,34,5,
        42,0,0,34,8,1,0,0,0,35,36,5,47,0,0,36,10,1,0,0,0,37,38,5,37,0,0,
        38,12,1,0,0,0,39,40,5,40,0,0,40,14,1,0,0,0,41,42,5,41,0,0,42,16,
        1,0,0,0,43,45,2,48,57,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,
        0,46,47,1,0,0,0,47,18,1,0,0,0,48,50,7,0,0,0,49,48,1,0,0,0,50,51,
        1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,6,9,0,0,
        54,20,1,0,0,0,55,59,5,35,0,0,56,58,8,1,0,0,57,56,1,0,0,0,58,61,1,
        0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,
        63,6,10,0,0,63,22,1,0,0,0,4,0,46,51,59,1,6,0,0
    ]

class JacLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    PLUS = 2
    MINUS = 3
    TIMES = 4
    OVER = 5
    REM = 6
    OP_PAR = 7
    CL_PAR = 8
    NUMBER = 9
    SPACE = 10
    COOMENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", 
            "CL_PAR", "NUMBER", "SPACE", "COOMENT" ]

    ruleNames = [ "PRINT", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", 
                  "CL_PAR", "NUMBER", "SPACE", "COOMENT" ]

    grammarFileName = "Jac.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


