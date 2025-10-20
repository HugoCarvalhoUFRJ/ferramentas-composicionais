# Simula Xenakis

Código desenvolvido a pedido do [Prof. Liduino Pitombeira](https://pitombeira.com/) para facilitar a geração de material musical utilizando ferramentas estocásticas, conforme Iannis Xenakis. Todas as funções do arquivo `XENAKIS.py` são de minha autoria, seguindo instruções do Prof. Liduino, e gerados com assistência de LLM para melhor lidar com o pacote `music21`.

1) Entre no [Google Colab](https://colab.research.google.com/), e clique no botão azul `+ Novo notebook`. Esteja logado em sua conta Google, pois esse notebook poderá ser acessado novamente.

2) Na célula que tem um botão de `Play` do lado esquerdo, copie e cole as duas linhas de código abaixo:
```python
!wget https://raw.githubusercontent.com/HugoCarvalhoUFRJ/ferramentas-composicionais/refs/heads/main/simula-xenakis/XENAKIS.py
from XENAKIS import *
```

3) Clique no botão de `Play`, e quando aparecer um *check* verde ao lado dele, deu tudo certo.

4) Abaixo do bloco com esse código, coloque o mouse na metade da parte inferior desse bloco para aparecer um menu, e clique em `+ Código`. Irá aparecer uma nova célula de código abaixo.

5) Abaixo segue um exemplo de utilização das funções dentro do arquivo `XENAKIS.py`. Copie e cole esse código em uma célula do Google Colab, faça as suas modificações e rode a célula:
```python
pesos = {
 "C": 0.1, "C#": 0.5, "D": 0.8, "D#": 0.7,
 "E": 1.2, "F": 1, "F#": 0.5, "G": 1,
 "G#": 0.8, "A": 1, "A#": 0.5, "B": 1
 } # Declara o peso de cada nota no sorteio aleatório, a ser realizado abaixo.

n_compassos = 4 # Quantidade de compassos a serem gerados.

n_partes = 3 # Número de partes na peça.

lambd = 3 # Parâmetro da distribuição de Poisson, que irá controlar quantas notas são sorteadas em cada compasso de cada parte.
          # Pense nesse número como o número médio de notas por casa compasso de cada parte.

nome_arquivo_saida = 'xenakis.mid' # Nome do arquivo MIDI a ser gerado com as notas sorteadas

# Daqui pra baixo você não precisa modificar nada.

df_xenakis = gerar_matriz_musical( # Essa é a função principal do código, que irá sortear notas de acordo com os parâmetros.
    pesos=pesos,
    n_compassos=n_compassos, 
    n_partes=n_partes,
    lambd=lambd,
) # Esse código irá gerar um DataFrame, essencialmente uma tabela, que servirá de entrada para o próximo código.

dataframe_para_midi( # Essa função recebe como entrada o dataframe gerado acima e cria um arquivo MIDI correspondente.
    df = df_xenakis, # 
    arquivo_saida = nome_arquivo_saida
)
```

6) Após executar o código acima, será gerado um arquivo MIDI, que estará armazenado nessa seção do Google Colab. Para baixá-lo pro seu computador, clique no ícone de uma pasta do lado esquerdo da tela, coloque o mouse em cima do arquivo MIDI gerado, clique no `...` vertical que irá aparecer e depois em "Fazer download.
   
7) Você pode criar quantas células de código quiser, para rodar o código diversas vezes.

8) Se você ficar muito tempo sem usar essa janela do Google Colab, você será desconectado do servidor. Para reativar a sua seção, você precisará rodar o primeiro bloco de código, com todas as funções, novamente.

9) Esse *notebook* ficará salvo em sua conta do Google. Por padrão, ele terá um nome `UntitlecNUMERO.ipynb`, mas você pode alterá-lo no cabeçalho da página, e sempre que entrar no Google Colab, poderá acessá-lo novamente.
