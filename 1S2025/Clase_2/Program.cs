using System;
using Antlr4.Runtime;

namespace AntlrExample
{
    public class EvalVisitor : gramaticaBaseVisitor<double> {
        public override double VisitStart(gramaticaParser.StartContext context)
        {
            return Visit(context.expr());
        }

        public override double VisitExpr(gramaticaParser.ExprContext context)
        {
            if(context.INT() != null ){
                return double.Parse(context.INT().GetText());
            }
            else if(context.DECIMAL() != null ){
                return double.Parse(context.DECIMAL().GetText());
            }
            else if(context.CADENA() != null){
                Console.WriteLine(context.CADENA().GetText());
                return 1.0;
            }
            else if(context.ChildCount == 3){
                double left = Visit(context.GetChild(0));
                double right = Visit(context.GetChild(2));
                string op = context.GetChild(1).GetText();

                return op switch {
                    "+" => left + right,
                    "-" => left - right,
                    "*" => left * right,
                    "/" => left / right,
                    _ => Visit(context.GetChild(1)),
                };
            }
            else if(context.ChildCount == 1){
                return Visit(context.GetChild(1));
            }

         throw new Exception("Expresión inválida");
        }

    }
 
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Entrada de texto (puedes cambiar esto por un archivo o entrada del usuario)
                string input = "'HOLA A TODOS, COMPI2 SECCION A'"; // Reemplaza con algo válido según tu gramática

                // Crear el input stream
                AntlrInputStream inputStream = new AntlrInputStream(input);

                // Inicializar el lexer generado
                var lexer = new gramaticaLexer(inputStream);

                // Crear un token stream
                CommonTokenStream tokenStream = new CommonTokenStream(lexer);

                // Inicializar el parser generado
                var parser = new gramaticaParser(tokenStream);

                // Parsear el texto usando la regla principal de tu gramática
                var tree = parser.start(); // Cambia "r" por la regla principal de tu gramática

                // Imprimir el árbol de sintaxis en consola
                EvalVisitor visitor = new EvalVisitor();
                double result = visitor.VisitStart(tree) ;
                Console.WriteLine(result);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
