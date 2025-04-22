public enum SymbolType
{
    Integer,
    Double,
    String,
    Boolean ,
    Void
}

public class Symbol
{
    public object Value { get; set; }
    public SymbolType Type { get; set; }

    public Symbol(object value, SymbolType type)
    {
        Value = value;
        Type = type;
    }
}

public class Environment
{
    public Dictionary<string, Symbol> Variables = new Dictionary<string, Symbol>();
    private Dictionary<string,  (List<string> parameters, LanguageParser.BlockContext body)> functions = new();
    public Environment Parent { get; set; }

    private int temporal;
    private int msg;
    private int label;

    public Environment(Environment parent = null)
    {
        Parent = parent;
        temporal = -1;
        msg = -1;
        label = -1;

    }

    public Symbol GetVariable(string id)
    {
        if (Variables.ContainsKey(id))
        {
            return Variables[id];
        }
        else if (Parent != null)
        {
            return Parent.GetVariable(id);
        }
        else
        {
            //throw new Exception("Variable " + id + " not found");
            return null;
        }
    }

    public void SetVariable(string id, object value, SymbolType type)
    {
        if (Variables.ContainsKey(id))
        {
            Variables[id] = new Symbol(value, type);
        }
        else
        {
            Variables.Add(id, new Symbol(value, type));
        }
    }

    public void SetFunciones(string id, List<string> parametros, LanguageParser.BlockContext body)
    {
        if (functions.ContainsKey(id))
        {
            functions[id] = (parametros, body);
        }
        else
        {
            functions.Add(id, (parametros, body));
        }
    }
    public object GetFuncion(string id)
    {
        if (functions.ContainsKey(id))
        {
            return functions[id];
        }
        else if (Parent != null)
        {
            return Parent.GetVariable(id);
        }
        else
        {
            return null;
        }
    }
    public int generateTemporal(){
        temporal += 1;

        if(temporal == 7){
            temporal =  0;
        }

        return temporal;
    }

    public int lastTemporal(){
        return temporal;
    }

    public int generateLabel(){
        label += 1;
        return label;
    }

    public int lastLabel(){
        return label;
    }
    public int generateMsg(){
        msg += 1;
        return msg;
    }

    public int lastMsg(){
        return msg;
    }


}
