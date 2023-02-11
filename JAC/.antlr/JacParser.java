// Generated from c:\Users\gabri\OneDrive\Área de Trabalho\Tudo\codes\jac\JAC\Jac.g4 by ANTLR 4.9.2

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


import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JacParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, PRINT=2, READINT=3, READSTR=4, WHILE=5, BREAK=6, CONTINUE=7, DEF=8, 
		RETURN=9, PLUS=10, MINUS=11, TIMES=12, OVER=13, REM=14, EQ=15, NE=16, 
		GT=17, GE=18, LT=19, LE=20, OP_PAR=21, CL_PAR=22, OP_CUR=23, CL_CUR=24, 
		COLON=25, ATTRIB=26, COMMA=27, NAME=28, NUMBER=29, STRING=30, COMMENT=31, 
		NL=32, SPACE=33, INDENT=34, DEDENT=35;
	public static final int
		RULE_program = 0, RULE_main = 1, RULE_statement = 2, RULE_st_print = 3, 
		RULE_st_attrib = 4, RULE_st_if = 5, RULE_comparison_if = 6, RULE_st_while = 7, 
		RULE_comparison_while = 8, RULE_st_break = 9, RULE_st_continue = 10, RULE_function = 11, 
		RULE_parameters = 12, RULE_st_call = 13, RULE_arguments = 14, RULE_st_return = 15, 
		RULE_expression = 16, RULE_term = 17, RULE_factor = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main", "statement", "st_print", "st_attrib", "st_if", "comparison_if", 
			"st_while", "comparison_while", "st_break", "st_continue", "function", 
			"parameters", "st_call", "arguments", "st_return", "expression", "term", 
			"factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'print'", "'readint'", "'readstr'", "'while'", "'break'", 
			"'continue'", "'def'", "'return'", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'('", "')'", "'{'", "'}'", 
			"':'", "'='", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "PRINT", "READINT", "READSTR", "WHILE", "BREAK", "CONTINUE", 
			"DEF", "RETURN", "PLUS", "MINUS", "TIMES", "OVER", "REM", "EQ", "NE", 
			"GT", "GE", "LT", "LE", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "COLON", 
			"ATTRIB", "COMMA", "NAME", "NUMBER", "STRING", "COMMENT", "NL", "SPACE", 
			"INDENT", "DEDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Jac.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public JacParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			if 1:
			        print('.source Test')
			        print('.class  public Test')
			        print('.super  java/lang/Object\n')
			        print('.method public <init>()V')
			        print('    aload_0')
			        print('    invokenonvirtual java/lang/Object/<init>()V')
			        print('    return')
			        print('.end method\n')
			    
			setState(42);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DEF) {
				{
				{
				setState(39);
				function();
				}
				}
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(45);
			main();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			if 1:
			        print('.method public static main([Ljava/lang/String;)V')
			    
			setState(49); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(48);
				statement();
				}
				}
				setState(51); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << PRINT) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << RETURN) | (1L << NAME) | (1L << NL))) != 0) );
			if 1:
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
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public TerminalNode NL() { return getToken(JacParser.NL, 0); }
		public St_printContext st_print() {
			return getRuleContext(St_printContext.class,0);
		}
		public St_attribContext st_attrib() {
			return getRuleContext(St_attribContext.class,0);
		}
		public St_ifContext st_if() {
			return getRuleContext(St_ifContext.class,0);
		}
		public St_whileContext st_while() {
			return getRuleContext(St_whileContext.class,0);
		}
		public St_breakContext st_break() {
			return getRuleContext(St_breakContext.class,0);
		}
		public St_continueContext st_continue() {
			return getRuleContext(St_continueContext.class,0);
		}
		public St_callContext st_call() {
			return getRuleContext(St_callContext.class,0);
		}
		public St_returnContext st_return() {
			return getRuleContext(St_returnContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(64);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(55);
				match(NL);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				st_print();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(57);
				st_attrib();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(58);
				st_if();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(59);
				st_while();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(60);
				st_break();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(61);
				st_continue();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(62);
				st_call();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(63);
				st_return();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_printContext extends ParserRuleContext {
		public ExpressionContext e1;
		public ExpressionContext e2;
		public TerminalNode PRINT() { return getToken(JacParser.PRINT, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(JacParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JacParser.COMMA, i);
		}
		public St_printContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_print; }
	}

	public final St_printContext st_print() throws RecognitionException {
		St_printContext _localctx = new St_printContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_st_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(PRINT);
			setState(67);
			match(OP_PAR);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READINT) | (1L << READSTR) | (1L << OP_PAR) | (1L << NAME) | (1L << NUMBER) | (1L << STRING))) != 0)) {
				{
				if 1:
				        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
				    
				setState(69);
				((St_printContext)_localctx).e1 = expression();
				if 1:
				        if ((St_printContext)_localctx).e1.type == 'i':
				            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
				        elif ((St_printContext)_localctx).e1.type == 's':
				            emit ('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
				        else:
				            sys.stderr.write('ERROR: Invalid type for print')
				            sys.exit(1)
				    
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(71);
					match(COMMA);
					if 1:
					            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
					        
					setState(73);
					((St_printContext)_localctx).e2 = expression();
					if 1:
					            if ((St_printContext)_localctx).e2.type == 'i':
					                emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
					            elif ((St_printContext)_localctx).e2.type == 's':
					                emit ('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
					            else:
					                sys.stderr.write('ERROR: Invalid type for print')
					                sys.exit(1)
					        
					}
					}
					setState(80);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(83);
			match(CL_PAR);
			if 1:
			            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
			            emit('    invokevirtual java/io/PrintStream/println()V\n', -1)
			        
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_attribContext extends ParserRuleContext {
		public Token NAME;
		public ExpressionContext op;
		public ExpressionContext expression;
		public TerminalNode NAME() { return getToken(JacParser.NAME, 0); }
		public TerminalNode ATTRIB() { return getToken(JacParser.ATTRIB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public St_attribContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_attrib; }
	}

	public final St_attribContext st_attrib() throws RecognitionException {
		St_attribContext _localctx = new St_attribContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_st_attrib);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			((St_attribContext)_localctx).NAME = match(NAME);
			setState(87);
			match(ATTRIB);
			setState(88);
			((St_attribContext)_localctx).op = ((St_attribContext)_localctx).expression = expression();
			if 1:
			        if (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) not in symbol_table:
			            symbol_table.append((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))
			            type_table.append(((St_attribContext)_localctx).expression.type)
			            used_vars.append(False)

			        index = str(symbol_table.index((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null)))
			        type  = type_table[int(index)]
			        if(type == ((St_attribContext)_localctx).op.type):
			            if(type == 'i'):
			                emit('istore ' + str(index), -1)
			            elif(type == 's'):
			                emit('astore ' + str(index), -1)
			        if(type == 'i' and ((St_attribContext)_localctx).op.type == 's'):
			            sys.stderr.write('ERROR: Expected type int for assignment in variable ' + (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) + ' in line ' + str((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getLine():0)) + '\n')
			        if(type == 's' and ((St_attribContext)_localctx).op.type == 'i'):
			            sys.stderr.write('ERROR: Expected type string for assignment in variable ' + (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) + ' in line ' + str((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getLine():0)) + '\n')
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_ifContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(JacParser.IF, 0); }
		public Comparison_ifContext comparison_if() {
			return getRuleContext(Comparison_ifContext.class,0);
		}
		public TerminalNode COLON() { return getToken(JacParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(JacParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(JacParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public St_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_if; }
	}

	public final St_ifContext st_if() throws RecognitionException {
		St_ifContext _localctx = new St_ifContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_st_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(IF);
			setState(92);
			comparison_if();
			if 1:
			        global x 
			        local_x = x
			        x += 1
			    
			setState(94);
			match(COLON);
			setState(95);
			match(INDENT);
			setState(97); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(96);
				statement();
				}
				}
				setState(99); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << PRINT) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << RETURN) | (1L << NAME) | (1L << NL))) != 0) );
			if 1:
			        print('NOT_IF_' + str(local_x) + ':')
			    
			setState(102);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Comparison_ifContext extends ParserRuleContext {
		public ExpressionContext ex;
		public Token op;
		public ExpressionContext ex1;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(JacParser.EQ, 0); }
		public TerminalNode NE() { return getToken(JacParser.NE, 0); }
		public TerminalNode GT() { return getToken(JacParser.GT, 0); }
		public TerminalNode GE() { return getToken(JacParser.GE, 0); }
		public TerminalNode LT() { return getToken(JacParser.LT, 0); }
		public TerminalNode LE() { return getToken(JacParser.LE, 0); }
		public Comparison_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison_if; }
	}

	public final Comparison_ifContext comparison_if() throws RecognitionException {
		Comparison_ifContext _localctx = new Comparison_ifContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_comparison_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			((Comparison_ifContext)_localctx).ex = expression();
			setState(105);
			((Comparison_ifContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ) | (1L << NE) | (1L << GT) | (1L << GE) | (1L << LT) | (1L << LE))) != 0)) ) {
				((Comparison_ifContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(106);
			((Comparison_ifContext)_localctx).ex1 = expression();
			if 1:
			        if ((Comparison_ifContext)_localctx).ex.type == 's' or ((Comparison_ifContext)_localctx).ex1.type == 's':
			            sys.stderr.write('ERROR: Operator cannot use string type: ' + str((((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getText():null)) + '\n')
			            sys.exit(1)
			        if (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.EQ:
			            emit ('if_icmpne NOT_IF_' + str(x), -2)
			        if (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.NE:
			            emit ('if_icmpeq NOT_IF_' + str(x), -2)    
			        if (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.GT:
			            emit ('if_icmple NOT_IF_' + str(x), -2)      
			        if (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.GE:
			            emit ('if_icmplt NOT_IF_' + str(x), -2)   
			        if (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.LT:
			            emit ('if_icmpge NOT_IF_' + str(x), -2)     
			        if (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.LE:
			            emit ('if_icmpgt NOT_IF_' + str(x), -2)                 
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_whileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(JacParser.WHILE, 0); }
		public Comparison_whileContext comparison_while() {
			return getRuleContext(Comparison_whileContext.class,0);
		}
		public TerminalNode COLON() { return getToken(JacParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(JacParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(JacParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public St_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_while; }
	}

	public final St_whileContext st_while() throws RecognitionException {
		St_whileContext _localctx = new St_whileContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_st_while);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(WHILE);
			if 1:
			        global y
			        global Loop
			        Loop = True
			        local_y = y
			        print('BEGIN_WHILE_' + str(local_y) + ':')
			    
			setState(111);
			comparison_while();
			if 1:
			        y += 1
			    
			setState(113);
			match(COLON);
			setState(114);
			match(INDENT);
			setState(116); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(115);
				statement();
				}
				}
				setState(118); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << PRINT) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << RETURN) | (1L << NAME) | (1L << NL))) != 0) );
			if 1:
			        emit('goto BEGIN_WHILE_' + str(local_y), 0)
			        emit('END_WHILE_' + str(local_y) + ':', 0)
			        Loop = False
			    
			setState(121);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Comparison_whileContext extends ParserRuleContext {
		public ExpressionContext ex;
		public Token op;
		public ExpressionContext ex1;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(JacParser.EQ, 0); }
		public TerminalNode NE() { return getToken(JacParser.NE, 0); }
		public TerminalNode GT() { return getToken(JacParser.GT, 0); }
		public TerminalNode GE() { return getToken(JacParser.GE, 0); }
		public TerminalNode LT() { return getToken(JacParser.LT, 0); }
		public TerminalNode LE() { return getToken(JacParser.LE, 0); }
		public Comparison_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison_while; }
	}

	public final Comparison_whileContext comparison_while() throws RecognitionException {
		Comparison_whileContext _localctx = new Comparison_whileContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_comparison_while);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			((Comparison_whileContext)_localctx).ex = expression();
			setState(124);
			((Comparison_whileContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ) | (1L << NE) | (1L << GT) | (1L << GE) | (1L << LT) | (1L << LE))) != 0)) ) {
				((Comparison_whileContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(125);
			((Comparison_whileContext)_localctx).ex1 = expression();
			if 1:
			        if ((Comparison_whileContext)_localctx).ex.type == 's' or ((Comparison_whileContext)_localctx).ex1.type == 's':
			            sys.stderr.write('ERROR: Operator cannot use string type: ' + str((((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getText():null)) + '\n')
			            sys.exit(1)
			        if (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.EQ:
			            emit ('if_icmpne END_WHILE_' + str(y), -2)
			        if (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.NE:
			            emit ('if_icmpeq END_WHILE_' + str(y), -2)    
			        if (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.GT:
			            emit ('if_icmple END_WHILE_' + str(y), -2)      
			        if (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.GE:
			            emit ('if_icmplt END_WHILE_' + str(y), -2)   
			        if (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.LT:
			            emit ('if_icmpge END_WHILE_' + str(y), -2)     
			        if (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.LE:
			            emit ('if_icmpgt END_WHILE_' + str(y), -2)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_breakContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(JacParser.BREAK, 0); }
		public St_breakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_break; }
	}

	public final St_breakContext st_break() throws RecognitionException {
		St_breakContext _localctx = new St_breakContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_st_break);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(BREAK);
			if 1:
			        global y
			        global Loop
			        if Loop == True: 
			            print('goto END_WHILE_' + str(y-1))
			        else:
			            sys.stderr.write('ERROR: Break without while')
			            sys.exit(1)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_continueContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(JacParser.CONTINUE, 0); }
		public St_continueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_continue; }
	}

	public final St_continueContext st_continue() throws RecognitionException {
		St_continueContext _localctx = new St_continueContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_st_continue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(CONTINUE);
			if 1:
			        global y
			        global Loop
			        if Loop == True: 
			            print('goto BEGIN_WHILE_' + str(y-1))
			        else:
			            sys.stderr.write('ERROR: Continue without while')
			            sys.exit(1)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public Token NAME;
		public ParametersContext p;
		public Token ft;
		public StatementContext st;
		public TerminalNode DEF() { return getToken(JacParser.DEF, 0); }
		public List<TerminalNode> NAME() { return getTokens(JacParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(JacParser.NAME, i);
		}
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public TerminalNode COLON() { return getToken(JacParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(JacParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(JacParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(DEF);
			setState(135);
			((FunctionContext)_localctx).NAME = match(NAME);
			setState(136);
			match(OP_PAR);
			{
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(137);
				((FunctionContext)_localctx).p = parameters();
				}
			}

			}
			setState(140);
			match(CL_PAR);
			setState(141);
			match(COLON);
			{
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(142);
				((FunctionContext)_localctx).ft = match(NAME);
				}
			}

			}
			setState(145);
			match(INDENT);
			if 1:
			    if (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) not in function_table:
			        parameters = (((FunctionContext)_localctx).p!=null?_input.getText(((FunctionContext)_localctx).p.start,((FunctionContext)_localctx).p.stop):null).split(',') if (((FunctionContext)_localctx).p!=null?_input.getText(((FunctionContext)_localctx).p.start,((FunctionContext)_localctx).p.stop):null) else []
			        if len(parameters) == len(set(parameters)):
			            function_table.append((((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null))
			            function_parameters.append(len(parameters))
			            function_return.append(True if (((FunctionContext)_localctx).ft!=null?((FunctionContext)_localctx).ft.getText():null) == 'int' else False)
			            print('.method public static '+(((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null)+'('+('I' * len(parameters))+')'+('I' if (((FunctionContext)_localctx).ft!=null?((FunctionContext)_localctx).ft.getText():null) else 'V'))

			            for p in parameters:
			                if p not in symbol_table:
			                    symbol_table.append(p)
			                    type_table.append('i')
			                    used_vars.append(False)
			        else:
			            sys.stderr.write('ERROR: Parameter(s) must be unique: ' + str(parameters))
			            sys.exit(1)
			    else:
			        sys.stderr.write('ERROR: Function already defined: ' + (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) )
			        sys.exit(1)
			  

			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << PRINT) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << RETURN) | (1L << NAME) | (1L << NL))) != 0)) {
				{
				{
				setState(147);
				((FunctionContext)_localctx).st = statement();
				}
				}
				setState(152);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(153);
			match(DEDENT);
			if 1:

			    print('    return')
			    print('.limit stack ' + str(stack_max))
			    print('.limit locals ' + str(len(symbol_table)))
			    print(';symbol_table ' + str(symbol_table))
			    print('.end method')
			    resetFunctionMetrics()

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParametersContext extends ParserRuleContext {
		public List<TerminalNode> NAME() { return getTokens(JacParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(JacParser.NAME, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(JacParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JacParser.COMMA, i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(NAME);
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(157);
				match(COMMA);
				setState(158);
				match(NAME);
				}
				}
				setState(163);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_callContext extends ParserRuleContext {
		public Token NAME;
		public ArgumentsContext arg;
		public TerminalNode NAME() { return getToken(JacParser.NAME, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public St_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_call; }
	}

	public final St_callContext st_call() throws RecognitionException {
		St_callContext _localctx = new St_callContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_st_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			((St_callContext)_localctx).NAME = match(NAME);
			setState(165);
			match(OP_PAR);
			{
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READINT) | (1L << READSTR) | (1L << OP_PAR) | (1L << NAME) | (1L << NUMBER) | (1L << STRING))) != 0)) {
				{
				setState(166);
				((St_callContext)_localctx).arg = arguments();
				}
			}

			}
			setState(169);
			match(CL_PAR);
			if 1:

			    if (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null) in function_table:
			        index = function_table.index((((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null))
			        arguments = (((St_callContext)_localctx).arg!=null?_input.getText(((St_callContext)_localctx).arg.start,((St_callContext)_localctx).arg.stop):null) if (((St_callContext)_localctx).arg!=null?_input.getText(((St_callContext)_localctx).arg.start,((St_callContext)_localctx).arg.stop):null) else ""
			        if not function_return[index]:
			            if '"' not in arguments:
			                real_arguments = arguments.split(',') if len(arguments) > 0 else []
			                if len(real_arguments) == function_parameters[index]:
			                    func_I = "I" * function_parameters[index]
			                    emit('invokestatic Test/' + (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null) + '(' + func_I + ')V', 0)
			                else:
			                    sys.stderr.write('ERROR: Wrong number of arguments: '+ (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null) + '\n')
			            else:
			                sys.stderr.write('ERROR: all arguments must be integer: ' + (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null) + '\n')
			        else:
			           sys.stderr.write('ERROR: Function missing return statement: ' + (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null) + '\n')
			    else:
			        sys.stderr.write('ERROR: Function not defined: ' + (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null) + '\n')

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentsContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(JacParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JacParser.COMMA, i);
		}
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			expression();
			setState(177);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(173);
				match(COMMA);
				setState(174);
				expression();
				}
				}
				setState(179);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_returnContext extends ParserRuleContext {
		public ExpressionContext ex;
		public TerminalNode RETURN() { return getToken(JacParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public St_returnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_return; }
	}

	public final St_returnContext st_return() throws RecognitionException {
		St_returnContext _localctx = new St_returnContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_st_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			match(RETURN);
			setState(181);
			((St_returnContext)_localctx).ex = expression();
			if 1:
			    if ((St_returnContext)_localctx).ex.type == 'i':
			        emit('ireturn', 0)
			    else:
			        sys.stderr.write('ERROR: Return type must be integer: '+ (((St_returnContext)_localctx).ex!=null?_input.getText(((St_returnContext)_localctx).ex.start,((St_returnContext)_localctx).ex.stop):null) + ' is ' + '"' + ((St_returnContext)_localctx).ex.type +'"' + '\n')

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public  type;
		public TermContext t1;
		public Token op;
		public TermContext t2;
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(JacParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(JacParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(JacParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(JacParser.MINUS, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			((ExpressionContext)_localctx).t1 = term();
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(185);
				((ExpressionContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
					((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(186);
				((ExpressionContext)_localctx).t2 = term();
				if 1:
				        if ((ExpressionContext)_localctx).t1.type == 's' or ((ExpressionContext)_localctx).t2.type == 's':
				            sys.stderr.write('ERROR: Operators cannot use string type: ' + (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getText():null) + '\n')
				        if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == JacParser.PLUS:
				            emit('    iadd', -1)
				        if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == JacParser.MINUS:
				            emit('    isub', -1)
				        
				    
				}
				}
				setState(193);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			if 1:
			        _localctx.type = ((ExpressionContext)_localctx).t1.type
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public  type;
		public FactorContext f;
		public FactorContext factor;
		public Token op;
		public FactorContext f1;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> TIMES() { return getTokens(JacParser.TIMES); }
		public TerminalNode TIMES(int i) {
			return getToken(JacParser.TIMES, i);
		}
		public List<TerminalNode> OVER() { return getTokens(JacParser.OVER); }
		public TerminalNode OVER(int i) {
			return getToken(JacParser.OVER, i);
		}
		public List<TerminalNode> REM() { return getTokens(JacParser.REM); }
		public TerminalNode REM(int i) {
			return getToken(JacParser.REM, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			((TermContext)_localctx).f = ((TermContext)_localctx).factor = factor();
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) {
				{
				{
				setState(197);
				((TermContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) ) {
					((TermContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(198);
				((TermContext)_localctx).f1 = ((TermContext)_localctx).factor = factor();
				if 1:
				        if ((TermContext)_localctx).f.type == 's' or ((TermContext)_localctx).f1.type == 's':
				            sys.stderr.write('ERROR: Operator cannot use string type: ' + (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getText():null) + '\n')
				        if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.TIMES: 
				            emit('imul',     -1)
				        if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.OVER:  
				            emit('idiv',     -1)
				        if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.REM:   
				            emit('irem',     -1)
				    
				}
				}
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			if 1:
			        _localctx.type = ((TermContext)_localctx).factor.type
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public  type;
		public Token NUMBER;
		public Token STRING;
		public ExpressionContext e;
		public Token NAME;
		public ArgumentsContext arg;
		public TerminalNode NUMBER() { return getToken(JacParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(JacParser.STRING, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NAME() { return getToken(JacParser.NAME, 0); }
		public TerminalNode READINT() { return getToken(JacParser.READINT, 0); }
		public TerminalNode READSTR() { return getToken(JacParser.READSTR, 0); }
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_factor);
		int _la;
		try {
			setState(234);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(208);
				((FactorContext)_localctx).NUMBER = match(NUMBER);
				if 1:
				        emit('ldc ' + (((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null), +1)
				        _localctx.type = 'i'

				    
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(210);
				((FactorContext)_localctx).STRING = match(STRING);
				if 1:
				        emit('ldc ' + (((FactorContext)_localctx).STRING!=null?((FactorContext)_localctx).STRING.getText():null), +1)
				        _localctx.type = 's'
				    
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(212);
				match(OP_PAR);
				setState(213);
				((FactorContext)_localctx).e = expression();
				setState(214);
				match(CL_PAR);
				if 1:
				        _localctx.type = ((FactorContext)_localctx).e.type
				    
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(217);
				((FactorContext)_localctx).NAME = match(NAME);
				if 1:
				        try:
				            index = str(symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null)))
				        except ValueError:
				            sys.stderr.write('ERROR: Variable ' + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + ' not defined in line ' + str((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getLine():0))  )
				            sys.exit(1)
				        used_vars[int(index)] = True    
				        type  = type_table[int(index)]
				        if(type == 'i'):
				            emit('iload ' + str(index), +1)
				        elif(type == 's'):
				            emit('aload ' + str(index), +1)
				        _localctx.type = type

				    
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(219);
				match(READINT);
				setState(220);
				match(OP_PAR);
				setState(221);
				match(CL_PAR);
				if 1:
				        #geração de código de leitura de inteiro
				        emit('    invokestatic Runtime/readInt()I', +1)
				        _localctx.type = 'i'
				    
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(223);
				match(READSTR);
				setState(224);
				match(OP_PAR);
				setState(225);
				match(CL_PAR);
				if 1:
				        #geração de código de leitura de string
				        emit('    invokestatic Runtime/readString()Ljava/lang/String;', +1)
				        _localctx.type = 's'
				    
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(227);
				((FactorContext)_localctx).NAME = match(NAME);
				setState(228);
				match(OP_PAR);
				{
				setState(230);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READINT) | (1L << READSTR) | (1L << OP_PAR) | (1L << NAME) | (1L << NUMBER) | (1L << STRING))) != 0)) {
					{
					setState(229);
					((FactorContext)_localctx).arg = arguments();
					}
				}

				}
				setState(232);
				match(CL_PAR);
				if 1:
				        if (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) in function_table:
				            index = function_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))
				            arguments = (((FactorContext)_localctx).arg!=null?_input.getText(((FactorContext)_localctx).arg.start,((FactorContext)_localctx).arg.stop):null) if (((FactorContext)_localctx).arg!=null?_input.getText(((FactorContext)_localctx).arg.start,((FactorContext)_localctx).arg.stop):null) else ""
				            if function_return[index]:
				                if '"' not in arguments:
				                    real_arguments = arguments.split(',') if len(arguments) > 0 else []
				                    if len(real_arguments) == function_parameters[index]:

				                        func_I = "I" * function_parameters[index]
				                        emit('invokestatic Test/' + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + '(' + func_I + ')I', 0)
				                        _localctx.type = 'i'
				                    else:
				                        sys.stderr.write('ERROR: Wrong number of arguments: '+ str(real_arguments) + ' ' + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + '\n' )
				                else:
				                    sys.stderr.write('ERROR: All arguments must be integer: ' + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + '\n')
				            else:
				                sys.stderr.write('ERROR: Function Void must not return: ' + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + '\n')
				        else:
				            sys.stderr.write('ERROR: Function not defined: ' + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + '\n')
				    
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%\u00ef\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\3\2\3\2\7\2+\n\2\f\2\16\2.\13\2\3\2\3\2\3\3\3\3\6"+
		"\3\64\n\3\r\3\16\3\65\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4"+
		"C\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5O\n\5\f\5\16\5R\13\5"+
		"\5\5T\n\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\6\7"+
		"d\n\7\r\7\16\7e\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\6\tw\n\t\r\t\16\tx\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3"+
		"\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u008d\n\r\3\r\3\r\3\r\5\r\u0092\n"+
		"\r\3\r\3\r\3\r\7\r\u0097\n\r\f\r\16\r\u009a\13\r\3\r\3\r\3\r\3\16\3\16"+
		"\3\16\7\16\u00a2\n\16\f\16\16\16\u00a5\13\16\3\17\3\17\3\17\5\17\u00aa"+
		"\n\17\3\17\3\17\3\17\3\20\3\20\3\20\7\20\u00b2\n\20\f\20\16\20\u00b5\13"+
		"\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\7\22\u00c0\n\22\f\22"+
		"\16\22\u00c3\13\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\7\23\u00cc\n\23"+
		"\f\23\16\23\u00cf\13\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\24\5\24\u00e9\n\24\3\24\3\24\5\24\u00ed\n\24\3\24\2\2\25\2\4\6\b\n\f"+
		"\16\20\22\24\26\30\32\34\36 \"$&\2\5\3\2\21\26\3\2\f\r\3\2\16\20\2\u00f8"+
		"\2(\3\2\2\2\4\61\3\2\2\2\6B\3\2\2\2\bD\3\2\2\2\nX\3\2\2\2\f]\3\2\2\2\16"+
		"j\3\2\2\2\20o\3\2\2\2\22}\3\2\2\2\24\u0082\3\2\2\2\26\u0085\3\2\2\2\30"+
		"\u0088\3\2\2\2\32\u009e\3\2\2\2\34\u00a6\3\2\2\2\36\u00ae\3\2\2\2 \u00b6"+
		"\3\2\2\2\"\u00ba\3\2\2\2$\u00c6\3\2\2\2&\u00ec\3\2\2\2(,\b\2\1\2)+\5\30"+
		"\r\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\5"+
		"\4\3\2\60\3\3\2\2\2\61\63\b\3\1\2\62\64\5\6\4\2\63\62\3\2\2\2\64\65\3"+
		"\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\678\b\3\1\28\5\3\2\2"+
		"\29C\7\"\2\2:C\5\b\5\2;C\5\n\6\2<C\5\f\7\2=C\5\20\t\2>C\5\24\13\2?C\5"+
		"\26\f\2@C\5\34\17\2AC\5 \21\2B9\3\2\2\2B:\3\2\2\2B;\3\2\2\2B<\3\2\2\2"+
		"B=\3\2\2\2B>\3\2\2\2B?\3\2\2\2B@\3\2\2\2BA\3\2\2\2C\7\3\2\2\2DE\7\4\2"+
		"\2ES\7\27\2\2FG\b\5\1\2GH\5\"\22\2HP\b\5\1\2IJ\7\35\2\2JK\b\5\1\2KL\5"+
		"\"\22\2LM\b\5\1\2MO\3\2\2\2NI\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QT"+
		"\3\2\2\2RP\3\2\2\2SF\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\30\2\2VW\b\5\1\2"+
		"W\t\3\2\2\2XY\7\36\2\2YZ\7\34\2\2Z[\5\"\22\2[\\\b\6\1\2\\\13\3\2\2\2]"+
		"^\7\3\2\2^_\5\16\b\2_`\b\7\1\2`a\7\33\2\2ac\7$\2\2bd\5\6\4\2cb\3\2\2\2"+
		"de\3\2\2\2ec\3\2\2\2ef\3\2\2\2fg\3\2\2\2gh\b\7\1\2hi\7%\2\2i\r\3\2\2\2"+
		"jk\5\"\22\2kl\t\2\2\2lm\5\"\22\2mn\b\b\1\2n\17\3\2\2\2op\7\7\2\2pq\b\t"+
		"\1\2qr\5\22\n\2rs\b\t\1\2st\7\33\2\2tv\7$\2\2uw\5\6\4\2vu\3\2\2\2wx\3"+
		"\2\2\2xv\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\b\t\1\2{|\7%\2\2|\21\3\2\2\2}~"+
		"\5\"\22\2~\177\t\2\2\2\177\u0080\5\"\22\2\u0080\u0081\b\n\1\2\u0081\23"+
		"\3\2\2\2\u0082\u0083\7\b\2\2\u0083\u0084\b\13\1\2\u0084\25\3\2\2\2\u0085"+
		"\u0086\7\t\2\2\u0086\u0087\b\f\1\2\u0087\27\3\2\2\2\u0088\u0089\7\n\2"+
		"\2\u0089\u008a\7\36\2\2\u008a\u008c\7\27\2\2\u008b\u008d\5\32\16\2\u008c"+
		"\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\7\30"+
		"\2\2\u008f\u0091\7\33\2\2\u0090\u0092\7\36\2\2\u0091\u0090\3\2\2\2\u0091"+
		"\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\7$\2\2\u0094\u0098\b\r"+
		"\1\2\u0095\u0097\5\6\4\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098"+
		"\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u0098\3\2"+
		"\2\2\u009b\u009c\7%\2\2\u009c\u009d\b\r\1\2\u009d\31\3\2\2\2\u009e\u00a3"+
		"\7\36\2\2\u009f\u00a0\7\35\2\2\u00a0\u00a2\7\36\2\2\u00a1\u009f\3\2\2"+
		"\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\33"+
		"\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\7\36\2\2\u00a7\u00a9\7\27\2\2"+
		"\u00a8\u00aa\5\36\20\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab"+
		"\3\2\2\2\u00ab\u00ac\7\30\2\2\u00ac\u00ad\b\17\1\2\u00ad\35\3\2\2\2\u00ae"+
		"\u00b3\5\"\22\2\u00af\u00b0\7\35\2\2\u00b0\u00b2\5\"\22\2\u00b1\u00af"+
		"\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4"+
		"\37\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\7\13\2\2\u00b7\u00b8\5\"\22"+
		"\2\u00b8\u00b9\b\21\1\2\u00b9!\3\2\2\2\u00ba\u00c1\5$\23\2\u00bb\u00bc"+
		"\t\3\2\2\u00bc\u00bd\5$\23\2\u00bd\u00be\b\22\1\2\u00be\u00c0\3\2\2\2"+
		"\u00bf\u00bb\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2"+
		"\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\b\22\1\2"+
		"\u00c5#\3\2\2\2\u00c6\u00cd\5&\24\2\u00c7\u00c8\t\4\2\2\u00c8\u00c9\5"+
		"&\24\2\u00c9\u00ca\b\23\1\2\u00ca\u00cc\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cc"+
		"\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2"+
		"\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\b\23\1\2\u00d1%\3\2\2\2\u00d2\u00d3"+
		"\7\37\2\2\u00d3\u00ed\b\24\1\2\u00d4\u00d5\7 \2\2\u00d5\u00ed\b\24\1\2"+
		"\u00d6\u00d7\7\27\2\2\u00d7\u00d8\5\"\22\2\u00d8\u00d9\7\30\2\2\u00d9"+
		"\u00da\b\24\1\2\u00da\u00ed\3\2\2\2\u00db\u00dc\7\36\2\2\u00dc\u00ed\b"+
		"\24\1\2\u00dd\u00de\7\5\2\2\u00de\u00df\7\27\2\2\u00df\u00e0\7\30\2\2"+
		"\u00e0\u00ed\b\24\1\2\u00e1\u00e2\7\6\2\2\u00e2\u00e3\7\27\2\2\u00e3\u00e4"+
		"\7\30\2\2\u00e4\u00ed\b\24\1\2\u00e5\u00e6\7\36\2\2\u00e6\u00e8\7\27\2"+
		"\2\u00e7\u00e9\5\36\20\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9"+
		"\u00ea\3\2\2\2\u00ea\u00eb\7\30\2\2\u00eb\u00ed\b\24\1\2\u00ec\u00d2\3"+
		"\2\2\2\u00ec\u00d4\3\2\2\2\u00ec\u00d6\3\2\2\2\u00ec\u00db\3\2\2\2\u00ec"+
		"\u00dd\3\2\2\2\u00ec\u00e1\3\2\2\2\u00ec\u00e5\3\2\2\2\u00ed\'\3\2\2\2"+
		"\23,\65BPSex\u008c\u0091\u0098\u00a3\u00a9\u00b3\u00c1\u00cd\u00e8\u00ec";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}