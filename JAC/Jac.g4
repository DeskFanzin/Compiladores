grammar Jac;

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
}


/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
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
        print('.source Test.src')
        print('.class  public Test')
        print('.super  java/lang/Object\n')
        print('.method public <init>()V')
        print('    aload_0')
        print('    invokenonvirtual java/lang/Object/<init>()V')
        print('    return')
        print('.end method\n')
    }
    main
    ;



main:
    {if 1:
        print('.method public static main([Ljava/lang/String;)V\n')
    }
    ( statement )+
    {if 1:
        print('    return')
        print('.limit stack 10')
        print('.end method')
        print('\n; symbol_table:', symbol_table)
    }
    ;

statement: NL | st_print | st_attrib | st_if | st_while | st_break | st_continue
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
            print('*****HELP*****')
    }
    ( COMMA
        {if 1:
        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
        } 
        expression
        {if 1:
        emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
        }
    )*
    )? CL_PAR
       {if 1:
        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
        emit('    invokevirtual java/io/PrintStream/println()V\n', -1)
        }
    ;

st_attrib: NAME ATTRIB expression
    {if 1:
        print('    istore 0')
    }
    ;

st_if: IF comparison_if 
    {if 1:
        global x 
        local_x = x
        x += 1
    }
    OP_CUR ( statement )+ 
    {if 1:
        print('NOT_IF_' + str(local_x) + ':')
    }
    CL_CUR
    ;

comparison_if: expression op = ( EQ | NE | GT | GE | LT | LE ) expression
    {if 1:
        if $op.type == JacParser.EQ:
            emit ('if_icmpne NOT_IF_' + str(x), -2)
        elif $op.type == JacParser.NE:
            emit ('if_icmpeq NOT_IF_' + str(x), -2)    
        elif $op.type == JacParser.GT:
            emit ('if_icmple NOT_IF_' + str(x), -2)      
        elif $op.type == JacParser.GE:
            emit ('if_icmplt NOT_IF_' + str(x), -2)   
        elif $op.type == JacParser.LT:
            emit ('if_icmpge NOT_IF_' + str(x), -2)     
        elif $op.type == JacParser.LE:
            emit ('if_icmpgt NOT_IF_' + str(x), -2)                 
    }
    ;


st_while: WHILE
    {if 1:
        global y 
        local_y = y
        print('BEGIN_WHILE_' + str(local_y) + ':')
    } 
    comparison_while
    {if 1:
        y += 1
    }
    OP_CUR ( statement )+ 
    {if 1:
        emit('goto BEGIN_WHILE_' + str(local_y), 0)
        print('END_WHILE_' + str(local_y) + ':')
    }
    CL_CUR
    ;

comparison_while: expression op = ( EQ | NE | GT | GE | LT | LE ) expression
    {if 1:
        if $op.type == JacParser.EQ:
            emit ('if_icmpne END_WHILE_' + str(x), -2)
        elif $op.type == JacParser.NE:
            emit ('if_icmpeq END_WHILE_' + str(x), -2)    
        elif $op.type == JacParser.GT:
            emit ('if_icmple END_WHILE_' + str(x), -2)      
        elif $op.type == JacParser.GE:
            emit ('if_icmplt END_WHILE_' + str(x), -2)   
        elif $op.type == JacParser.LT:
            emit ('if_icmpge END_WHILE_' + str(x), -2)     
        elif $op.type == JacParser.LE:
            emit ('if_icmpgt END_WHILE_' + str(x), -2)                 
    }
    ;

st_break: BREAK
    {if 1:
        print('goto END_WHILE_' + str(y-1))
    }
    ;

st_continue: CONTINUE
    {if 1:
        print('goto BEGIN_WHILE_' + str(y-1))
    }
    ;





expression returns [type]: t1 = term ( op = ( PLUS | MINUS ) t2 = term
    {if 1:
        if $op.type == JacParser.PLUS:
            print('    iadd')
        else:
            print('    isub')    
    }
    )*
    {if 1:
        $type = $t1.type
    }
    ;

term returns [type]: factor ( ( op = TIMES | OVER | REM ) factor
    {if 1:
        if $op.type == JacParser.TIMES:
            print('    imul')
        elif $op.type == JacParser.OVER:
            print('    idiv')
        else:
            print('    irem')
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
        $type = e.type
    }
    | NAME
    {if 1:
        print('    iload 0')
        $type = 'i'
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

    ;
