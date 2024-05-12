grammar URL;

prog : protocol domain port? path? query? fragment_? EOF;

domain : word;
protocol : ('http' | 'https' | 'ftp') '://';
query : '?' word '=' word ('&' word '=' word)*;
path : '/' (CHARACTER '/')* CHARACTER;
fragment_ : '#' word;
port : ':' NUMBER;
word :  (CHARACTER | NUMBER)+;
NUMBER : [0-9]+;
CHARACTER : [a-zA-Z._-]+;
