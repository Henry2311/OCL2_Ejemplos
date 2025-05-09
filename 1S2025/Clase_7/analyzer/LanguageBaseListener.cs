//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     ANTLR Version: 4.13.2
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

// Generated from Language.g4 by ANTLR 4.13.2

// Unreachable code detected
#pragma warning disable 0162
// The variable '...' is assigned but its value is never used
#pragma warning disable 0219
// Missing XML comment for publicly visible type or member '...'
#pragma warning disable 1591
// Ambiguous reference in cref attribute
#pragma warning disable 419


using Antlr4.Runtime.Misc;
using IErrorNode = Antlr4.Runtime.Tree.IErrorNode;
using ITerminalNode = Antlr4.Runtime.Tree.ITerminalNode;
using IToken = Antlr4.Runtime.IToken;
using ParserRuleContext = Antlr4.Runtime.ParserRuleContext;

/// <summary>
/// This class provides an empty implementation of <see cref="ILanguageListener"/>,
/// which can be extended to create a listener which only needs to handle a subset
/// of the available methods.
/// </summary>
[System.CodeDom.Compiler.GeneratedCode("ANTLR", "4.13.2")]
[System.Diagnostics.DebuggerNonUserCode]
[System.CLSCompliant(false)]
public partial class LanguageBaseListener : ILanguageListener {
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.program"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterProgram([NotNull] LanguageParser.ProgramContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.program"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitProgram([NotNull] LanguageParser.ProgramContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>PrintStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterPrintStmt([NotNull] LanguageParser.PrintStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>PrintStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitPrintStmt([NotNull] LanguageParser.PrintStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>IfStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterIfStmt([NotNull] LanguageParser.IfStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>IfStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitIfStmt([NotNull] LanguageParser.IfStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>WhileStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterWhileStmt([NotNull] LanguageParser.WhileStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>WhileStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitWhileStmt([NotNull] LanguageParser.WhileStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>FuncDeclStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterFuncDeclStmt([NotNull] LanguageParser.FuncDeclStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>FuncDeclStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitFuncDeclStmt([NotNull] LanguageParser.FuncDeclStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>ReturnStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterReturnStmt([NotNull] LanguageParser.ReturnStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>ReturnStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitReturnStmt([NotNull] LanguageParser.ReturnStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>FuncCallStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterFuncCallStmt([NotNull] LanguageParser.FuncCallStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>FuncCallStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitFuncCallStmt([NotNull] LanguageParser.FuncCallStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>AsignStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterAsignStmt([NotNull] LanguageParser.AsignStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>AsignStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitAsignStmt([NotNull] LanguageParser.AsignStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>VarDeclStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterVarDeclStmt([NotNull] LanguageParser.VarDeclStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>VarDeclStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitVarDeclStmt([NotNull] LanguageParser.VarDeclStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>ArryDclStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterArryDclStmt([NotNull] LanguageParser.ArryDclStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>ArryDclStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitArryDclStmt([NotNull] LanguageParser.ArryDclStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>SliceDclStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterSliceDclStmt([NotNull] LanguageParser.SliceDclStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>SliceDclStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitSliceDclStmt([NotNull] LanguageParser.SliceDclStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>AppendSliceStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterAppendSliceStmt([NotNull] LanguageParser.AppendSliceStmtContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>AppendSliceStmt</c>
	/// labeled alternative in <see cref="LanguageParser.dcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitAppendSliceStmt([NotNull] LanguageParser.AppendSliceStmtContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.block"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterBlock([NotNull] LanguageParser.BlockContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.block"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitBlock([NotNull] LanguageParser.BlockContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.varDcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterVarDcl([NotNull] LanguageParser.VarDclContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.varDcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitVarDcl([NotNull] LanguageParser.VarDclContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.varAsign"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterVarAsign([NotNull] LanguageParser.VarAsignContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.varAsign"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitVarAsign([NotNull] LanguageParser.VarAsignContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.varCall"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterVarCall([NotNull] LanguageParser.VarCallContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.varCall"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitVarCall([NotNull] LanguageParser.VarCallContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.parametros"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterParametros([NotNull] LanguageParser.ParametrosContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.parametros"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitParametros([NotNull] LanguageParser.ParametrosContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.param"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterParam([NotNull] LanguageParser.ParamContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.param"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitParam([NotNull] LanguageParser.ParamContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.args"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterArgs([NotNull] LanguageParser.ArgsContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.args"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitArgs([NotNull] LanguageParser.ArgsContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.sliceDcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterSliceDcl([NotNull] LanguageParser.SliceDclContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.sliceDcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitSliceDcl([NotNull] LanguageParser.SliceDclContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.appendSlice"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterAppendSlice([NotNull] LanguageParser.AppendSliceContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.appendSlice"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitAppendSlice([NotNull] LanguageParser.AppendSliceContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.arrayDcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterArrayDcl([NotNull] LanguageParser.ArrayDclContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.arrayDcl"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitArrayDcl([NotNull] LanguageParser.ArrayDclContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.list_values"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterList_values([NotNull] LanguageParser.List_valuesContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.list_values"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitList_values([NotNull] LanguageParser.List_valuesContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>MulDiv</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterMulDiv([NotNull] LanguageParser.MulDivContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>MulDiv</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitMulDiv([NotNull] LanguageParser.MulDivContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>AddSub</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterAddSub([NotNull] LanguageParser.AddSubContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>AddSub</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitAddSub([NotNull] LanguageParser.AddSubContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>ArrayAccessExpr</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterArrayAccessExpr([NotNull] LanguageParser.ArrayAccessExprContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>ArrayAccessExpr</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitArrayAccessExpr([NotNull] LanguageParser.ArrayAccessExprContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Parens</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterParens([NotNull] LanguageParser.ParensContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Parens</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitParens([NotNull] LanguageParser.ParensContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Logical</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterLogical([NotNull] LanguageParser.LogicalContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Logical</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitLogical([NotNull] LanguageParser.LogicalContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>String</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterString([NotNull] LanguageParser.StringContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>String</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitString([NotNull] LanguageParser.StringContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Double</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterDouble([NotNull] LanguageParser.DoubleContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Double</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitDouble([NotNull] LanguageParser.DoubleContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Integer</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterInteger([NotNull] LanguageParser.IntegerContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Integer</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitInteger([NotNull] LanguageParser.IntegerContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Not</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterNot([NotNull] LanguageParser.NotContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Not</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitNot([NotNull] LanguageParser.NotContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Identifier</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterIdentifier([NotNull] LanguageParser.IdentifierContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Identifier</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitIdentifier([NotNull] LanguageParser.IdentifierContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Compare</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterCompare([NotNull] LanguageParser.CompareContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Compare</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitCompare([NotNull] LanguageParser.CompareContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Negate</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterNegate([NotNull] LanguageParser.NegateContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Negate</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitNegate([NotNull] LanguageParser.NegateContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>Boolean</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterBoolean([NotNull] LanguageParser.BooleanContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>Boolean</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitBoolean([NotNull] LanguageParser.BooleanContext context) { }
	/// <summary>
	/// Enter a parse tree produced by the <c>FuncCallExpr</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterFuncCallExpr([NotNull] LanguageParser.FuncCallExprContext context) { }
	/// <summary>
	/// Exit a parse tree produced by the <c>FuncCallExpr</c>
	/// labeled alternative in <see cref="LanguageParser.expr"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitFuncCallExpr([NotNull] LanguageParser.FuncCallExprContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.type"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterType([NotNull] LanguageParser.TypeContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.type"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitType([NotNull] LanguageParser.TypeContext context) { }
	/// <summary>
	/// Enter a parse tree produced by <see cref="LanguageParser.arrAccess"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void EnterArrAccess([NotNull] LanguageParser.ArrAccessContext context) { }
	/// <summary>
	/// Exit a parse tree produced by <see cref="LanguageParser.arrAccess"/>.
	/// <para>The default implementation does nothing.</para>
	/// </summary>
	/// <param name="context">The parse tree.</param>
	public virtual void ExitArrAccess([NotNull] LanguageParser.ArrAccessContext context) { }

	/// <inheritdoc/>
	/// <remarks>The default implementation does nothing.</remarks>
	public virtual void EnterEveryRule([NotNull] ParserRuleContext context) { }
	/// <inheritdoc/>
	/// <remarks>The default implementation does nothing.</remarks>
	public virtual void ExitEveryRule([NotNull] ParserRuleContext context) { }
	/// <inheritdoc/>
	/// <remarks>The default implementation does nothing.</remarks>
	public virtual void VisitTerminal([NotNull] ITerminalNode node) { }
	/// <inheritdoc/>
	/// <remarks>The default implementation does nothing.</remarks>
	public virtual void VisitErrorNode([NotNull] IErrorNode node) { }
}
