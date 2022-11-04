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
		NUMBER=9, SPACE=10, COOMENT=11;
	public static final int
		RULE_program = 0, RULE_main = 1, RULE_statement = 2, RULE_st_print = 3, 
		RULE_expression = 4, RULE_term = 5, RULE_factor = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main", "statement", "st_print", "expression", "term", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'print'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PRINT", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", "CL_PAR", 
			"NUMBER", "SPACE", "COOMENT"
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
			    
			setState(15);
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
			    
			setState(19); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(18);
				statement();
				}
				}
				setState(21); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==PRINT );
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
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			st_print();
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
			setState(27);
			match(PRINT);
			setState(28);
			match(OP_PAR);
			if 1:
			        print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
			    
			setState(30);
			expression();
			setState(31);
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
		enterRule(_localctx, 8, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			term();
			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(37);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(35);
					((ExpressionContext)_localctx).op = match(PLUS);
					}
					break;
				case MINUS:
					{
					setState(36);
					match(MINUS);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(39);
				term();
				if 1:
				        if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == JacParser.PLUS:
				            print('    iadd')
				        else:
				            print('    isub')    
				    
				}
				}
				setState(46);
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
		enterRule(_localctx, 10, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			factor();
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) {
				{
				{
				setState(51);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case TIMES:
					{
					setState(48);
					((TermContext)_localctx).op = match(TIMES);
					}
					break;
				case OVER:
					{
					setState(49);
					match(OVER);
					}
					break;
				case REM:
					{
					setState(50);
					match(REM);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(53);
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
				setState(60);
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
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_factor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			((FactorContext)_localctx).NUMBER = match(NUMBER);
			if 1:
			        print('    ldc ' + (((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null))
			        # symbol_table.append((((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null))
			    
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\rC\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\3\2\3\2\3\3\3\3\6\3\26"+
		"\n\3\r\3\16\3\27\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3"+
		"\6\5\6(\n\6\3\6\3\6\3\6\7\6-\n\6\f\6\16\6\60\13\6\3\7\3\7\3\7\3\7\5\7"+
		"\66\n\7\3\7\3\7\3\7\7\7;\n\7\f\7\16\7>\13\7\3\b\3\b\3\b\3\b\2\2\t\2\4"+
		"\6\b\n\f\16\2\2\2A\2\20\3\2\2\2\4\23\3\2\2\2\6\33\3\2\2\2\b\35\3\2\2\2"+
		"\n$\3\2\2\2\f\61\3\2\2\2\16?\3\2\2\2\20\21\b\2\1\2\21\22\5\4\3\2\22\3"+
		"\3\2\2\2\23\25\b\3\1\2\24\26\5\6\4\2\25\24\3\2\2\2\26\27\3\2\2\2\27\25"+
		"\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32\b\3\1\2\32\5\3\2\2\2\33\34"+
		"\5\b\5\2\34\7\3\2\2\2\35\36\7\3\2\2\36\37\7\t\2\2\37 \b\5\1\2 !\5\n\6"+
		"\2!\"\7\n\2\2\"#\b\5\1\2#\t\3\2\2\2$.\5\f\7\2%(\7\4\2\2&(\7\5\2\2\'%\3"+
		"\2\2\2\'&\3\2\2\2()\3\2\2\2)*\5\f\7\2*+\b\6\1\2+-\3\2\2\2,\'\3\2\2\2-"+
		"\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\13\3\2\2\2\60.\3\2\2\2\61<\5\16\b\2\62"+
		"\66\7\6\2\2\63\66\7\7\2\2\64\66\7\b\2\2\65\62\3\2\2\2\65\63\3\2\2\2\65"+
		"\64\3\2\2\2\66\67\3\2\2\2\678\5\16\b\289\b\7\1\29;\3\2\2\2:\65\3\2\2\2"+
		";>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\r\3\2\2\2><\3\2\2\2?@\7\13\2\2@A\b\b\1"+
		"\2A\17\3\2\2\2\7\27\'.\65<";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}