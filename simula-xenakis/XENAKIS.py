import numpy as np
import pandas as pd
from music21 import stream, note, meter, tempo, midi, instrument, key

def gerar_matriz_musical(
    pesos: dict[str, float],
    n_compassos: int,
    n_partes: int,
    lambd: float,
    semente: int | None = None
    ) -> pd.DataFrame:
    
    """
    Gera um DataFrame representando células musicais sorteadas segundo
    pesos cromáticos e distribuição de Poisson.

    Parâmetros
    ----------
    pesos : dict[str, float]
        Dicionário com pesos associados a cada nota (12 notas da escala cromática).
        Exemplo: {"C": 0.2, "C#": 0.05, ..., "B": 0.1}
    n_compassos : int
        Número de colunas (compassos) no DataFrame.
    n_partes : int
        Número de linhas (partes) no DataFrame.
    lambd : float
        Parâmetro λ da distribuição de Poisson que define a quantidade de notas por célula.
    semente : int | None, opcional
        Semente para reprodutibilidade.

    Retorna
    -------
    pd.DataFrame
        DataFrame com shape (n_partes, n_compassos).
        Cada célula contém uma lista de notas sorteadas de acordo com os pesos e Poisson(λ).
    """

    if semente is not None:
        np.random.seed(semente)

    notas = list(pesos.keys())
    probabilidades = np.array(list(pesos.values()), dtype=float)
    probabilidades /= probabilidades.sum()  # normalização

    matriz = []
    for parte in range(n_partes):
        linha = []
        for compasso in range(n_compassos):
            n_notas = np.random.poisson(lambd)
            if n_notas == 0:
                celula = []
            else:
                celula = list(np.random.choice(notas, size=n_notas, p=probabilidades))
            linha.append(celula)
        matriz.append(linha)

    # criar o DataFrame
    df = pd.DataFrame(
        matriz,
        index=[f"Parte_{i+1}" for i in range(n_partes)],
        columns=[f"Compasso_{j+1}" for j in range(n_compassos)]
    )

    return df

def dataframe_para_midi(
    df: pd.DataFrame,
    arquivo_saida: str = "saida.mid"
    ):

    """
    Converte o DataFrame gerado anteriormente em um arquivo MIDI.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame onde cada célula contém uma lista de notas (strings).
    arquivo_saida : str, opcional
        Caminho do arquivo MIDI a ser gerado.
    """

    # 0. Dicionário para converter nomes de notas para alturas relativas (0–11)
    MAPA_NOTAS = {
        "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5,
        "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11
    }
    
    # 1. Determinar K = maior quantidade de notas em qualquer célula
    K = max(len(notas) for linha in df.values for notas in linha)
    # print(f"Maior quantidade de notas em uma célula (K): {K}")

    # 2. Criar partitura principal
    partitura = stream.Score()
    partitura.append(tempo.MetronomeMark(number=90))  # andamento padrão
    partitura.append(meter.TimeSignature(f"{K}/4"))

    # 3. Criar partes (linhas do DataFrame)
    for nome_parte, linha in df.iterrows():
        parte = stream.Part()
        parte.id = nome_parte
        # parte.insert(0, instrument.WoodwindInstrument())  # genérico
        parte.append(meter.TimeSignature(f"{K}/4"))

        for idx_compasso, notas_celula in enumerate(linha):
            comp = stream.Measure(number=idx_compasso + 1)
            comp.append(meter.TimeSignature(f"{K}/4"))

            # Garantir lista válida
            if not isinstance(notas_celula, (list, tuple)):
                notas_celula = [notas_celula]

            # Adicionar notas e pausas
            for i in range(K):
                duracao = 1.0  # semínima
                if i < len(notas_celula) and notas_celula[i] in MAPA_NOTAS:
                    altura_relativa = MAPA_NOTAS[notas_celula[i]]
                    altura_midi = 72 + (altura_relativa % 12)
                    if altura_midi > 76:
                        altura_midi -= 12
                    n_midi = note.Note(altura_midi, quarterLength=duracao)
                    comp.append(n_midi)
                else:
                    comp.append(note.Rest(quarterLength=duracao))

            parte.append(comp)

        partitura.append(parte)

    # 4. Exportar o arquivo MIDI
    mf = midi.translate.streamToMidiFile(partitura)
    mf.open(arquivo_saida, 'wb')
    mf.write()
    mf.close()
    print(f"Arquivo MIDI gerado: {arquivo_saida}")
