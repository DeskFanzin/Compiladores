.source Test
.class  public Test
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static main([Ljava/lang/String;)V
    ldc 1    ; delta=1
    istore 0    ; delta=-1
BEGIN_WHILE_0:
    iload 0    ; delta=1
    ldc 10    ; delta=1
    if_icmpgt END_WHILE_0    ; delta=-2
    iload 0    ; delta=1
    ldc 1    ; delta=1
        iadd    ; delta=-1
    istore 0    ; delta=-1
    iload 0    ; delta=1
    ldc 2    ; delta=1
    if_icmpne NOT_IF_0    ; delta=-2
goto BEGIN_WHILE_0
NOT_IF_0:
    goto BEGIN_WHILE_0    ; delta=0
    END_WHILE_0:    ; delta=0
    iload 0    ; delta=1
    ldc 0    ; delta=1
    if_icmpeq NOT_IF_1    ; delta=-2
