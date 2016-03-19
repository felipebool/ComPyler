#Analisador Léxico

##Definição do trabalho 1
Fazer o analisador léxico para a linguagem definida logo abaixo.

o analisador **deve** ser implementado em uma função que retorna um
token a cada chamada.

O programa principal **deve** ser um loop até o final do arquivo com
chamadas sucessivas à função do analisador léxico. 

Após cada chamada da função, o programa principal deve gravar os token
no arquivo *saída.tokens*.

O programa deve indicar erros léxicos, mostrando em qual linha ocorreu,
o programa **pára no primeiro erro** encontrado 

##Definição da linguagem
A linguagem para implementação do analisador léxico é uma versão
simplificada do C e está definida em maiores detalhes logo abaixo.

###Comandos

For
```C
for (atribuicao; teste; incremento) {
   // commandos
}
```

While
```C
while (teste) {
   // comandos
}
```

If
```C
if (teste) {
   // comandos
}

if (teste) {
   // comandos
}
else {
   // comandos
}
```

####Atribuição
```C
id = numero;
id = expressao_numerica;
id = caractere;
id = literal;
```

###Formato do programa
```C
// Definição de variáveis/constantes
// Definição de funções
main {
   // o main não tem o 'int' e não recebe parâmetros
   // variáveis/comandos
}
```

###Declaração de variáveis
```C
tipo identificador;
```

###Tipos
```C
int
char
float
string
```

###Identificador
```C
letra{letra/numero}
```

###Constantes
```C
// somente constantes numéricas
const identificador = num;
```

###Números
Sequência de dígitos, com ou sem ponto. Se tiver ponto, é seguido por sequência de dígitos, 
por exemplo: 123, 12.345

###Char
Aspas simples, uma letra, fecha aspas simples, exemplo: 'a'.

###Literal
Aspas dupas, uma string, fecha aspas duplas, exemplo: "aaa".

###Comentários
```C
/* somente comentários multi linha
farão parte da linguagem */
```

<!--
###Expressões aritméticas
---
| operador| op\_arit | operador|
|---------|----------|---------|
|num      |op\_arit  | num     |
|num      |op\_arit  | id      |
|id       |op\_arit  | num     |
|id       |op\_arit  | id      |


####op\_arit
+, -, \*, / \(divisão de inteiros\) e \# \(divisão de reais\). 

###Expressões relacionais
---
| operador| op\_rel | operador|
|---------|---------|---------|
|num      |op\_rel  | num     |
|num      |op\_rel  | id      |
|id       |op\_rel  | num     |
|id       |op\_rel  | id      |



####Operadores
Os operadores relacionais são 
---

###Teste
---
   * Expressão relacional
   * Expressão lógica

####Expressão lógica
| operador  | op\_log | operador   |
|-----------|=--------|------------|
|(exp\_rel) |op\_log  | (exp\_rel) |
-->
