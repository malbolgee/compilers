grammar MinC;

program : definition+ EOF;

definition : data_definition | function_definition;
data_definition : 'int' declarator (',' declarator)* ';';
declarator : IDENTIFIER;
function_definition : 'int'? function_header function_body;
function_header : declarator '(' parameter_list? ')';
parameter : 'int' IDENTIFIER;
parameter_list : parameter (',' parameter)*;
function_body : '{' (data_definition | statement)* '}';
statement : compound_statement
         | expression_statement
         | if_statement
         | while_statement
         | 'break' ';'
         | 'continue' ';'
         | 'return' expression? ';'
         ;
compound_statement : '{' statement* '}';
expression_statement : expression? ';';
while_statement : 'while' '(' expression ')' statement;
if_statement : 'if' '(' expression ')' statement ('else' statement)?;
expression : binary (',' binary)*;
binary : IDENTIFIER '=' binary
       | IDENTIFIER '+=' binary
       | IDENTIFIER '-=' binary
       | IDENTIFIER '*=' binary
       | IDENTIFIER '/=' binary
       | IDENTIFIER '%=' binary
       | binary '==' binary
       | binary '&&' binary
       | binary '||' binary
       | binary '!=' binary
       | binary '<' binary
       | binary '>' binary
       | binary '<=' binary
       | binary '>=' binary
       | binary '*' binary
       | binary '/' binary
       | binary '+' binary
       | binary '-' binary
       | binary '%' binary
       | unary
       ;
unary : IDENTIFIER '++' | IDENTIFIER '--' | primary;
primary : IDENTIFIER | CONSTANT_INT | '(' expression ')' | IDENTIFIER '(' argument_list? ')';
argument_list : binary (',' binary)*;

IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;
CONSTANT_INT : [0-9]+;
WS : [ \t\r\n]+ -> skip;
