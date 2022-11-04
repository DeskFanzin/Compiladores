// Generated from c:\Users\gabri\OneDrive\Área de Trabalho\codes\vscode\compiladores\JAC\Jac.g4 by ANTLR 4.9.2

# symbol_table = []

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
		PRINT=1, PLUS=2, MINUS=3, TIMES=4, OVER=5, REM=6, OP_PAR=7, CL_PAR=8, 
		ATTRIB=9, NAME=10, NUMBER=11, SPACE=12, COOMENT=13;
	public static final int
		RULE_program = 0, RULE_main = 1, RULE_statement = 2, RULE_st_print = 3, 
		RULE_st_attrib = 4, RULE_expression = 5, RULE_term = 6, RULE_factor = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main", "statement", "st_print", "st_attrib", "expression", 
			"term", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'print'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PRINT", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", "CL_PAR", 
			"ATTRIB", "NAME", "NUMBER", "SPACE", "COOMENT"
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
			    
			setState(17);
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
			    
			setState(21); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(20);
				statement();
				}
				}
				setState(23); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==PRINT || _la==NAME );
			if 1:
			        print('    return')
			        print('.limit stack 10')
			        print('.end method')
			        # print('\n; symbol_table:', symbol_table)
			    
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
		public St_printContext st_print() {
			return getRuleContext(St_printContext.class,0);
		}
		public St_attribContext st_attrib() {
			return getRuleContext(St_attribContext.class,0);
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
			setState(29);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
				enterOuterAlt(_localctx, 1);
				{
				setState(27);
				st_print();
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(28);
				st_attrib();
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
		public TerminalNode PRINT() { return getToken(JacParser.PRINT, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public St_printContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_print; }
	}

	public final St_printContext st_print() throws RecognitionException {
		St_printContext _localctx = new St_printContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_st_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			match(PRINT);
			setState(32);
			match(OP_PAR);
			if 1:
			        print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
			    
			setState(34);
			expression();
			setState(35);
			match(CL_PAR);
			if 1:
			        print('    invokevirtual java/io/PrintStream/println(I)V\n')
			    
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
			setState(38);
			match(NAME);
			setState(39);
			match(ATTRIB);
			setState(40);
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

	public static class ExpressionContext extends ParserRuleContext {
		public Token op;
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> MINUS() { return getTokens(JacParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(JacParser.MINUS, i);
		}
		public List<TerminalNode> PLUS() { return getTokens(JacParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(JacParser.PLUS, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			term();
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(46);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(44);
					((ExpressionContext)_localctx).op = match(PLUS);
					}
					break;
				case MINUS:
					{
					setState(45);
					match(MINUS);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(48);
				term();
				if 1:
				        if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == JacParser.PLUS:
				            print('    iadd')
				        else:
				            print('    isub')    
				    
				}
				}
				setState(55);
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

	public static class TermContext extends ParserRuleContext {
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
		enterRule(_localctx, 12, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			factor();
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) {
				{
				{
				setState(60);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case TIMES:
					{
					setState(57);
					((TermContext)_localctx).op = match(TIMES);
					}
					break;
				case OVER:
					{
					setState(58);
					match(OVER);
					}
					break;
				case REM:
					{
					setState(59);
					match(REM);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(62);
				factor();
				if 1:
				        if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.TIMES:
				            print('    imul')
				        elif (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.OVER:
				            print('    idiv')
				        else:
				            print('    irem')
				    
				}
				}
				setState(69);
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

	public static class FactorContext extends ParserRuleContext {
		public Token NUMBER;
		public TerminalNode NUMBER() { return getToken(JacParser.NUMBER, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public TerminalNode NAME() { return getToken(JacParser.NAME, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_factor);
		try {
			setState(78);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(70);
				((FactorContext)_localctx).NUMBER = match(NUMBER);
				if 1:
				        print('    ldc ' + (((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null))
				        # symbol_table.append((((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null))
				    
				}
				break;
			case OP_PAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				match(OP_PAR);
				setState(73);
				expression();
				setState(74);
				match(CL_PAR);
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 3);
				{
				setState(76);
				match(NAME);
				if 1:
				        print('    iload 0')
				    
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17S\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3"+
		"\6\3\30\n\3\r\3\16\3\31\3\3\3\3\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\61\n\7\3\7\3\7\3\7\7\7\66\n"+
		"\7\f\7\16\79\13\7\3\b\3\b\3\b\3\b\5\b?\n\b\3\b\3\b\3\b\7\bD\n\b\f\b\16"+
		"\bG\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tQ\n\t\3\t\2\2\n\2\4\6\b\n"+
		"\f\16\20\2\2\2S\2\22\3\2\2\2\4\25\3\2\2\2\6\37\3\2\2\2\b!\3\2\2\2\n(\3"+
		"\2\2\2\f-\3\2\2\2\16:\3\2\2\2\20P\3\2\2\2\22\23\b\2\1\2\23\24\5\4\3\2"+
		"\24\3\3\2\2\2\25\27\b\3\1\2\26\30\5\6\4\2\27\26\3\2\2\2\30\31\3\2\2\2"+
		"\31\27\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33\34\b\3\1\2\34\5\3\2\2\2"+
		"\35 \5\b\5\2\36 \5\n\6\2\37\35\3\2\2\2\37\36\3\2\2\2 \7\3\2\2\2!\"\7\3"+
		"\2\2\"#\7\t\2\2#$\b\5\1\2$%\5\f\7\2%&\7\n\2\2&\'\b\5\1\2\'\t\3\2\2\2("+
		")\7\f\2\2)*\7\13\2\2*+\5\f\7\2+,\b\6\1\2,\13\3\2\2\2-\67\5\16\b\2.\61"+
		"\7\4\2\2/\61\7\5\2\2\60.\3\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\63\5\16"+
		"\b\2\63\64\b\7\1\2\64\66\3\2\2\2\65\60\3\2\2\2\669\3\2\2\2\67\65\3\2\2"+
		"\2\678\3\2\2\28\r\3\2\2\29\67\3\2\2\2:E\5\20\t\2;?\7\6\2\2<?\7\7\2\2="+
		"?\7\b\2\2>;\3\2\2\2><\3\2\2\2>=\3\2\2\2?@\3\2\2\2@A\5\20\t\2AB\b\b\1\2"+
		"BD\3\2\2\2C>\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\17\3\2\2\2GE\3\2\2"+
		"\2HI\7\r\2\2IQ\b\t\1\2JK\7\t\2\2KL\5\f\7\2LM\7\n\2\2MQ\3\2\2\2NO\7\f\2"+
		"\2OQ\b\t\1\2PH\3\2\2\2PJ\3\2\2\2PN\3\2\2\2Q\21\3\2\2\2\t\31\37\60\67>"+
		"EP";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}