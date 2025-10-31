import re
import matplotlib.pyplot as plt
import numpy as np

CORDAS = {
    'violino': {'G3': 55, 'D4': 62, 'A4': 69, 'E5': 76},
    'viola': {'C3': 48, 'G3': 55, 'D4': 62, 'A4': 69},
    'violoncelo': {'C2': 36, 'G2': 43, 'D3': 50, 'A3': 57},
}

NOTAS = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
         'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
         'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11}

def nota_para_midi(nota):
    m = re.match(r"([A-Ga-g#b]+)(\d)", nota)
    if not m:
        raise ValueError(f"Nota inválida: {nota}")
    nome, oitava = m.groups()
    nome = nome.capitalize()
    return NOTAS[nome] + (int(oitava) + 1) * 12

def posicoes_possiveis(nota, instrumento, alcance=12):
    midi_nota = nota_para_midi(nota)
    posicoes = []
    for corda, midi_corda in CORDAS[instrumento].items():
        dif = midi_nota - midi_corda
        if 0 <= dif <= alcance:
            posicoes.append((corda, dif))
    return posicoes

def todas_combinacoes(nota1, nota2, instrumento):
    pos1 = posicoes_possiveis(nota1, instrumento)
    pos2 = posicoes_possiveis(nota2, instrumento)
    combs = []
    for c1, d1 in pos1:
        for c2, d2 in pos2:
            if c1 != c2:
                combs.append(((c1, d1), (c2, d2)))
    return combs

def semiton_to_position(n, L=1.0):
    """Mapeia o número de semitons para posição física (não linear)."""
    return L * (1 - 2**(-n/12))

def diagrama_double_stops_realista(nota1, nota2, instrumento):
    combs = todas_combinacoes(nota1, nota2, instrumento)
    if not combs:
        print(f"Nenhuma combinação possível para {nota1} e {nota2} em {instrumento}.")
        return

    cordas = list(CORDAS[instrumento].keys())
    fig, axes = plt.subplots(len(combs), 1, figsize=(8, 2*len(combs)), sharex=True)

    if len(combs) == 1:
        axes = [axes]

    for ax, comb in zip(axes, combs):
        ax.set_title(f"{comb[0][0]}: {comb[0][1]} st | {comb[1][0]}: {comb[1][1]} st", fontsize=10)

        # desenha as cordas
        for i, corda in enumerate(cordas):
            xs = [semiton_to_position(n) for n in np.linspace(0, 12, 100)]
            ax.plot(xs, [i]*len(xs), color='lightgray')
            ax.text(-0.03, i, corda, ha='right', va='center', fontsize=10)

        # desenha os pontos
        for (corda, semitons) in comb:
            y = cordas.index(corda)
            x = semiton_to_position(semitons)
            ax.plot(x, y, 'o', color='black', markersize=10 if semitons == 0 else 8, 
                    fillstyle='none' if semitons > 0 else 'full')

        ax.set_xlim(-0.05, semiton_to_position(12) + 0.05)
        ax.set_ylim(-0.5, len(cordas)-0.5)
        ax.set_yticks([])
        ax.set_xlabel("Posição (proporcional ao braço)")
        ax.set_xticks([semiton_to_position(i) for i in range(0, 13, 2)])
        ax.set_xticklabels([str(i) for i in range(0, 13, 2)])
        ax.grid(False)

    plt.suptitle(f"{instrumento.capitalize()} — Combinações para {nota1} e {nota2}", fontsize=14, weight='bold')
    plt.tight_layout()
    plt.show()
