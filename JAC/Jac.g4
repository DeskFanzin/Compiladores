grammar Jac;

/*--Feito por: Gabiel Martins(142356)--*/
/*--Auxílio de alunos: Arthur Bubolz(140548), Andre Maurell(142365), William Souza(76901) */

/*---------------- LEXER INTERNALS ----------------*/

@lexer::header
{
from antlr_denter.DenterHelper import DenterHelper
from JacParser import JacParser
}

@lexer::members
{
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
    for i in range(len(self.symbol_table)):
        if self.symbol_table[i] == name:
            return self.type_table[i]

    sys.stderr.write('ERROR: Variable ' + name + ' not declared')
    sys.exit(1)
}


/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
import sys
symbol_table = []
type_table = []
used_vars = []
function_table = []
function_parameters = []
function_return = []
x = 0
y = 0
Loop = False
stack_cur = 0
stack_max = 0
def emit(bytecode, delta):
    global stack_cur, stack_max
    print('    '+ bytecode + '    ; delta=' + str(delta))
    stack_cur += delta
    if stack_cur > stack_max:
        stack_max = stack_cur

def resetFunctionMetrics():
    global symbol_table
    global type_table
    global used_vars
    global stack_max
    global stack_cur

    symbol_table = []
    type_table = []
    used_table = []
    stack_max = 0
    stack_cur = 0

}



/*---------------- LEXER RULES ----------------*/

tokens { INDENT, DEDENT }
IF      : 'if'     ;
PRINT   : 'print'  ;
READINT : 'readint';
READSTR  : 'readstr';
WHILE   : 'while'  ;
BREAK   : 'break'  ;
CONTINUE: 'continue';
DEF     : 'def'    ;
RETURN  : 'return' ;

PLUS  : '+' ;
MINUS : '-' ;
TIMES : '*' ;
OVER  : '/' ;
REM   : '%' ;

EQ    : '==' ;
NE    : '!=' ;
GT    : '>' ;
GE    : '>=' ;
LT    : '<' ;
LE    : '<=' ;

OP_PAR : '(' ;
CL_PAR : ')' ;
OP_CUR : '{' ;
CL_CUR : '}' ;
COLON :  ':' ;
ATTRIB : '=' ;
COMMA  : ',' ;

NAME : 'a' .. 'z'+ ;

NUMBER : '0'..'9'+ ;

STRING : '"' ~('"')* '"' ;

COMMENT: '#' ~('\n')* -> skip ;
NL: ('\r'? '\n' ' '*);
SPACE: (' '|'\t')+ -> skip ;

/*---------------- PARSER RULES ----------------*/

program:
    {if 1:
        print('.source Test')
        print('.class  public Test')
        print('.super  java/lang/Object\n')
        print('.method public <init>()V')
        print('    aload_0')
        print('    invokenonvirtual java/lang/Object/<init>()V')
        print('    return')
        print('.end method\n')
    }
    ( function )*
    main
    ;



main:
    {if 1:
        print('.method public static main([Ljava/lang/String;)V')
    }
    ( statement )+
    
    {if 1:
        for i in range(len(used_vars)):
            if used_vars[i] == False:
                try:
                    sys.stderr.write('WARNING: Variable ' + symbol_table[i] + ' was declared but not used\n')
                except IndexError:
                    pass
        print('    return')
        if len(symbol_table) != 0:
            print('.limit locals ' + str(len(symbol_table)))
        else:
            print('.limit locals 1')
        print('.limit stack ' + str(stack_max))
        print('.end method')
        print('\n; symbol_tabe:', symbol_table)
        print('; type_table:', type_table)
        print('; used_vars:', used_vars)

    }
    ;
    
statement: NL | st_print | st_attrib | st_if | st_while | st_break | st_continue | st_call | st_return
    ;

