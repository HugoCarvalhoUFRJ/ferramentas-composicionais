# Visualiza _double stops_

Código desenvolvido para facilitar a visualização de _double stops_ nos braços do violino, viola e violoncelo. Todas as funções do arquivo `DOUBLE_STOP.py` são de minha autoria, com assistência de LLM. Adicionamente, gerei o tutorial abaixo para estudantes que não estão familiarizados com Python.

1) Entre no [Google Colab](https://colab.research.google.com/), e clique no botão azul `+ Novo notebook`. Esteja logado em sua conta Google, pois esse notebook poderá ser acessado novamente.

2) Na célula que tem um botão de `Play` do lado esquerdo, copie e cole as duas linhas de código abaixo:
```python
!wget https://raw.githubusercontent.com/HugoCarvalhoUFRJ/ferramentas-composicionais/refs/heads/main/double-stop/DOUBLE_STOP.py
from DOUBLE_STOP import *
```

3) Clique no botão de `Play`, e quando aparecer um *check* verde ao lado dele, deu tudo certo.

4) Abaixo do bloco com esse código, coloque o mouse na metade da parte inferior desse bloco para aparecer um menu, e clique em `+ Código`. Irá aparecer uma nova célula de código abaixo.

5) Abaixo segue um exemplo de utilização das funções dentro do arquivo `XENAKIS.py`. Copie e cole esse código em uma célula do Google Colab, faça as suas modificações e rode a célula:
```python
diagrama_double_stops_realista('A4', 'G#5', 'violino')
```

6) Após executar o código acima, será gerada uma figura, ilustrando possibilidades de tocar essas duas notas no braço do instrumento em questão. Uma bolinha preta à esquerda do gráfico significa corda solta.
   
7) Você pode criar quantas células de código quiser, para rodar o código diversas vezes.

8) Se você ficar muito tempo sem usar essa janela do Google Colab, você será desconectado do servidor. Para reativar a sua seção, você precisará rodar o primeiro bloco de código, com todas as funções, novamente.
9) Esse *notebook* ficará salvo em sua conta do Google. Por padrão, ele terá um nome `UntitlecNUMERO.ipynb`, mas você pode alterá-lo no cabeçalho da página, e sempre que entrar no Google Colab, poderá acessá-lo novamente.
