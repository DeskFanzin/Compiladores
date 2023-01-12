// Generated from c:\Users\gabri\OneDrive\Área de Trabalho\Tudo\codes\jac\JAC\Jac.g4 by ANTLR 4.9.2

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
		IF=1, PRINT=2, READINT=3, READSTR=4, WHILE=5, BREAK=6, CONTINUE=7, PLUS=8, 
		MINUS=9, TIMES=10, OVER=11, REM=12, EQ=13, NE=14, GT=15, GE=16, LT=17, 
		LE=18, OP_PAR=19, CL_PAR=20, OP_CUR=21, CL_CUR=22, ATTRIB=23, COMMA=24, 
		NAME=25, NUMBER=26, STRING=27, COMMENT=28, NL=29, SPACE=30, INDENT=31, 
		DEDENT=32;
	public static final int
		RULE_program = 0, RULE_main = 1, RULE_statement = 2, RULE_st_print = 3, 
		RULE_st_attrib = 4, RULE_st_if = 5, RULE_comparison_if = 6, RULE_st_while = 7, 
		RULE_comparison_while = 8, RULE_st_break = 9, RULE_st_continue = 10, RULE_expression = 11, 
		RULE_term = 12, RULE_factor = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main", "statement", "st_print", "st_attrib", "st_if", "comparison_if", 
			"st_while", "comparison_while", "st_break", "st_continue", "expression", 
			"term", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'print'", "'readint'", "'readstr'", "'while'", "'break'", 
			"'continue'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>'", 
			"'>='", "'<'", "'<='", "'('", "')'", "'{'", "'}'", "'='", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "PRINT", "READINT", "READSTR", "WHILE", "BREAK", "CONTINUE", 
			"PLUS", "MINUS", "TIMES", "OVER", "REM", "EQ", "NE", "GT", "GE", "LT", 
			"LE", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", "COMMA", "NAME", 
			"NUMBER", "STRING", "COMMENT", "NL", "SPACE", "INDENT", "DEDENT"
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
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			if 1:
			        print('.source Test.src')
			        print('.class  public Test')
			        print('.super  java/lang/Object\n')
			        print('.method public <init>()V')
			        print('    aload_0')
			        print('    invokenonvirtual java/lang/Object/<init>()V')
			        print('    return')
			        print('.end method\n')
			    
			setState(29);
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
			        print('.method public static main([Ljava/lang/String;)V\n')
			    
			setState(33); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(32);
				statement();
				}
				}
				setState(35); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << PRINT) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME) | (1L << NL))) != 0) );
			if 1:
			        print('    return')
			        print('.limit stack 10')
			        print('.end method')
			        print('\n; symbol_table:', symbol_table)
			    
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
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(46);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NL:
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				match(NL);
				}
				break;
			case PRINT:
				enterOuterAlt(_localctx, 2);
				{
				setState(40);
				st_print();
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 3);
				{
				setState(41);
				st_attrib();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 4);
				{
				setState(42);
				st_if();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 5);
				{
				setState(43);
				st_while();
				}
				break;
			case BREAK:
				enterOuterAlt(_localctx, 6);
				{
				setState(44);
				st_break();
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 7);
				{
				setState(45);
				st_continue();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
			setState(48);
			match(PRINT);
			setState(49);
			match(OP_PAR);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READINT) | (1L << READSTR) | (1L << OP_PAR) | (1L << NAME) | (1L << NUMBER) | (1L << STRING))) != 0)) {
				{
				if 1:
				        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
				    
				setState(51);
				((St_printContext)_localctx).e1 = expression();
				if 1:
				        if ((St_printContext)_localctx).e1.type == 'i':
				            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
				        elif ((St_printContext)_localctx).e1.type == 's':
				            emit ('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
				        else:
				            print('*****HELP*****')
				    
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(53);
					match(COMMA);
					if 1:
					        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
					        
					setState(55);
					expression();
					if 1:
					        emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
					        
					}
					}
					setState(62);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(65);
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
			setState(68);
			match(NAME);
			setState(69);
			match(ATTRIB);
			setState(70);
			expression();
			if 1:
			        print('    istore 0')
			    
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
		public TerminalNode OP_CUR() { return getToken(JacParser.OP_CUR, 0); }
		public TerminalNode CL_CUR() { return getToken(JacParser.CL_CUR, 0); }
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
			setState(73);
			match(IF);
			setState(74);
			comparison_if();
			if 1:
			        global x 
			        local_x = x
			        x += 1
			    
			setState(76);
			match(OP_CUR);
			setState(78); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(77);
				statement();
				}
				}
				setState(80); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << PRINT) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME) | (1L << NL))) != 0) );
			if 1:
			        print('NOT_IF_' + str(local_x) + ':')
			    
			setState(83);
			match(CL_CUR);
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
		public Token op;
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
			setState(85);
			expression();
			setState(86);
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
			setState(87);
			expression();
			if 1:
			        if (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.EQ:
			            emit ('if_icmpne NOT_IF_' + str(x), -2)
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.NE:
			            emit ('if_icmpeq NOT_IF_' + str(x), -2)    
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.GT:
			            emit ('if_icmple NOT_IF_' + str(x), -2)      
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.GE:
			            emit ('if_icmplt NOT_IF_' + str(x), -2)   
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.LT:
			            emit ('if_icmpge NOT_IF_' + str(x), -2)     
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.LE:
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
		public TerminalNode OP_CUR() { return getToken(JacParser.OP_CUR, 0); }
		public TerminalNode CL_CUR() { return getToken(JacParser.CL_CUR, 0); }
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
			setState(90);
			match(WHILE);
			if 1:
			        global y 
			        local_y = y
			        print('BEGIN_WHILE_' + str(local_y) + ':')
			    
			setState(92);
			comparison_while();
			if 1:
			        y += 1
			    
			setState(94);
			match(OP_CUR);
			setState(96); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(95);
				statement();
				}
				}
				setState(98); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << PRINT) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME) | (1L << NL))) != 0) );
			if 1:
			        emit('goto BEGIN_WHILE_' + str(local_y), 0)
			        print('END_WHILE_' + str(local_y) + ':')
			    
			setState(101);
			match(CL_CUR);
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
		public Token op;
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
			setState(103);
			expression();
			setState(104);
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
			setState(105);
			expression();
			if 1:
			        if (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.EQ:
			            emit ('if_icmpne END_WHILE_' + str(x), -2)
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.NE:
			            emit ('if_icmpeq END_WHILE_' + str(x), -2)    
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.GT:
			            emit ('if_icmple END_WHILE_' + str(x), -2)      
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.GE:
			            emit ('if_icmplt END_WHILE_' + str(x), -2)   
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.LT:
			            emit ('if_icmpge END_WHILE_' + str(x), -2)     
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.LE:
			            emit ('if_icmpgt END_WHILE_' + str(x), -2)                 
			    
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
			setState(108);
			match(BREAK);
			if 1:
			        print('goto END_WHILE_' + str(y-1))
			    
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
			setState(111);
			match(CONTINUE);
			if 1:
			        print('goto BEGIN_WHILE_' + str(y-1))
			    
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
		enterRule(_localctx, 22, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			((ExpressionContext)_localctx).t1 = term();
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(115);
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
				setState(116);
				((ExpressionContext)_localctx).t2 = term();
				if 1:
				        if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == JacParser.PLUS:
				            print('    iadd')
				        else:
				            print('    isub')    
				    
				}
				}
				setState(123);
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
		public FactorContext factor;
		public Token op;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> OVER() { return getTokens(JacParser.OVER); }
		public TerminalNode OVER(int i) {
			return getToken(JacParser.OVER, i);
		}
		public List<TerminalNode> REM() { return getTokens(JacParser.REM); }
		public TerminalNode REM(int i) {
			return getToken(JacParser.REM, i);
		}
		public List<TerminalNode> TIMES() { return getTokens(JacParser.TIMES); }
		public TerminalNode TIMES(int i) {
			return getToken(JacParser.TIMES, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			((TermContext)_localctx).factor = factor();
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) {
				{
				{
				setState(130);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case TIMES:
					{
					setState(127);
					((TermContext)_localctx).op = match(TIMES);
					}
					break;
				case OVER:
					{
					setState(128);
					match(OVER);
					}
					break;
				case REM:
					{
					setState(129);
					match(REM);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(132);
				((TermContext)_localctx).factor = factor();
				if 1:
				        if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.TIMES:
				            print('    imul')
				        elif (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.OVER:
				            print('    idiv')
				        else:
				            print('    irem')
				    
				}
				}
				setState(139);
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
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_factor);
		try {
			setState(161);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				((FactorContext)_localctx).NUMBER = match(NUMBER);
				if 1:
				        emit('ldc ' + (((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null), +1)
				        _localctx.type = 'i'

				    
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(144);
				((FactorContext)_localctx).STRING = match(STRING);
				if 1:
				        emit('ldc ' + (((FactorContext)_localctx).STRING!=null?((FactorContext)_localctx).STRING.getText():null), +1)
				        _localctx.type = 's'
				    
				}
				break;
			case OP_PAR:
				enterOuterAlt(_localctx, 3);
				{
				setState(146);
				match(OP_PAR);
				setState(147);
				((FactorContext)_localctx).e = expression();
				setState(148);
				match(CL_PAR);
				if 1:
				        _localctx.type = e.type
				    
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 4);
				{
				setState(151);
				match(NAME);
				if 1:
				        print('    iload 0')
				        _localctx.type = 'i'
				    
				}
				break;
			case READINT:
				enterOuterAlt(_localctx, 5);
				{
				setState(153);
				match(READINT);
				setState(154);
				match(OP_PAR);
				setState(155);
				match(CL_PAR);
				if 1:
				        #geração de código de leitura de inteiro
				        emit('    invokestatic Runtime/readInt()I', +1)
				        _localctx.type = 'i'
				    
				}
				break;
			case READSTR:
				enterOuterAlt(_localctx, 6);
				{
				setState(157);
				match(READSTR);
				setState(158);
				match(OP_PAR);
				setState(159);
				match(CL_PAR);
				if 1:
				        #geração de código de leitura de string
				        emit('    invokestatic Runtime/readString()Ljava/lang/String;', +1)
				        _localctx.type = 's'
				    
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"\u00a6\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\6\3$\n\3\r"+
		"\3\16\3%\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\61\n\4\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5=\n\5\f\5\16\5@\13\5\5\5B\n\5\3\5\3\5\3"+
		"\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\6\7Q\n\7\r\7\16\7R\3\7\3\7"+
		"\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\6\tc\n\t\r\t\16\td\3"+
		"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r"+
		"\3\r\3\r\7\rz\n\r\f\r\16\r}\13\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u0085"+
		"\n\16\3\16\3\16\3\16\7\16\u008a\n\16\f\16\16\16\u008d\13\16\3\16\3\16"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\5\17\u00a4\n\17\3\17\2\2\20\2\4\6\b\n\f\16\20"+
		"\22\24\26\30\32\34\2\4\3\2\17\24\3\2\n\13\2\u00ab\2\36\3\2\2\2\4!\3\2"+
		"\2\2\6\60\3\2\2\2\b\62\3\2\2\2\nF\3\2\2\2\fK\3\2\2\2\16W\3\2\2\2\20\\"+
		"\3\2\2\2\22i\3\2\2\2\24n\3\2\2\2\26q\3\2\2\2\30t\3\2\2\2\32\u0080\3\2"+
		"\2\2\34\u00a3\3\2\2\2\36\37\b\2\1\2\37 \5\4\3\2 \3\3\2\2\2!#\b\3\1\2\""+
		"$\5\6\4\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\b\3\1"+
		"\2(\5\3\2\2\2)\61\7\37\2\2*\61\5\b\5\2+\61\5\n\6\2,\61\5\f\7\2-\61\5\20"+
		"\t\2.\61\5\24\13\2/\61\5\26\f\2\60)\3\2\2\2\60*\3\2\2\2\60+\3\2\2\2\60"+
		",\3\2\2\2\60-\3\2\2\2\60.\3\2\2\2\60/\3\2\2\2\61\7\3\2\2\2\62\63\7\4\2"+
		"\2\63A\7\25\2\2\64\65\b\5\1\2\65\66\5\30\r\2\66>\b\5\1\2\678\7\32\2\2"+
		"89\b\5\1\29:\5\30\r\2:;\b\5\1\2;=\3\2\2\2<\67\3\2\2\2=@\3\2\2\2><\3\2"+
		"\2\2>?\3\2\2\2?B\3\2\2\2@>\3\2\2\2A\64\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7"+
		"\26\2\2DE\b\5\1\2E\t\3\2\2\2FG\7\33\2\2GH\7\31\2\2HI\5\30\r\2IJ\b\6\1"+
		"\2J\13\3\2\2\2KL\7\3\2\2LM\5\16\b\2MN\b\7\1\2NP\7\27\2\2OQ\5\6\4\2PO\3"+
		"\2\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\b\7\1\2UV\7\30\2\2V\r"+
		"\3\2\2\2WX\5\30\r\2XY\t\2\2\2YZ\5\30\r\2Z[\b\b\1\2[\17\3\2\2\2\\]\7\7"+
		"\2\2]^\b\t\1\2^_\5\22\n\2_`\b\t\1\2`b\7\27\2\2ac\5\6\4\2ba\3\2\2\2cd\3"+
		"\2\2\2db\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\b\t\1\2gh\7\30\2\2h\21\3\2\2\2"+
		"ij\5\30\r\2jk\t\2\2\2kl\5\30\r\2lm\b\n\1\2m\23\3\2\2\2no\7\b\2\2op\b\13"+
		"\1\2p\25\3\2\2\2qr\7\t\2\2rs\b\f\1\2s\27\3\2\2\2t{\5\32\16\2uv\t\3\2\2"+
		"vw\5\32\16\2wx\b\r\1\2xz\3\2\2\2yu\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2"+
		"\2|~\3\2\2\2}{\3\2\2\2~\177\b\r\1\2\177\31\3\2\2\2\u0080\u008b\5\34\17"+
		"\2\u0081\u0085\7\f\2\2\u0082\u0085\7\r\2\2\u0083\u0085\7\16\2\2\u0084"+
		"\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2"+
		"\2\2\u0086\u0087\5\34\17\2\u0087\u0088\b\16\1\2\u0088\u008a\3\2\2\2\u0089"+
		"\u0084\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2"+
		"\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\b\16\1\2\u008f"+
		"\33\3\2\2\2\u0090\u0091\7\34\2\2\u0091\u00a4\b\17\1\2\u0092\u0093\7\35"+
		"\2\2\u0093\u00a4\b\17\1\2\u0094\u0095\7\25\2\2\u0095\u0096\5\30\r\2\u0096"+
		"\u0097\7\26\2\2\u0097\u0098\b\17\1\2\u0098\u00a4\3\2\2\2\u0099\u009a\7"+
		"\33\2\2\u009a\u00a4\b\17\1\2\u009b\u009c\7\5\2\2\u009c\u009d\7\25\2\2"+
		"\u009d\u009e\7\26\2\2\u009e\u00a4\b\17\1\2\u009f\u00a0\7\6\2\2\u00a0\u00a1"+
		"\7\25\2\2\u00a1\u00a2\7\26\2\2\u00a2\u00a4\b\17\1\2\u00a3\u0090\3\2\2"+
		"\2\u00a3\u0092\3\2\2\2\u00a3\u0094\3\2\2\2\u00a3\u0099\3\2\2\2\u00a3\u009b"+
		"\3\2\2\2\u00a3\u009f\3\2\2\2\u00a4\35\3\2\2\2\f%\60>ARd{\u0084\u008b\u00a3";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}