st_print:
    PRINT OP_PAR (
    {if 1:
        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    e1 = expression
    {if 1:
        if $e1.type == 'i':
            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
        elif $e1.type == 's':
            emit ('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
        else:
            sys.stderr.write('ERROR: Invalid type for print')
            sys.exit(1)
    }
    ( COMMA
        {if 1:
            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
        } 
        e2 = expression
        {if 1:
            if $e2.type == 'i':
                emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
            elif $e2.type == 's':
                emit ('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
            else:
                sys.stderr.write('ERROR: Invalid type for print')
                sys.exit(1)
        }
    )*
    )? CL_PAR
       {if 1:
            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
            emit('    invokevirtual java/io/PrintStream/println()V\n', -1)
        }
    ;

st_attrib: NAME ATTRIB op = expression
    {if 1:
        if $NAME.text not in symbol_table:
            symbol_table.append($NAME.text)
            type_table.append($expression.type)
            used_vars.append(False)

        index = str(symbol_table.index($NAME.text))
        type  = type_table[int(index)]
        if(type == $op.type):
            if(type == 'i'):
                emit('istore ' + str(index), -1)
            elif(type == 's'):
                emit('astore ' + str(index), -1)
        if(type == 'i' and $op.type == 's'):
            sys.stderr.write('ERROR: Expected type int for assignment in variable ' + $NAME.text + ' in line ' + str($NAME.line) + '\n')
        if(type == 's' and $op.type == 'i'):
            sys.stderr.write('ERROR: Expected type string for assignment in variable ' + $NAME.text + ' in line ' + str($NAME.line) + '\n')
    }
    ;

st_if: IF comparison_if 
    {if 1:
        global x 
        local_x = x
        x += 1
    }
    COLON INDENT  ( statement )+ 
    {if 1:
        print('NOT_IF_' + str(local_x) + ':')
    }
    DEDENT 
    ;

comparison_if: ex = expression op = ( EQ | NE | GT | GE | LT | LE ) ex1 = expression
    {if 1:
        if $ex.type == 's' or $ex1.type == 's':
            sys.stderr.write('ERROR: Operator cannot use string type: ' + str($op.text) + '\n')
            sys.exit(1)
        if $op.type == JacParser.EQ:
            emit ('if_icmpne NOT_IF_' + str(x), -2)
        if $op.type == JacParser.NE:
            emit ('if_icmpeq NOT_IF_' + str(x), -2)    
        if $op.type == JacParser.GT:
            emit ('if_icmple NOT_IF_' + str(x), -2)      
        if $op.type == JacParser.GE:
            emit ('if_icmplt NOT_IF_' + str(x), -2)   
        if $op.type == JacParser.LT:
            emit ('if_icmpge NOT_IF_' + str(x), -2)     
        if $op.type == JacParser.LE:
            emit ('if_icmpgt NOT_IF_' + str(x), -2)                 
    }
    ;


st_while: WHILE
    {if 1:
        global y
        global Loop
        Loop = True
        local_y = y
        print('BEGIN_WHILE_' + str(local_y) + ':')
    } 
    comparison_while
    {if 1:
        y += 1
    }
    COLON INDENT ( statement )+
    {if 1:
        emit('goto BEGIN_WHILE_' + str(local_y), 0)
        emit('END_WHILE_' + str(local_y) + ':', 0)
        Loop = False
    }
    DEDENT
    ;

comparison_while: ex = expression op = ( EQ | NE | GT | GE | LT | LE ) ex1 = expression
    {if 1:
        if $ex.type == 's' or $ex1.type == 's':
            sys.stderr.write('ERROR: Operator cannot use string type: ' + str($op.text) + '\n')
            sys.exit(1)
        if $op.type == JacParser.EQ:
            emit ('if_icmpne END_WHILE_' + str(y), -2)
        if $op.type == JacParser.NE:
            emit ('if_icmpeq END_WHILE_' + str(y), -2)    
        if $op.type == JacParser.GT:
            emit ('if_icmple END_WHILE_' + str(y), -2)      
        if $op.type == JacParser.GE:
            emit ('if_icmplt END_WHILE_' + str(y), -2)   
        if $op.type == JacParser.LT:
            emit ('if_icmpge END_WHILE_' + str(y), -2)     
        if $op.type == JacParser.LE:
            emit ('if_icmpgt END_WHILE_' + str(y), -2)
    }
    ;

st_break: BREAK
    {if 1:
        global y
        global Loop
        if Loop == True: 
            print('goto END_WHILE_' + str(y-1))
        else:
            sys.stderr.write('ERROR: Break without while')
            sys.exit(1)
    }
    ;

st_continue: CONTINUE
    {if 1:
        global y
        global Loop
        if Loop == True: 
            print('goto BEGIN_WHILE_' + str(y-1))
        else:
            sys.stderr.write('ERROR: Continue without while')
            sys.exit(1)
    }
    ;

function : DEF NAME OP_PAR ((p = parameters)?) CL_PAR COLON ((ft = NAME)?) INDENT
{if 1:
    if $NAME.text not in function_table:
        parameters = $p.text.split(',') if $p.text else []
        if len(parameters) == len(set(parameters)):
            function_table.append($NAME.text)
            function_parameters.append(len(parameters))
            function_return.append(True if $ft.text == 'int' else False)
            print('.method public static '+$NAME.text+'('+('I' * len(parameters))+')'+('I' if $ft.text else 'V'))

            for p in parameters:
                if p not in symbol_table:
                    symbol_table.append(p)
                    type_table.append('i')
                    used_vars.append(False)
        else:
            sys.stderr.write('ERROR: Parameter(s) must be unique: ' + str(parameters))
            sys.exit(1)
    else:
        sys.stderr.write('ERROR: Function already defined: ' + $NAME.text )
        sys.exit(1)
  
}
( st = statement )* DEDENT
{if 1:

    print('    return')
    print('.limit stack ' + str(stack_max))
    print('.limit locals ' + str(len(symbol_table)))
    print(';symbol_table ' + str(symbol_table))
    print('.end method')
    resetFunctionMetrics()
}
;


parameters : NAME (COMMA NAME) *;

st_call: NAME OP_PAR ((arg = arguments)?) CL_PAR
{if 1:

    if $NAME.text in function_table:
        index = function_table.index($NAME.text)
        arguments = $arg.text if $arg.text else ""
        if not function_return[index]:
            if '"' not in arguments:
                real_arguments = arguments.split(',') if len(arguments) > 0 else []
                if len(real_arguments) == function_parameters[index]:
                    func_I = "I" * function_parameters[index]
                    emit('invokestatic Test/' + $NAME.text + '(' + func_I + ')V', 0)
                else:
                    sys.stderr.write('ERROR: Wrong number of arguments: '+ $NAME.text + '\n')
            else:
                sys.stderr.write('ERROR: all arguments must be integer: ' + $NAME.text + '\n')
        else:
           sys.stderr.write('ERROR: Function missing return statement: ' + $NAME.text + '\n')
    else:
        sys.stderr.write('ERROR: Function not defined: ' + $NAME.text + '\n')
}; 

arguments : expression (COMMA expression) *;

st_return: RETURN ex = expression
{if 1:
    if $ex.type == 'i':
        emit('ireturn', 0)
    else:
        sys.stderr.write('ERROR: Return type must be integer: '+ $ex.text + ' is ' + '"' + $ex.type +'"' + '\n')
};


expression returns [type]: t1 = term ( op = ( PLUS | MINUS ) t2 = term
    {if 1:
        if $t1.type == 's' or $t2.type == 's':
            sys.stderr.write('ERROR: Operators cannot use string type: ' + $op.text + '\n')
        if $op.type == JacParser.PLUS:
            emit('    iadd', -1)
        if $op.type == JacParser.MINUS:
            emit('    isub', -1)
        
    }
    )*
    {if 1:
        $type = $t1.type
    }
    ;

term returns [type]: f = factor ( op = ( TIMES | OVER | REM ) f1 = factor
    {if 1:
        if $f.type == 's' or $f1.type == 's':
            sys.stderr.write('ERROR: Operator cannot use string type: ' + $op.text + '\n')
        if $op.type == JacParser.TIMES: 
            emit('imul',     -1)
        if $op.type == JacParser.OVER:  
            emit('idiv',     -1)
        if $op.type == JacParser.REM:   
            emit('irem',     -1)
    }
    )*
    {if 1:
        $type = $factor.type
    }
    ;

factor returns [type]: NUMBER
    {if 1:
        emit('ldc ' + $NUMBER.text, +1)
        $type = 'i'

    }
    | STRING
    {if 1:
        emit('ldc ' + $STRING.text, +1)
        $type = 's'
    }
    | OP_PAR e = expression CL_PAR
    {if 1:
        $type = $e.type
    }
    | NAME
    {if 1:
        try:
            index = str(symbol_table.index($NAME.text))
        except ValueError:
            sys.stderr.write('ERROR: Variable ' + $NAME.text + ' not defined in line ' + str($NAME.line)  )
            sys.exit(1)
        used_vars[int(index)] = True    
        type  = type_table[int(index)]
        if(type == 'i'):
            emit('iload ' + str(index), +1)
        elif(type == 's'):
            emit('aload ' + str(index), +1)
        $type = type

    }
    | READINT OP_PAR CL_PAR
    {if 1:
        #geração de código de leitura de inteiro
        emit('    invokestatic Runtime/readInt()I', +1)
        $type = 'i'
    }
    | READSTR OP_PAR CL_PAR
    {if 1:
        #geração de código de leitura de string
        emit('    invokestatic Runtime/readString()Ljava/lang/String;', +1)
        $type = 's'
    }
    | NAME OP_PAR ((arg = arguments)?) CL_PAR
    {if 1:
        if $NAME.text in function_table:
            index = function_table.index($NAME.text)
            arguments = $arg.text if $arg.text else ""
            if function_return[index]:
                if '"' not in arguments:
                    real_arguments = arguments.split(',') if len(arguments) > 0 else []
                    if len(real_arguments) == function_parameters[index]:

                        func_I = "I" * function_parameters[index]
                        emit('invokestatic Test/' + $NAME.text + '(' + func_I + ')I', 0)
                        $type = 'i'
                    else:
                        sys.stderr.write('ERROR: Wrong number of arguments: '+ str(real_arguments) + ' ' + $NAME.text + '\n' )
                else:
                    sys.stderr.write('ERROR: All arguments must be integer: ' + $NAME.text + '\n')
            else:
                sys.stderr.write('ERROR: Function Void must not return: ' + $NAME.text + '\n')
        else:
            sys.stderr.write('ERROR: Function not defined: ' + $NAME.text + '\n')
    }
    ;
