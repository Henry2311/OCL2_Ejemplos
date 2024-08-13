Start
  = Statement

Statement
  = "System.out.println" _ "(" _ StringLiteral _ ")" _ ";" {
      return { type: "println", value: $4 };
    }

StringLiteral
  = "\"" chars:Char* "\"" {
      return chars.join("");
    }

Char
  = [^"]

_ "whitespace"
  = [ \t\n\r]*
