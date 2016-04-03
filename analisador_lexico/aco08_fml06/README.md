#Analisador Léxico

O analisador léxico foi implementado utilizando um autômato relativamente simples.
São 14 estados, 6 deles estados de aceitação, 1 estado inicial, e o restante estados
de erro.

Quando um erro é detectado em algum dos estados de aceitação, o automato "transita"
para algum dos estados de erro. Na prática, a mensagem de erro é gerada no estado
de aceitação e o token é retornado para o estado inicial com a mensagem de erro e
a linha onde ocorreu o erro.


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
Estado que reconhece *números*. 

####Transições
   * 0-9\.DELIMITERS:                  DOT_WITHOUT_NUMBER
   * (O-9 + ((0-9)\*\.(0-9)\*):        EXTRA_DOTS
   * (0-9)(0-9)\*(a-z + A-Z)\*(0-9)\*: ID_OR_NUMBER
   * FORBIDDEN:                        FORBIDDEN_SYMBOL


###is_alpha
Estado que reconhece *identificadores*, *palavras reservadas*, e *tipos*.

####Transições
   * FORBIDDEN:                        FORBIDDEN_SYMBOL


###is_string_char_value
Estado que reconhece valores atribuídos para *strings* e *chars*.

####Transições
   * '(a-z + A-Z)(a-z + A-Z)\*': BIG_CHAR
   * "":                         EMPTY_STRING


###is_logical_op_or_attr
Estado que reconhece *operadores lógicos* e *atribuição*.

####Transições
   * FORBIDDEN:                        FORBIDDEN_SYMBOL


###is_arithmetic
Estado que reconhece *operadores aritméticos*.

####Transições
Este estado não gera transições


###is_special_char
Estado que reconhece *símbolos especiais da linguagem*, por exemplo, '{' e ';'

####Transições
Este estado não gera transições




Contagem de linhas

Decisões de projeto

- Identificado começando com número ou número com símbolo letra
Quando um símbolo número é lido em get_token, o automato transita para o estado
is_digit, onde o processamento do número acontece. Caso, em algum momento, seja
lido um símbolo letra, é gerado um erro léxico. O erro sinaliza duas
possibilidades: ou existe uma letra no meio do número ou o identificador começa
com um número.


