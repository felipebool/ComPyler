# Analisador Léxico

## Definição da linguagem
A linguagem utilizada é uma versão simplificada de C

### Comandos
#### For
```C
   for (atribuicao; teste; incremento) {
      // commandos
   }
```

#### While
```C
   while (teste) {
      // comandos
   }
```

#### If
```C
   if (teste) {
      // comandos
   }
```

#### Atribuição
```C
   id = numero;
   id = expressao_numerica;
   id = caractere;
   id = literal;
```
---

### Formato do programa
```C
   // Definição de variáveis/constantes
   // Definição de funções
   main {
      // o main não tem o 'int' e não recebe parâmetros
      // variáveis/comandos
   }
```
---

### Declaração de variáveis
```C
   tipo identificador;
```
---

### Tipos
```C
   int
   char
   float
   string
```
---

### Identificador
```C
   letra{letra/numero}
```
---

### Constantes
```C
   // somente constantes numéricas
   const identificador = num;
```
---

### Números
   Sequência de dígitos, com ou sem ponto. Se tiver ponto, é seguido por sequência de dígitos.
   Por exemplo: 123, 12.345
---

### Char
   Aspas simples, uma letra, fecha aspas simples, exemplo: 'a'.
---

### Literal
   Aspas dupas, uma string, fecha aspas duplas, exemplo: "aaa".
---

### Comentários
```C
   /* somente comentários multi linha
   farão parte da linguagem */
```
---

### Expressões aritméticas
| operador| op_arit | operador|
|---------|---------|---------|
|num      |op_arit  | num     |
|num      |op_arit  | id      |
|id       |op_arit  | num     |
|id       |op_arit  | id      |


#### op_arit
   * [\+] Adição
   * [\-] Subtração
   * [\*] Multiplicação
   * [/] Divisão de inteiros
   * [#]   Divisão de reais
---

### Expressões relacionais
| operador| op_rel | operador|
|---------|--------|---------|
|num      |op_rel  | num     |
|num      |op_rel  | id      |
|id       |op_rel  | num     |
|id       |op_rel  | id      |

#### op_rel
   * [==] Igualdade
   * [!=] Diferença
   * [<] Menor que
   * [>] Maior que
   * [>=]
---

### Teste
   * Expressão relacional
   * Expressão lógica

#### Expressão lógica
| operador | op_log | operador  |
|----------|--------|-----------|
|(exp_rel) |op_log  | (exp_rel) |

