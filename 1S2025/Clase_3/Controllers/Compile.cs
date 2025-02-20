using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
//using gramatica;
using Antlr4.Runtime;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;


namespace Clase_3.Controllers{
[Route("[controller]")]
    public class Compile : Controller
    {
        private readonly ILogger<Compile> _logger;

        public Compile(ILogger<Compile> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View("Error!");
        }

        public class CompileRequest
        {
            [Required]
            public required string Code { get; set; }
            public required string Nombre { get; set; }
        }

        // POST /compile
        [HttpPost]
        public async Task<IActionResult> Post([FromBody] CompileRequest request)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            _logger.LogInformation("Compiling code: {0}", request.Code);

            var inputStream = new AntlrInputStream(request.Code);
            var lexer = new gramaticaLexer(inputStream);
            var tokenStream = new CommonTokenStream(lexer);
            var parser = new gramaticaParser(tokenStream);
            var tree = parser.start();

            var visitor = new CompilerVisitor();
            var result = visitor.Visit(tree);

            return Ok(result);
        }
    }
}