## **Table of Contents**
- [E2 - Komanda](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_e_02_komanda.html&ref=master#mcetoc_1f33pqfa46) 
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_e_02_komanda.html&ref=master#mcetoc_1f33pqfa47)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_e_02_komanda.html&ref=master#mcetoc_1f33pqfa48)
  - [Desafio](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_e_02_komanda.html&ref=master#mcetoc_1f33pqfa49)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_e_02_komanda.html&ref=master#mcetoc_1egvoav555j) 
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_e_02_komanda.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_e_02_komanda.html&ref=master#mcetoc_1eh146n6m3)
# **E2 - Komanda**
Nessa entrega você criará um sistema de gerenciamento de mesas para cafés.


## **Objetivo**
Trabalhar seus conhecimentos de **listas** e **dicionários** no Python. 


## **Preparativos**
Você deverá criar um arquivo chamado **komanda.py** e copiar o código abaixo para este arquivo. Dessa forma, a variável **menu** guarda uma lista de dicionários, onde cada dicionário representa um produto de um café.

menu = [

`    `{'id': 1, 'name': 'ADICIONAL FRANGO 50G', 'price': 4.0},

`    `{'id': 2, 'name': 'SALADA', 'price': 18.0},

`    `{'id': 3, 'name': 'ADICIONAL DE LEITE', 'price': 1.0},

`    `{'id': 4, 'name': 'AMERICANO', 'price': 5.0},

`    `{'id': 5, 'name': 'CAPUCCINO', 'price': 7.0},

`    `{'id': 6, 'name': 'CARIOCA', 'price': 5.0},

`    `{'id': 7, 'name': 'COADO', 'price': 6.0},

`    `{'id': 8, 'name': 'COADO PEQUENO', 'price': 3.0},

`    `{'id': 9, 'name': 'DUPLO MACCHIATO', 'price': 9.0},

`    `{'id': 10, 'name': 'ESPRESSO', 'price': 5.0},

`    `{'id': 11, 'name': 'ESPRESSO DUPLO', 'price': 8.0},

`    `{'id': 12, 'name': 'FRENCH PRESS 300ML', 'price': 8.0},

`    `{'id': 13, 'name': 'FRENCH PRESS 600ML', 'price': 14.0},

`    `{'id': 14, 'name': 'LATTE', 'price': 7.0},

`    `{'id': 15, 'name': 'MACCHIATO', 'price': 6.0},

`    `{'id': 16, 'name': 'MOCCHA', 'price': 9.0},

`    `{'id': 17, 'name': 'AFFOGATO', 'price': 8.0},

`    `{'id': 18, 'name': 'COLD BREW', 'price': 8.0},

`    `{'id': 19, 'name': 'LATTE GELADO', 'price': 7.0},

`    `{'id': 20, 'name': 'MOCCHA GELADO', 'price': 10.0},

`    `{'id': 21, 'name': 'STELLA ARTOIS 310ML', 'price': 6.0},

`    `{'id': 22, 'name': 'CHÁ GELADO', 'price': 7.0},

`    `{'id': 23, 'name': 'CHÁ QUENTE', 'price': 5.0},

`    `{'id': 24, 'name': 'MATE BATIDO', 'price': 7.0},

`    `{'id': 25, 'name': 'CHOCOLATE QUENTE', 'price': 8.0},

`    `{'id': 26, 'name': 'DESAYUNO', 'price': 18.0},

`    `{'id': 27, 'name': 'ADICIONAL GRANOLA', 'price': 1.0},

`    `{'id': 28, 'name': 'BOLO FATIA', 'price': 5.0},

`    `{'id': 29, 'name': 'BOLO NO POTE', 'price': 8.0},

`    `{'id': 30, 'name': 'BRIGADEIRO', 'price': 2.0},

`    `{'id': 31, 'name': 'BROWNIE CHOCOLATE', 'price': 5.0},

`    `{'id': 32, 'name': 'COOKIE', 'price': 5.0},

`    `{'id': 33, 'name': 'FOLHADO DOCE', 'price': 5.0},

`    `{'id': 34, 'name': 'FRENCH TOAST', 'price': 5.0},

]

Em seguida, você deverá escrever uma variável chamada **table\_1**, que representa o consumo de uma mesa arbitrária. O consumo de cada mesa será representado por uma **lista de dicionários**, onde cada dicionário contém apenas: o **id do produto** e a **quantidade de vezes que o produto foi consumido.** Por exemplo:

table\_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
## ** 
## **Desafio**
Escreva uma função chamada **calculate\_tab** que recebe como argumento uma lista com o mesmo formato de **table\_1**.

Essa função deverá calcular o **valor total do consumo da mesa**.

Usando a variável **table\_1** como exemplo:

total = calculate\_tab(table\_1)

print(total) 

\> 55.0

-----

# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:** 
  - arquivo **komanda.py**.
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|5|Criação de arquivo **komanda.py** com variável **menu**|Verificada pela equipe de ensino|Esteja de acordo com o solicitado|
|5|Função **calculate\_tab**|Executada a bateria de testes semelhante ao que foi especificado nas **Entradas e Saídas**|O retorno seja de acordo com o especificado|


**Boa diversão, devs! ⛩**






