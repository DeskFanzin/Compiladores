// Generated from c:\Users\gabri\OneDrive\Área de Trabalho\Tudo\codes\jac\JAC\Jac.g4 by ANTLR 4.9.2

from antlr_denter.DenterHelper import DenterHelper
from JacParser import JacParser

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
		IF=1, PRINT=2, READINT=3, READSTR=4, WHILE=5, BREAK=6, CONTINUE=7, PLUS=8, 
		MINUS=9, TIMES=10, OVER=11, REM=12, EQ=13, NE=14, GT=15, GE=16, LT=17, 
		LE=18, OP_PAR=19, CL_PAR=20, OP_CUR=21, CL_CUR=22, ATTRIB=23, COMMA=24, 
		NAME=25, NUMBER=26, STRING=27, COMMENT=28, NL=29, SPACE=30;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"IF", "PRINT", "READINT", "READSTR", "WHILE", "BREAK", "CONTINUE", "PLUS", 
			"MINUS", "TIMES", "OVER", "REM", "EQ", "NE", "GT", "GE", "LT", "LE", 
			"OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", "COMMA", "NAME", "NUMBER", 
			"STRING", "COMMENT", "NL", "SPACE"
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
			"NUMBER", "STRING", "COMMENT", "NL", "SPACE"
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


	class JacDenter(DenterHelper):
	    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
	        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
	        self.lexer: JacLexer = lexer

	    def pull_token(self):
	        return super(JacLexer, self.lexer).nextToken()
	    denter = None

	    def nextToken(self):
	        if not self.denter:
	            self.denter = self.JacDenter(self, self.NL, JacParser.INDENT, JacParser.DEDENT, False)
	        return self.denter.next_token()


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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 \u00c0\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\3\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3"+
		"\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22"+
		"\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31"+
		"\3\31\3\32\6\32\u0095\n\32\r\32\16\32\u0096\3\33\6\33\u009a\n\33\r\33"+
		"\16\33\u009b\3\34\3\34\7\34\u00a0\n\34\f\34\16\34\u00a3\13\34\3\34\3\34"+
		"\3\35\3\35\7\35\u00a9\n\35\f\35\16\35\u00ac\13\35\3\35\3\35\3\36\5\36"+
		"\u00b1\n\36\3\36\3\36\7\36\u00b5\n\36\f\36\16\36\u00b8\13\36\3\37\6\37"+
		"\u00bb\n\37\r\37\16\37\u00bc\3\37\3\37\2\2 \3\3\5\4\7\5\t\6\13\7\r\b\17"+
		"\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+"+
		"\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= \3\2\5\3\2$$\3\2\f\f\4\2"+
		"\13\13\"\"\2\u00c6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\3?\3\2\2\2\5B\3\2\2\2\7H\3\2\2\2\tP"+
		"\3\2\2\2\13X\3\2\2\2\r^\3\2\2\2\17d\3\2\2\2\21m\3\2\2\2\23o\3\2\2\2\25"+
		"q\3\2\2\2\27s\3\2\2\2\31u\3\2\2\2\33w\3\2\2\2\35z\3\2\2\2\37}\3\2\2\2"+
		"!\177\3\2\2\2#\u0082\3\2\2\2%\u0084\3\2\2\2\'\u0087\3\2\2\2)\u0089\3\2"+
		"\2\2+\u008b\3\2\2\2-\u008d\3\2\2\2/\u008f\3\2\2\2\61\u0091\3\2\2\2\63"+
		"\u0094\3\2\2\2\65\u0099\3\2\2\2\67\u009d\3\2\2\29\u00a6\3\2\2\2;\u00b0"+
		"\3\2\2\2=\u00ba\3\2\2\2?@\7k\2\2@A\7h\2\2A\4\3\2\2\2BC\7r\2\2CD\7t\2\2"+
		"DE\7k\2\2EF\7p\2\2FG\7v\2\2G\6\3\2\2\2HI\7t\2\2IJ\7g\2\2JK\7c\2\2KL\7"+
		"f\2\2LM\7k\2\2MN\7p\2\2NO\7v\2\2O\b\3\2\2\2PQ\7t\2\2QR\7g\2\2RS\7c\2\2"+
		"ST\7f\2\2TU\7u\2\2UV\7v\2\2VW\7t\2\2W\n\3\2\2\2XY\7y\2\2YZ\7j\2\2Z[\7"+
		"k\2\2[\\\7n\2\2\\]\7g\2\2]\f\3\2\2\2^_\7d\2\2_`\7t\2\2`a\7g\2\2ab\7c\2"+
		"\2bc\7m\2\2c\16\3\2\2\2de\7e\2\2ef\7q\2\2fg\7p\2\2gh\7v\2\2hi\7k\2\2i"+
		"j\7p\2\2jk\7w\2\2kl\7g\2\2l\20\3\2\2\2mn\7-\2\2n\22\3\2\2\2op\7/\2\2p"+
		"\24\3\2\2\2qr\7,\2\2r\26\3\2\2\2st\7\61\2\2t\30\3\2\2\2uv\7\'\2\2v\32"+
		"\3\2\2\2wx\7?\2\2xy\7?\2\2y\34\3\2\2\2z{\7#\2\2{|\7?\2\2|\36\3\2\2\2}"+
		"~\7@\2\2~ \3\2\2\2\177\u0080\7@\2\2\u0080\u0081\7?\2\2\u0081\"\3\2\2\2"+
		"\u0082\u0083\7>\2\2\u0083$\3\2\2\2\u0084\u0085\7>\2\2\u0085\u0086\7?\2"+
		"\2\u0086&\3\2\2\2\u0087\u0088\7*\2\2\u0088(\3\2\2\2\u0089\u008a\7+\2\2"+
		"\u008a*\3\2\2\2\u008b\u008c\7}\2\2\u008c,\3\2\2\2\u008d\u008e\7\177\2"+
		"\2\u008e.\3\2\2\2\u008f\u0090\7?\2\2\u0090\60\3\2\2\2\u0091\u0092\7.\2"+
		"\2\u0092\62\3\2\2\2\u0093\u0095\4c|\2\u0094\u0093\3\2\2\2\u0095\u0096"+
		"\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\64\3\2\2\2\u0098"+
		"\u009a\4\62;\2\u0099\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u0099\3\2"+
		"\2\2\u009b\u009c\3\2\2\2\u009c\66\3\2\2\2\u009d\u00a1\7$\2\2\u009e\u00a0"+
		"\n\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1"+
		"\u00a2\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7$"+
		"\2\2\u00a58\3\2\2\2\u00a6\u00aa\7%\2\2\u00a7\u00a9\n\3\2\2\u00a8\u00a7"+
		"\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab"+
		"\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\b\35\2\2\u00ae:\3\2\2\2"+
		"\u00af\u00b1\7\17\2\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2"+
		"\3\2\2\2\u00b2\u00b6\7\f\2\2\u00b3\u00b5\7\"\2\2\u00b4\u00b3\3\2\2\2\u00b5"+
		"\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7<\3\2\2\2"+
		"\u00b8\u00b6\3\2\2\2\u00b9\u00bb\t\4\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc"+
		"\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be"+
		"\u00bf\b\37\2\2\u00bf>\3\2\2\2\n\2\u0096\u009b\u00a1\u00aa\u00b0\u00b6"+
		"\u00bc\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}