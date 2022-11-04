grammar Jac;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
# symbol_table = []
}

/*---------------- LEXER RULES ----------------*/

PRINT : 'print' ;

PLUS  : '+' ;
MINUS : '-' ;
TIMES : '*' ;
OVER  : '/' ;
REM   : '%' ;

OP_PAR: '(' ;
CL_PAR: ')' ;
ATTRIB: '=' ;

NAME : 'a' .. 'z'+ ;

NUMBER: '0'..'9'+ ;

SPACE: (' '|'\t'|'\r'|'\n')+ -> skip ;
COOMENT: '#' ~('\n')* -> skip ;  

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
        # print('\n; symbol_table:', symbol_table)
    }
    ;

statement: st_print | st_attrib
    ;

st_print:
    PRINT OP_PAR
    {if 1:
        print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
    }
    expression CL_PAR
    {if 1:
        print('    invokevirtual java/io/PrintStream/println(I)V\n')
    }
    ;

st_attrib: NAME ATTRIB expression
    {if 1:
        print('    istore 0')
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
        print('    ldc ' + $NUMBER.text)
        # symbol_table.append($NUMBER.text)
    }
    | OP_PAR expression CL_PAR
    | NAME
    {if 1:
        print('    iload 0')
    }
    ;

