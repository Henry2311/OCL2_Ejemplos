//using gramatica;

class CompilerVisitor : gramaticaBaseVisitor<int>
{

    public override int VisitPrint(gramaticaParser.PrintContext context)
    {
        return Visit(context.expr());
    }

    public override int VisitAddSub(gramaticaParser.AddSubContext context)
    {
        int left = Visit(context.expr(0));
        int right = Visit(context.expr(1));

        return context.GetChild(1).GetText() == "+" ? left + right : left - right;
    }

    public override int VisitMulDiv(gramaticaParser.MulDivContext context)
    {
        int left = Visit(context.expr(0));
        int right = Visit(context.expr(1));

        return context.GetChild(1).GetText() == "*" ? left * right : left / right;
    }

    public override int VisitNumber(gramaticaParser.NumberContext context)
    {
        return int.Parse(context.INT().GetText());
    }

    // public override int VisitCadena(gramaticaParser.CadenaContext context)
    // {
    //     return context.CADENA().GetText();
    // }

    // public override int VisitDecimal(gramaticaParser.DecimalContext context)
    // {
    //     return double.Parse(context.DECIMAL().GetText());
    // }

    public override int VisitParens(gramaticaParser.ParensContext context)
    {
        return Visit(context.expr());
    }

}