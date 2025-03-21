//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     ANTLR Version: 4.13.2
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

// Generated from gramatica.g4 by ANTLR 4.13.2

// Unreachable code detected
#pragma warning disable 0162
// The variable '...' is assigned but its value is never used
#pragma warning disable 0219
// Missing XML comment for publicly visible type or member '...'
#pragma warning disable 1591
// Ambiguous reference in cref attribute
#pragma warning disable 419

using System;
using System.IO;
using System.Text;
using System.Diagnostics;
using System.Collections.Generic;
using Antlr4.Runtime;
using Antlr4.Runtime.Atn;
using Antlr4.Runtime.Misc;
using Antlr4.Runtime.Tree;
using DFA = Antlr4.Runtime.Dfa.DFA;

[System.CodeDom.Compiler.GeneratedCode("ANTLR", "4.13.2")]
[System.CLSCompliant(false)]
public partial class gramaticaParser : Parser {
	protected static DFA[] decisionToDFA;
	protected static PredictionContextCache sharedContextCache = new PredictionContextCache();
	public const int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, NEWLINE=8, INT=9, 
		DECIMAL=10, CADENA=11;
	public const int
		RULE_start = 0, RULE_instrucciones = 1, RULE_instruccion = 2, RULE_print = 3, 
		RULE_expr = 4;
	public static readonly string[] ruleNames = {
		"start", "instrucciones", "instruccion", "print", "expr"
	};

	private static readonly string[] _LiteralNames = {
		null, "'fmt.println'", "'('", "')'", "'*'", "'/'", "'+'", "'-'"
	};
	private static readonly string[] _SymbolicNames = {
		null, null, null, null, null, null, null, null, "NEWLINE", "INT", "DECIMAL", 
		"CADENA"
	};
	public static readonly IVocabulary DefaultVocabulary = new Vocabulary(_LiteralNames, _SymbolicNames);

	[NotNull]
	public override IVocabulary Vocabulary
	{
		get
		{
			return DefaultVocabulary;
		}
	}

	public override string GrammarFileName { get { return "gramatica.g4"; } }

	public override string[] RuleNames { get { return ruleNames; } }

	public override int[] SerializedAtn { get { return _serializedATN; } }

	static gramaticaParser() {
		decisionToDFA = new DFA[_ATN.NumberOfDecisions];
		for (int i = 0; i < _ATN.NumberOfDecisions; i++) {
			decisionToDFA[i] = new DFA(_ATN.GetDecisionState(i), i);
		}
	}

		public gramaticaParser(ITokenStream input) : this(input, Console.Out, Console.Error) { }

		public gramaticaParser(ITokenStream input, TextWriter output, TextWriter errorOutput)
		: base(input, output, errorOutput)
	{
		Interpreter = new ParserATNSimulator(this, _ATN, decisionToDFA, sharedContextCache);
	}

	public partial class StartContext : ParserRuleContext {
		[System.Diagnostics.DebuggerNonUserCode] public InstruccionesContext instrucciones() {
			return GetRuleContext<InstruccionesContext>(0);
		}
		[System.Diagnostics.DebuggerNonUserCode] public ITerminalNode Eof() { return GetToken(gramaticaParser.Eof, 0); }
		public StartContext(ParserRuleContext parent, int invokingState)
			: base(parent, invokingState)
		{
		}
		public override int RuleIndex { get { return RULE_start; } }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterStart(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitStart(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitStart(this);
			else return visitor.VisitChildren(this);
		}
	}

