using System;
using Antlr4.Runtime;

namespace AntlrExample
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Entrada de texto (puedes cambiar esto por un archivo o entrada del usuario)
                string input = "10+10"; // Reemplaza con algo válido según tu gramática

                // Crear el input stream
                AntlrInputStream inputStream = new AntlrInputStream(input);

                // Inicializar el lexer generado
                var lexer = new gramaticaLexer(inputStream);

                // Crear un token stream
                CommonTokenStream tokenStream = new CommonTokenStream(lexer);

                // Inicializar el parser generado
                var parser = new gramaticaParser(tokenStream);

                // Parsear el texto usando la regla principal de tu gramática
                var tree = parser.prog(); // Cambia "r" por la regla principal de tu gramática

                // Imprimir el árbol de sintaxis en consola
                Console.WriteLine(tree.ToStringTree(parser));
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
