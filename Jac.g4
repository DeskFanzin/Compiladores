grammar Jac;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
import sys
symbol_table = []
stack_cur = 0
stack_max = 0
def enit(bytecode, delta):
    global stack_cur, stack_max
    print('    '+ bytecode + '    ; delta=' + delta)
    stack_cur += delta
    if stack_cur > stack_max:
    stack_max = stack_cur
}



/*---------------- LEXER RULES ----------------*/

IF      : 'if'     ;
PRINT   : 'print'  ;
READINT : 'readint';

PLUS  : '+' ;
MINUS : '-' ;
TIMES : '*' ;
OVER  : '/' ;
REM   : '%' ;

LT    : '<' ;

OP_PAR : '(' ;
CL_PAR : ')' ;
OP_CUR : '{' ;
CL_CUR : '}' ;
ATTRIB : '=' ;
COMMA  : ',' ;

NAME : 'a' .. 'z'+ ;

NUMBER : '0'..'9'+ ;

SPACE: (' '|'\t'|'\r'|'\n')+ -> skip ;
COOMENT: '#' ~('\n')*        -> skip ;

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

statement: st_print | st_attrib
    ;

st_print:
    PRINT OP_PAR (
    {if 1:
        enit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    expression
    {if 1:
        enit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
    }
    ( COMMA
        {if 1:
        enit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
        } 
        expression
        {if 1:
        enit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
        }
    )*
    )? CL_PAR
       {if 1:
        enit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
        enit('    invokevirtual java/io/PrintStream/println()V\n', -1)
        }
    ;

st_attrib: NAME ATTRIB expression
    {if 1:
        print('    istore 0')
    }
    ;

st_if: IF comparison OP_CUR 
    ( statement )+
    CL_CUR
    {if 1:
        print('NOT_IF_0:')
    }
    ;

comparison: expression LT expression
    { if 1:
        emit ('if_icmpge NOT_IF_0', -2)
    }
    ;

expression:
    term ( ( op = PLUS | MINUS ) term
    {if 1:
        if $op.type == JacParser.PLUS:
            print('    iadd')
        else:
            print('    isub')    
    }
    )*
    ;

term: factor ( ( op = TIMES | OVER | REM ) factor
    {if 1:
        if $op.type == JacParser.TIMES:
            print('    imul')
        elif $op.type == JacParser.OVER:
            print('    idiv')
        else:
            print('    irem')
    }
    )*
    ;

factor: NUMBER
    {if 1:
        print('    ldc ' + $NUMBER.text +1)
        # symbol_table.append($NUMBER.text)
    }
    | OP_PAR expression CL_PAR
    | NAME
    {if 1:
        print('    iload 0')
    }
    | READINT OP_PAR CL_PAR
    {
        #geração de código de leitura de inteiro
        enit('    invokestatic Runtime/readInt()I', +1)
    }
    ;