	[RuleVersion(0)]
	public StartContext start() {
		StartContext _localctx = new StartContext(Context, State);
		EnterRule(_localctx, 0, RULE_start);
		try {
			EnterOuterAlt(_localctx, 1);
			{
			State = 10;
			instrucciones();
			State = 11;
			Match(Eof);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			ErrorHandler.ReportError(this, re);
			ErrorHandler.Recover(this, re);
		}
		finally {
			ExitRule();
		}
		return _localctx;
	}

	public partial class InstruccionesContext : ParserRuleContext {
		[System.Diagnostics.DebuggerNonUserCode] public InstruccionContext instruccion() {
			return GetRuleContext<InstruccionContext>(0);
		}
		[System.Diagnostics.DebuggerNonUserCode] public InstruccionesContext[] instrucciones() {
			return GetRuleContexts<InstruccionesContext>();
		}
		[System.Diagnostics.DebuggerNonUserCode] public InstruccionesContext instrucciones(int i) {
			return GetRuleContext<InstruccionesContext>(i);
		}
		public InstruccionesContext(ParserRuleContext parent, int invokingState)
			: base(parent, invokingState)
		{
		}
		public override int RuleIndex { get { return RULE_instrucciones; } }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterInstrucciones(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitInstrucciones(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitInstrucciones(this);
			else return visitor.VisitChildren(this);
		}
	}

	[RuleVersion(0)]
	public InstruccionesContext instrucciones() {
		InstruccionesContext _localctx = new InstruccionesContext(Context, State);
		EnterRule(_localctx, 2, RULE_instrucciones);
		try {
			int _alt;
			EnterOuterAlt(_localctx, 1);
			{
			State = 13;
			instruccion();
			State = 17;
			ErrorHandler.Sync(this);
			_alt = Interpreter.AdaptivePredict(TokenStream,0,Context);
			while ( _alt!=2 && _alt!=global::Antlr4.Runtime.Atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					State = 14;
					instrucciones();
					}
					} 
				}
				State = 19;
				ErrorHandler.Sync(this);
				_alt = Interpreter.AdaptivePredict(TokenStream,0,Context);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			ErrorHandler.ReportError(this, re);
			ErrorHandler.Recover(this, re);
		}
		finally {
			ExitRule();
		}
		return _localctx;
	}

	public partial class InstruccionContext : ParserRuleContext {
		[System.Diagnostics.DebuggerNonUserCode] public PrintContext print() {
			return GetRuleContext<PrintContext>(0);
		}
		public InstruccionContext(ParserRuleContext parent, int invokingState)
			: base(parent, invokingState)
		{
		}
		public override int RuleIndex { get { return RULE_instruccion; } }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterInstruccion(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitInstruccion(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitInstruccion(this);
			else return visitor.VisitChildren(this);
		}
	}

	[RuleVersion(0)]
	public InstruccionContext instruccion() {
		InstruccionContext _localctx = new InstruccionContext(Context, State);
		EnterRule(_localctx, 4, RULE_instruccion);
		try {
			EnterOuterAlt(_localctx, 1);
			{
			State = 20;
			print();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			ErrorHandler.ReportError(this, re);
			ErrorHandler.Recover(this, re);
		}
		finally {
			ExitRule();
		}
		return _localctx;
	}

	public partial class PrintContext : ParserRuleContext {
		[System.Diagnostics.DebuggerNonUserCode] public ExprContext expr() {
			return GetRuleContext<ExprContext>(0);
		}
		public PrintContext(ParserRuleContext parent, int invokingState)
			: base(parent, invokingState)
		{
		}
		public override int RuleIndex { get { return RULE_print; } }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterPrint(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitPrint(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitPrint(this);
			else return visitor.VisitChildren(this);
		}
	}

	[RuleVersion(0)]
	public PrintContext print() {
		PrintContext _localctx = new PrintContext(Context, State);
		EnterRule(_localctx, 6, RULE_print);
		try {
			EnterOuterAlt(_localctx, 1);
			{
			State = 22;
			Match(T__0);
			State = 23;
			Match(T__1);
			State = 24;
			expr(0);
			State = 25;
			Match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			ErrorHandler.ReportError(this, re);
			ErrorHandler.Recover(this, re);
		}
		finally {
			ExitRule();
		}
		return _localctx;
	}

	public partial class ExprContext : ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState)
			: base(parent, invokingState)
		{
		}
		public override int RuleIndex { get { return RULE_expr; } }
	 
		public ExprContext() { }
		public virtual void CopyFrom(ExprContext context) {
			base.CopyFrom(context);
		}
	}
	public partial class NumberContext : ExprContext {
		[System.Diagnostics.DebuggerNonUserCode] public ITerminalNode INT() { return GetToken(gramaticaParser.INT, 0); }
		public NumberContext(ExprContext context) { CopyFrom(context); }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterNumber(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitNumber(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitNumber(this);
			else return visitor.VisitChildren(this);
		}
	}
	public partial class DecimalContext : ExprContext {
		[System.Diagnostics.DebuggerNonUserCode] public ITerminalNode DECIMAL() { return GetToken(gramaticaParser.DECIMAL, 0); }
		public DecimalContext(ExprContext context) { CopyFrom(context); }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterDecimal(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitDecimal(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitDecimal(this);
			else return visitor.VisitChildren(this);
		}
	}
	public partial class MulDivContext : ExprContext {
		[System.Diagnostics.DebuggerNonUserCode] public ExprContext[] expr() {
			return GetRuleContexts<ExprContext>();
		}
		[System.Diagnostics.DebuggerNonUserCode] public ExprContext expr(int i) {
			return GetRuleContext<ExprContext>(i);
		}
		public MulDivContext(ExprContext context) { CopyFrom(context); }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterMulDiv(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitMulDiv(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitMulDiv(this);
			else return visitor.VisitChildren(this);
		}
	}
	public partial class AddSubContext : ExprContext {
		[System.Diagnostics.DebuggerNonUserCode] public ExprContext[] expr() {
			return GetRuleContexts<ExprContext>();
		}
		[System.Diagnostics.DebuggerNonUserCode] public ExprContext expr(int i) {
			return GetRuleContext<ExprContext>(i);
		}
		public AddSubContext(ExprContext context) { CopyFrom(context); }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterAddSub(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitAddSub(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitAddSub(this);
			else return visitor.VisitChildren(this);
		}
	}
	public partial class ParensContext : ExprContext {
		[System.Diagnostics.DebuggerNonUserCode] public ExprContext expr() {
			return GetRuleContext<ExprContext>(0);
		}
		public ParensContext(ExprContext context) { CopyFrom(context); }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterParens(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitParens(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitParens(this);
			else return visitor.VisitChildren(this);
		}
	}
	public partial class CadenaContext : ExprContext {
		[System.Diagnostics.DebuggerNonUserCode] public ITerminalNode CADENA() { return GetToken(gramaticaParser.CADENA, 0); }
		public CadenaContext(ExprContext context) { CopyFrom(context); }
		[System.Diagnostics.DebuggerNonUserCode]
		public override void EnterRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.EnterCadena(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override void ExitRule(IParseTreeListener listener) {
			IgramaticaListener typedListener = listener as IgramaticaListener;
			if (typedListener != null) typedListener.ExitCadena(this);
		}
		[System.Diagnostics.DebuggerNonUserCode]
		public override TResult Accept<TResult>(IParseTreeVisitor<TResult> visitor) {
			IgramaticaVisitor<TResult> typedVisitor = visitor as IgramaticaVisitor<TResult>;
			if (typedVisitor != null) return typedVisitor.VisitCadena(this);
			else return visitor.VisitChildren(this);
		}
	}

	[RuleVersion(0)]
	public ExprContext expr() {
		return expr(0);
	}

	private ExprContext expr(int _p) {
		ParserRuleContext _parentctx = Context;
		int _parentState = State;
		ExprContext _localctx = new ExprContext(Context, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		EnterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			EnterOuterAlt(_localctx, 1);
			{
			State = 35;
			ErrorHandler.Sync(this);
			switch (TokenStream.LA(1)) {
			case INT:
				{
				_localctx = new NumberContext(_localctx);
				Context = _localctx;
				_prevctx = _localctx;

				State = 28;
				Match(INT);
				}
				break;
			case DECIMAL:
				{
				_localctx = new DecimalContext(_localctx);
				Context = _localctx;
				_prevctx = _localctx;
				State = 29;
				Match(DECIMAL);
				}
				break;
			case CADENA:
				{
				_localctx = new CadenaContext(_localctx);
				Context = _localctx;
				_prevctx = _localctx;
				State = 30;
				Match(CADENA);
				}
				break;
			case T__1:
				{
				_localctx = new ParensContext(_localctx);
				Context = _localctx;
				_prevctx = _localctx;
				State = 31;
				Match(T__1);
				State = 32;
				expr(0);
				State = 33;
				Match(T__2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			Context.Stop = TokenStream.LT(-1);
			State = 45;
			ErrorHandler.Sync(this);
			_alt = Interpreter.AdaptivePredict(TokenStream,3,Context);
			while ( _alt!=2 && _alt!=global::Antlr4.Runtime.Atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( ParseListeners!=null )
						TriggerExitRuleEvent();
					_prevctx = _localctx;
					{
					State = 43;
					ErrorHandler.Sync(this);
					switch ( Interpreter.AdaptivePredict(TokenStream,2,Context) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						PushNewRecursionContext(_localctx, _startState, RULE_expr);
						State = 37;
						if (!(Precpred(Context, 6))) throw new FailedPredicateException(this, "Precpred(Context, 6)");
						State = 38;
						_la = TokenStream.LA(1);
						if ( !(_la==T__3 || _la==T__4) ) {
						ErrorHandler.RecoverInline(this);
						}
						else {
							ErrorHandler.ReportMatch(this);
						    Consume();
						}
						State = 39;
						expr(7);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						PushNewRecursionContext(_localctx, _startState, RULE_expr);
						State = 40;
						if (!(Precpred(Context, 5))) throw new FailedPredicateException(this, "Precpred(Context, 5)");
						State = 41;
						_la = TokenStream.LA(1);
						if ( !(_la==T__5 || _la==T__6) ) {
						ErrorHandler.RecoverInline(this);
						}
						else {
							ErrorHandler.ReportMatch(this);
						    Consume();
						}
						State = 42;
						expr(6);
						}
						break;
					}
					} 
				}
				State = 47;
				ErrorHandler.Sync(this);
				_alt = Interpreter.AdaptivePredict(TokenStream,3,Context);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			ErrorHandler.ReportError(this, re);
			ErrorHandler.Recover(this, re);
		}
		finally {
			UnrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public override bool Sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4: return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private bool expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0: return Precpred(Context, 6);
		case 1: return Precpred(Context, 5);
		}
		return true;
	}

	private static int[] _serializedATN = {
		4,1,11,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,1,1,
		5,1,16,8,1,10,1,12,1,19,9,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
		4,1,4,1,4,1,4,1,4,3,4,36,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,44,8,4,10,4,12,
		4,47,9,4,1,4,0,1,8,5,0,2,4,6,8,0,2,1,0,4,5,1,0,6,7,49,0,10,1,0,0,0,2,13,
		1,0,0,0,4,20,1,0,0,0,6,22,1,0,0,0,8,35,1,0,0,0,10,11,3,2,1,0,11,12,5,0,
		0,1,12,1,1,0,0,0,13,17,3,4,2,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,
		0,17,15,1,0,0,0,17,18,1,0,0,0,18,3,1,0,0,0,19,17,1,0,0,0,20,21,3,6,3,0,
		21,5,1,0,0,0,22,23,5,1,0,0,23,24,5,2,0,0,24,25,3,8,4,0,25,26,5,3,0,0,26,
		7,1,0,0,0,27,28,6,4,-1,0,28,36,5,9,0,0,29,36,5,10,0,0,30,36,5,11,0,0,31,
		32,5,2,0,0,32,33,3,8,4,0,33,34,5,3,0,0,34,36,1,0,0,0,35,27,1,0,0,0,35,
		29,1,0,0,0,35,30,1,0,0,0,35,31,1,0,0,0,36,45,1,0,0,0,37,38,10,6,0,0,38,
		39,7,0,0,0,39,44,3,8,4,7,40,41,10,5,0,0,41,42,7,1,0,0,42,44,3,8,4,6,43,
		37,1,0,0,0,43,40,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,
		9,1,0,0,0,47,45,1,0,0,0,4,17,35,43,45
	};

	public static readonly ATN _ATN =
		new ATNDeserializer().Deserialize(_serializedATN);


}
