// Generated from c:\Users\gabri\OneDrive\Área de Trabalho\codes\vscode\compiladores\JAC\Jac.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JacLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PRINT=1, PLUS=2, MINUS=3, TIMES=4, OVER=5, REM=6, OP_PAR=7, CL_PAR=8, 
		ATTRIB=9, NAME=10, NUMBER=11, SPACE=12, COOMENT=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PRINT", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", "CL_PAR", 
			"ATTRIB", "NAME", "NUMBER", "SPACE", "COOMENT"
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


	public JacLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Jac.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17M\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4"+
		"\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\65\n\13\r\13"+
		"\16\13\66\3\f\6\f:\n\f\r\f\16\f;\3\r\6\r?\n\r\r\r\16\r@\3\r\3\r\3\16\3"+
		"\16\7\16G\n\16\f\16\16\16J\13\16\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7"+
		"\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\4\5\2\13\f\17\17\"\"\3"+
		"\2\f\f\2P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2"+
		"\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2"+
		"\t\'\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2"+
		"\2\2\25\64\3\2\2\2\279\3\2\2\2\31>\3\2\2\2\33D\3\2\2\2\35\36\7r\2\2\36"+
		"\37\7t\2\2\37 \7k\2\2 !\7p\2\2!\"\7v\2\2\"\4\3\2\2\2#$\7-\2\2$\6\3\2\2"+
		"\2%&\7/\2\2&\b\3\2\2\2\'(\7,\2\2(\n\3\2\2\2)*\7\61\2\2*\f\3\2\2\2+,\7"+
		"\'\2\2,\16\3\2\2\2-.\7*\2\2.\20\3\2\2\2/\60\7+\2\2\60\22\3\2\2\2\61\62"+
		"\7?\2\2\62\24\3\2\2\2\63\65\4c|\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3"+
		"\2\2\2\66\67\3\2\2\2\67\26\3\2\2\28:\4\62;\298\3\2\2\2:;\3\2\2\2;9\3\2"+
		"\2\2;<\3\2\2\2<\30\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3"+
		"\2\2\2AB\3\2\2\2BC\b\r\2\2C\32\3\2\2\2DH\7%\2\2EG\n\3\2\2FE\3\2\2\2GJ"+
		"\3\2\2\2HF\3\2\2\2HI\3\2\2\2IK\3\2\2\2JH\3\2\2\2KL\b\16\2\2L\34\3\2\2"+
		"\2\7\2\66;@H\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}