grammar SimpleLang;

prog: stat+ ;

stat: ifStat
    | whileStat
    | assignStat
    | exprStat;

ifStat: 'if' '(' expr ')' 'then' stat ;
whileStat: 'while' '(' expr ')' stat;
assignStat: ID '=' expr ';';
exprStat: expr ';';
expr: expr ('*' | '/') expr                     # MulDivExpr
    | expr ('+' | '-') expr                     # AddSubExpr
    | expr ('<' | '>' | '==' | '!=') expr       # RelationalExpr
    | expr ('&&' | '||') expr                   # LogicalExpr
    | '!' expr                                  # NotExpr
    | ID                                        # IdExpr
    | INT                                       # IntExpr
    | '(' expr ')'                              # ParenExpr;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;

