//using analyzer;

using Antlr4.Runtime.Misc;

public class CompilerAssembler : LanguageBaseVisitor<object>
{

  public string output = "";
  public string dato = "";
    private Environment currentEnvironment = new Environment();
    private Dictionary<string,  (List<string> parameters, LanguageParser.BlockContext body)> functions = new();

    // VisitProgram
    public override object VisitProgram(LanguageParser.ProgramContext context)
    {
        foreach (var dcl in context.dcl())
        {
            Visit(dcl);
        }
        return null;
    }
    public override object VisitVarDeclStmt(LanguageParser.VarDeclStmtContext context)
    {
        var varDecl = context.varDcl();
        string id = varDecl.ID().GetText();

        dato += id+": .word 0\n"; //msg0

        object value = Visit(varDecl.expr());
        var tmp = currentEnvironment.generateTemporal();
        output+=$@"LDR X{tmp}, ={id}
                   STR X{value}, [X{tmp}]
        ";

        // Validación de tipo
       // if (!IsValidType(value, type))
       // {
            //throw new Exception($"Type mismatch: Cannot assign {value?.GetType().Name} to {type}");
        //}
        //A = 100  MOV X10, #100 
        // SP -> STACK POINTER 
        //
        /*[sp] = #10 1111 1111 1111 1111

        a: .word 0

        MOV X0, #99 //CREAR UN VALOR EN EJECUCION
        LDR X1, =a // X1 tiene la direccion de memoria de A
        STR X0, X1 // A = 99

        LDR X1, =a
        LDR X2, [X1]
        X2 = 99


        SUB     sp, sp, #16    // reservar 16 bytes en stack
        MOV     X0, #10
        MOV     X1, #5
        STR     X0, [sp]       // guardar a en [sp]
        STR     X1, [sp, #4]   // guardar b en [sp+4]
        LDR     X2, [sp]       // cargar a en w2
        LDR     X3, [sp, #4]   // cargar b en w3
        ADD     X4, X2, X3     // result = a + b
        ADD     sp, sp, #16    // liberar stack
        
        */
        return null;

    }
    public override object VisitAsignStmt(LanguageParser.AsignStmtContext context){
        var varAsign = context.varAsign();
        string id = varAsign.ID().GetText();
        
        object value = Visit(varAsign.expr());

        output+=$@"LDR X1, ={id}
                   STR X{value}, [X1]
        ";

        return null;
    }

    public override object VisitIdentifier(LanguageParser.IdentifierContext context)
    {
        string id = context.ID().GetText();
        var tmp = currentEnvironment.generateTemporal();
        output+=$@"LDR X1, ={id}
                   LDR X{tmp}, [X1]
        ";

        return tmp;
    }

    public override object VisitPrintStmt(LanguageParser.PrintStmtContext context)
    {
        object value = Visit(context.expr());
        
        if(context.expr().GetType().Name == "IntegerContext" || context.expr().GetType().Name == "AddSubContext"){
            if ((int)value == 0){
                output += @$"b print_integer
                " ;  
            }else {
                output += @$"mov x0, x{value}
                            b print_integer
                " ; 
            }   
        }else{
            output += "mov x0, 1\n" ;           
            output += "ldr x1, ="+value+"\n";      
            output += "mov x2, 14"+"\n";    
            output += "mov x8, 64"+"\n";         
            output += "svc 0"+"\n"; 
        }
        
        return null;
    }

    public override object VisitParens(LanguageParser.ParensContext context)
    {
        return Visit(context.expr());
    }
    public override object VisitAddSub(LanguageParser.AddSubContext context)
    {
        dynamic left = Visit(context.expr(0)); //X0
        dynamic right = Visit(context.expr(1)); //X1

        if (left is string && right is string && context.op.Text == "+")
            return left + right; // Concatenación de strings

        if ((left is int || left is double) && (right is int || right is double)){

            var tmp = currentEnvironment.generateTemporal();
            if(context.op.Text == "+"){
                output += $@"add x{tmp}, x{left}, x{right}
                ";
            }else{
                output += $@"sub x{tmp}, x{left}, x{right}
                ";
            }
            return tmp;
        }

        throw new Exception("Addition/Subtraction is only valid for numbers or concatenation of strings.");
    }
    public override object VisitInteger(LanguageParser.IntegerContext context)
    {        
        var tmp = currentEnvironment.generateTemporal(); //0 X0

        output+=$@"mov x{tmp}, {context.GetText()}
        "; // x0 =  

        return tmp;
    }
       // VisitCompare
    public override object VisitCompare(LanguageParser.CompareContext context)
    {
        dynamic left = Visit(context.expr(0));
        dynamic right = Visit(context.expr(1));

        if (!(left is int || left is double) || !(right is int || right is double))
            throw new Exception("Comparison operators can only be applied to numbers.");

        var label = currentEnvironment.generateLabel(); //L1 L2 L3 L4
            if(context.op.Text == "<"){
                output += $@"cmp x{left}, x{right}
                            blt L{label} 
                ";
            }else{
                output += $@"
                cmp x{left}, x{right}
                bgt L{label}
                ";
            }
            return label;
    }


    public override object VisitIfStmt(LanguageParser.IfStmtContext context)
    {
        object condition = Visit(context.expr()); //L1

        object ret = null;

        var else_label = currentEnvironment.generateLabel(); //L2
        var exit_label = currentEnvironment.generateLabel(); //L3

        output += $@"L{condition}:
        ";
        ret = Visit(context.block(0));

        output += $@"b L{exit_label}
        ";

        output += $@"L{else_label}:
        ";
        ret = Visit(context.block(1));
        output += $@"L{exit_label}:
        ";

        
        return ret;
    }


    // VisitDouble
    public override object VisitDouble(LanguageParser.DoubleContext context)
    {
        return double.Parse(context.GetText());
    }

    // VisitString
    public override object VisitString(LanguageParser.StringContext context)
    {
        var msg = currentEnvironment.generateMsg(); //0
        var cadena = context.GetText().Trim('"');
        dato += "msg"+msg+": .asciz \""+cadena+"\"\n"; //msg0
        return "msg"+msg; //msg0
    }

    // VisitBoolean
    public override object VisitBoolean(LanguageParser.BooleanContext context)
    {
        return bool.Parse(context.GetText());
    }


}