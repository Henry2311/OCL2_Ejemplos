using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using analyzer;
using Antlr4.Runtime;
using Antlr4.Runtime.Tree;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace api.Controllers
{
    [Route("[controller]")]
    public class Compile : Controller
    {
        private readonly ILogger<Compile> _logger;

        public Compile(ILogger<Compile> logger)
        {
            _logger = logger;
        }

        public class CompileRequest
        {
            [Required]
            public required string code { get; set; }
        }

        // POST /compile
        [HttpPost]
        public IActionResult Post([FromBody] CompileRequest request)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(new { error = "Invalid request" });
            }

            var inputStream = new AntlrInputStream(request.code);
            var lexer = new LanguageLexer(inputStream);
            var tokens = new CommonTokenStream(lexer);
            var parser = new LanguageParser(tokens);

            var tree = parser.program();

            var visitor = new CompilerVisitor();
            visitor.Visit(tree);

            return Ok(new { result = visitor.output });

            // var walker = new ParseTreeWalker();
            // var lister = new CompilerListerner();
            // walker.Walk(lister, tree);

            // return Ok(new { result = lister.GetResult() });
        }

    }
}