.source Test.src
.class  public Test
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static main([Ljava/lang/String;)V

    ldc 2
    istore 0
    getstatic java/lang/System/out Ljava/io/PrintStream;
    iload 0
    ldc 10
    iadd
    invokevirtual java/io/PrintStream/println(I)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 1
    ldc 2
    iadd
    invokevirtual java/io/PrintStream/println(I)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 1
    ldc 4
    isub
    invokevirtual java/io/PrintStream/println(I)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 2
    ldc 2
    irem
    invokevirtual java/io/PrintStream/println(I)V

    return
.limit stack 10
.end method
