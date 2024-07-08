// Autor: Victor Hugo
// Autor: Aldemir Silva
// Autor: Nilson Andrade

grammar MiniC;

program : definition+ EOF ;

definition : data_definition | function_definition ;
data_definition : TYPE IDENTIFIER (',' IDENTIFIER)* ';' ;
function : function_call | function_definition ;
function_definition : TYPE? function_header function_body ;
function_header : IDENTIFIER '(' parameter_list? ')' ;
parameter : TYPE IDENTIFIER;
parameter_list : parameter (',' parameter)* ;
function_call : IDENTIFIER '(' argument_list? ')' ;
function_body : '{' (data_definition | statement)* '}' ;
argument_list : binary (',' binary)* ;
statement : compound_statement
         | expression_statement
         | if_statement
         | while_statement
         | assignment_statement
         | BREAK ';'
         | CONTINUE ';'
         | RETURN expression ';'
         ;
compound_statement : '{' statement* '}' ;
expression_statement : expression? ';' ;
while_statement : 'while' '(' expression ')' statement ;
if_statement : IF '(' expression ')' statement (ELSE statement)? ;
expression : binary ;
assignment_statement :   <assoc=right>IDENTIFIER '=' expression
                       | <assoc=right>IDENTIFIER '+=' expression
                       | <assoc=right>IDENTIFIER '-=' expression
                       | <assoc=right>IDENTIFIER '*=' expression
                       | <assoc=right>IDENTIFIER '/=' expression
                       | <assoc=right>IDENTIFIER '%=' expression
                       ;
binary : binary '*' binary
       | binary '/' binary
       | binary '%' binary
       | binary '+' binary
       | binary '-' binary
       | binary '<' binary
       | binary '>' binary
       | binary '<=' binary
       | binary '>=' binary
       | binary '==' binary
       | binary '!=' binary
       | binary '&&' binary
       | binary '||' binary
       | unary
       ;
unary : PLUS_PLUS IDENTIFIER | MINUS_MINUS IDENTIFIER | primary ;
primary : IDENTIFIER | CONSTANT_INT | CONSTANT_CHAR | function_call | '(' expression ')' ;

PLUS_PLUS : '++' ;
MINUS_MINUS : '--' ;
IF : 'if' ;
ELSE : 'else' ;
RETURN : 'return' ;
BREAK : 'break' ;
CONTINUE : 'continue' ;
TYPE : ('int'| 'char') ;
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;
CONSTANT_INT : [0-9]+ ;
CONSTANT_CHAR : '\'' . '\'' ;
WS : [ \t\r\n]+ -> skip ;
