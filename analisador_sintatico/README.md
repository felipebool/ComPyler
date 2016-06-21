#Analisador Léxico

##Definição do trabalho 2
Fazer o analisador sintático SLR(1) para a linguagem definida em sala.

###Entregar 
* Tabela de análise sintática SLR(1)
* Relatório (este arquivo)
* Data: 21/06/16
* Em dupla
* Valor: 3.0

##Mudanças na gramática
Na gramática definida em classe existiam algumas regras que tratavam dos tokens de números,
são elas:

NUM -> NUM_INT | NUM_FLOAT

NUM_INT -> DIGITO NUM_INT | DIGITO

NUM_FLOAT -> NUM_INT.NUM_INT

Estas regras saíram da gramática do nosso trabalho pois a análise léxica já resolve o problema
com os diferentes tipos de números, retornando um token num, contendo o número encontrado,
independente de ser inteiro ou float, respeitando, em ambos os casos, as regras de formação
de inteiros e float da linguagem definida.

## Bugs conhecidos

### Identificação da linha do erro sintático
Devido a uma decisão de projeto, ainda na fase de análise léxica, ficou inviável,
no tempo que ainda nos resta, apresentar a linha exata onde o erro sintático ocorreu.
O analisador léxico somente retorna a linha quando ocorre um erro léxico.

Este problema foi detectado no final do desenvolvimento, apesar disso, seria possível
implementar a saída correta (mostrando a linha onde ocorreu o erro) enviando junto com
cada token a linha onde o token ocorre, este valor fica armazenado na variável *line*
no arquivo [automata.py](../analisador_lexico/automata.py) do analisador léxico. Bastaria,
então, adicionar um novo campo ao token gerado e adicionar o valor de *line* a ele.

Para remediar este problema, quando acontece um erro sintático, é imprimido o token
atual e os valores que estavam na pilha no momento do erro, assim, é possível
encontrar o erro acompanhando as sequências de reduções aplicadas até o momento.

