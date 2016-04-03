#Analisador Léxico

O analisador léxico foi implementado utilizando um autômato relativamente simples.
São 14 estados, 6 deles estados de aceitação, 1 estado inicial, e o restante estados
de erro.


##Estados

###get_token (estado inicial)
O estado inicial é o get_token, esta função funciona como um roteador, ela lê o
primeiro caractere do lexema e escolhe o estado apropriado para direcionar o processamento
da string de entrada.

####Transições:
   * 0-9:       is_digit
   * a-z, A-Z:  is_alpha
   * ", ':      is_string_char_value
   * LOGI_OP:   is_logical_op_or_attr
   * ARIT_OP:   is_arithmetic
   * SPEC_CHAR: is_special_char
   * FORBIDDEN: FORBIDDEN_SYMBOL

###is_digit
Este estado reconhece lexemas que representam números. 

####Transições
   * 0-9\.DELIMITERS:                  DOT_WITHOUT_NUMBER
   * (O-9 + ((0-9)\*\.(0-9)\*):        EXTRA_DOTS
   * (0-9)(0-9)\*(a-z + A-Z)\*(0-9)\*: ID_OR_NUMBER
   * FORBIDDEN:                        FORBIDDEN_SYMBOL

###is_alpha

Contagem de linhas

Decisões de projeto

- Identificado começando com número ou número com símbolo letra
Quando um símbolo número é lido em get_token, o automato transita para o estado
is_digit, onde o processamento do número acontece. Caso, em algum momento, seja
lido um símbolo letra, é gerado um erro léxico. O erro sinaliza duas
possibilidades: ou existe uma letra no meio do número ou o identificador começa
com um número.


