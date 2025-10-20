# Calculadora Hindemith

Código desenvolvido a pedido do [Prof. Liduino Pitombeira](https://pitombeira.com/) para facilitar o uso das teorias de Paul Hindemith na análise e composiçãço musical. Todas as funções do arquivo `HINDEMITH.py` são de autoria do Prof. Liduino, com exceção da função `note_to_pitch` (de autoria do meu aluno de Iniciação Científica Rumenick Brandi) e da função `gera_hindemith` (de minha autoria). Dessa forma, minha contribuição para o código foi, essencialmente, organizacional a fim de facilitar o uso, bem como gerar o tutorial abaixo para estudantes que não estão familiarizados com Python.

1) Entre no [Google Colab](https://colab.research.google.com/), e clique no botão azul `+ Novo notebook`. Esteja logado em sua conta Google, pois esse notebook poderá ser acessado novamente.

2) Na célula que tem um botão de `Play` do lado esquerdo, copie e cole as duas linhas de código abaixo:

```python
!wget https://raw.githubusercontent.com/HugoCarvalhoUFRJ/ferramentas-composicionais/refs/heads/main/calculadora-hindemith/HINDEMITH.py`
from HINDEMITH import *
```

4) Clique no botão de `Play`, e quando aparecer um *check* verde ao lado dele, deu tudo certo.

5) Abaixo do bloco com esse código, coloque o mouse na metade da parte inferior desse bloco para aparecer um menu, e clique em `+ Código`. Irá aparecer uma nova célula de código abaixo.

6) Para verificar o tipo de um acorde, use a seguinte função: `hindemith(['C4', 'D4', 'D#4', 'Gb4'])`, e clique no botão de `Play`. O resultado irá aparecer imediatamente abaixo do seu código.

Obs.: O programa aceita notas com sustenidos e com bemóis, desde `C0` até `B10`. Preste atenção à sintaxe, qualquer parênteses, colchete ou aspas mal colocado dará erro.

6) Você pode criar quantas células de código quiser, então você pode rodar essa mesma função num bloco abaixo, por exemplo.

7) Para gerar acordes de determinado tipo, use: `gera_hindemith(tipo = 'IV.2', mais_grave = 'C4', mais_aguda = 'C5', cardinalidade = 5, tentativas = 100)`. Assim, você irá gerar acordes de determinado tipo, com a nota mais grave prescrita, e com a cardinalidade prescrita. O programa funciona na força bruta, então ele gera tentativas acordes aleatórios no âmbito que você deseja, e verifica se é do tipo que você quer. Como é um sorteio, não necessariamente a `mais_aguda` estará no seu acorde, mas a `mais_grave` sempre estará.

8) Apesar da função `hindemith` lidar com enarmonias, a função `gera_hindemith` não o faz. Portanto, ela sempre irá retornar os acordes com bemol.

9) Rodar a função `gera_hindemith` diversas vezes irá gerar resultados diferentes! Se a sua geração não retornou nenhum acorde, tente novamente ou aumente o valor de `tentativas`.

10) Se você ficar muito tempo sem usar essa janela do Google Colab, você será desconectado do servidor. Para reativar a sua seção, você precisará rodar o primeiro bloco de código, com todas as funções, novamente.

11) Esse *notebook* ficará salvo em sua conta do Google. Por padrão, ele terá um nome `UntitlecNUMERO.ipynb`, mas você pode alterá-lo no cabeçalho da página, e sempre que entrar no Google Colab, poderá acessá-lo novamente.
