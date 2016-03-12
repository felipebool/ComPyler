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

### Formato do programa
```C
   // Definição de variáveis/constantes
   // Definição de funções
   main {
      // o main não tem o 'int' e não recebe parâmetros
      // variáveis/comandos
   }
```

### Declaração de variáveis
```C
   tipo identificador;
```

### Tipos
```C
   int
   char
   float
   string
```

### Identificador
```C
   letra{letra/numero}
```

### Constantes
```C
   // somente constantes numéricas
   const identificador = num;
```

### Números
   Sequência de dígitos, com ou sem '.'. Se tiver ponto, é seguido por sequência
   de dígitos.

### Char
   Aspas simples, uma letra, fecha aspas simples, exemplo: 'a'.

### Literal
   Aspas dupas, uma string, fecha aspas duplas, exemplo: "aaa".

### Comentários
```C
   /* somente comentários multi linha
   farão parte da linguagem */
```

