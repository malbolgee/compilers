grammar Html;

root: questao+;

questao: (qTexto | qRadioBox | qCheckBox | qMenu | qBotao);

qTexto: 'TEXTO' NUMERO NUMERO str_;
qRadioBox: 'ESCOLHAUMA' str_ opcoes;
qCheckBox: 'ESCOLHAVARIAS' str_ opcoes;
qMenu: 'MENU' IDENT str_ opcoesMenu;
qBotao: 'BOTAO' str_ str_;
opcoes: '(' str_ (',' str_)* ')';
opcoesMenu: '(' menuOpcao (',' menuOpcao)* ')';
menuOpcao: IDENT ':' str_;

str_: STRING;

// TOKENS:
NUMERO: [0-9]+;
STRING: '"' (~["])* '"';
IGNORE: [ \n\r\t] -> skip;
IDENT: [a-zA-Z_][a-zA-Z0-9_]*;
COMMENT: '#' ~[\r\n]* -> skip;
