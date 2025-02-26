//using analyzer;

public class CompilerVisitor : LanguageBaseVisitor<object>
{
    public string output = "";
    private Environment currentEnvironment = new Environment();

    // VisitProgram
    public override object VisitProgram(LanguageParser.ProgramContext context)
    {
        foreach (var dcl in context.dcl())
        {
            Visit(dcl);
        }
        return null;
    }

    // VisitVarDcl
    public override object VisitVarDeclStmt(LanguageParser.VarDeclStmtContext context)
    {
        var varDecl = context.varDcl();
        string id = varDecl.ID().GetText();
        string typeText = varDecl.type().GetText();
        SymbolType type = Enum.Parse<SymbolType>(typeText);
        object value = Visit(varDecl.expr());

        // Validación de tipo
        if (!IsValidType(value, type))
        {
            throw new Exception($"Type mismatch: Cannot assign {value?.GetType().Name} to {type}");
        }

        currentEnvironment.SetVariable(id, value, type);
        return null;
    }

    // VisitExprStmt
    public override object VisitExprStmt(LanguageParser.ExprStmtContext context)
    {
        return Visit(context.expr());
    }

    // VisitPrintStmt
    public override object VisitPrintStmt(LanguageParser.PrintStmtContext context)
    {
        object value = Visit(context.expr());
        output += value + "\n";
        return null;
    }

    // VisitIdentifier
    public override object VisitIdentifier(LanguageParser.IdentifierContext context)
    {
        string id = context.ID().GetText();
        return currentEnvironment.GetVariable(id).Value;
    }

    // VisitParens
    public override object VisitParens(LanguageParser.ParensContext context)
    {
        return Visit(context.expr());
    }

    // VisitNegate
    public override object VisitNegate(LanguageParser.NegateContext context)
    {
        object value = Visit(context.expr());

        if (value is int intValue) return -intValue;
        if (value is double doubleValue) return -doubleValue;

        throw new Exception("Negation can only be applied to numbers.");
    }

    // VisitNumber
    public override object VisitInteger(LanguageParser.IntegerContext context)
    {
        return int.Parse(context.GetText());
    }

    // VisitDouble
    public override object VisitDouble(LanguageParser.DoubleContext context)
    {
        return double.Parse(context.GetText());
    }

    // VisitString
    public override object VisitString(LanguageParser.StringContext context)
    {
        return context.GetText().Trim('"');
    }

    // VisitBoolean
    public override object VisitBoolean(LanguageParser.BooleanContext context)
    {
        return bool.Parse(context.GetText());
    }

    // VisitMulDiv
    public override object VisitMulDiv(LanguageParser.MulDivContext context)
    {
        dynamic left = Visit(context.expr(0));
        dynamic right = Visit(context.expr(1));

        if (left is string || right is string)
            throw new Exception("Multiplication and division are not supported for strings.");

        return context.op.Text == "*" ? left * right : left / right;
    }

    // VisitAddSub
    public override object VisitAddSub(LanguageParser.AddSubContext context)
    {
        dynamic left = Visit(context.expr(0));
        dynamic right = Visit(context.expr(1));

        if (left is string && right is string && context.op.Text == "+")
            return left + right; // Concatenación de strings

        if ((left is int || left is double) && (right is int || right is double))
            return context.op.Text == "+" ? left + right : left - right;

        throw new Exception("Addition/Subtraction is only valid for numbers or concatenation of strings.");
    }

    // VisitCompare
    public override object VisitCompare(LanguageParser.CompareContext context)
    {
        dynamic left = Visit(context.expr(0));
        dynamic right = Visit(context.expr(1));

        if (!(left is int || left is double) || !(right is int || right is double))
            throw new Exception("Comparison operators can only be applied to numbers.");

        return context.op.Text == "<" ? left < right : left > right;
    }

    // VisitLogical
    public override object VisitLogical(LanguageParser.LogicalContext context)
    {
        object left = Visit(context.expr(0));
        object right = Visit(context.expr(1));

        if (!(left is bool) || !(right is bool))
            throw new Exception("Logical operators can only be applied to booleans.");

        return context.op.Text == "&&" ? (bool)left && (bool)right : (bool)left || (bool)right;
    }

    // VisitNot
    public override object VisitNot(LanguageParser.NotContext context)
    {
        object value = Visit(context.expr());
        if (value is bool boolValue) return !boolValue;

        throw new Exception("Negation (!) can only be applied to booleans.");
    }

    // VisitIfStmt
    public override object VisitIfStmt(LanguageParser.IfStmtContext context)
    {
        object condition = Visit(context.expr());

        if (condition is not bool)
            throw new Exception("If statement condition must be a boolean.");

        if ((bool)condition)
        {
            Environment new_environment = new Environment(currentEnvironment);

            currentEnvironment = new_environment;
            Visit(context.block(0)); // Ejecutar el bloque del 'if'
            currentEnvironment = new_environment.Parent;
        }
        else if (context.block().Length > 1)
        {
            Visit(context.block(1)); // Ejecutar el bloque del 'else' si existe
        }

        return null;
    }

    public override object VisitAsignStmt(LanguageParser.AsignStmtContext context){
        var varAsign = context.varAsign();
        string id = varAsign.ID().GetText();
        SymbolType type = Enum.Parse<SymbolType>("Integer");
        object value = Visit(varAsign.expr());

        currentEnvironment.SetVariable(id, value, type);
        return null;
    }
    //WHILE
    public override object VisitWhileStmt(LanguageParser.WhileStmtContext context)
    {
        // object condition = Visit(context.expr());

        // if (condition is not bool)
        //     throw new Exception("If statement condition must be a boolean.");

        while((bool) Visit(context.expr())){
            Visit(context.block());
        }
        return null;

    }

    // Validar tipos
    private bool IsValidType(object value, SymbolType type)
    {
        return type switch
        {
            SymbolType.Integer => value is int,
            SymbolType.Double => value is double,
            SymbolType.String => value is string,
            SymbolType.Boolean => value is bool,
            _ => false,
        };
    }
}
