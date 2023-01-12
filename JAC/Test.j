.source Test.src
.class  public Test
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static main([Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;    ; delta=1
    ldc "hello world"    ; delta=1
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    ; delta=-2
        getstatic java/lang/System/out Ljava/io/PrintStream;    ; delta=1
        invokevirtual java/io/PrintStream/println()V
    ; delta=-1
    ldc 2    ; delta=1
    ldc 10    ; delta=1
    iadd
    istore 0
    getstatic java/lang/System/out Ljava/io/PrintStream;    ; delta=1
    ldc 2    ; delta=1
    invokevirtual java/io/PrintStream/print(I)V
    ; delta=-2
        getstatic java/lang/System/out Ljava/io/PrintStream;    ; delta=1
        invokevirtual java/io/PrintStream/println()V
    ; delta=-1
    getstatic java/lang/System/out Ljava/io/PrintStream;    ; delta=1
    iload 0
    invokevirtual java/io/PrintStream/print(I)V
    ; delta=-2
        getstatic java/lang/System/out Ljava/io/PrintStream;    ; delta=1
        invokevirtual java/io/PrintStream/println()V
    ; delta=-1
    return
.limit stack 10
.end method

; symbol_table: []
