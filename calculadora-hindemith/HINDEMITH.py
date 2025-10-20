from itertools import combinations
import numpy as np

def note_to_pitch(note_name):
    ## AGRADECIMENTO AO ALUNO RUMENICK BRANDI (MATEMÁTICA APLICADA) PELA FUNÇÃO
    note_to_pitch_dict = {
    'C0': 12, 'C#0': 13, 'Db0': 13, 'D0': 14, 'D#0': 15, 'Eb0': 15, 'E0': 16, 'F0': 17, 'F#0': 18, 'Gb0': 18, 'G0': 19, 'G#0': 20, 'Ab0': 20, 'A0': 21, 'A#0': 22, 'Bb0': 22, 'B0': 23,
    'C1': 24, 'C#1': 25, 'Db1': 25, 'D1': 26, 'D#1': 27, 'Eb1': 27, 'E1': 28, 'F1': 29, 'F#1': 30, 'Gb1': 30, 'G1': 31, 'G#1': 32, 'Ab1': 32, 'A1': 33, 'A#1': 34, 'Bb1': 34, 'B1': 35,
    'C2': 36, 'C#2': 37, 'Db2': 37, 'D2': 38, 'D#2': 39, 'Eb2': 39, 'E2': 40, 'F2': 41, 'F#2': 42, 'Gb2': 42, 'G2': 43, 'G#2': 44, 'Ab2': 44, 'A2': 45, 'A#2': 46, 'Bb2': 46, 'B2': 47,
    'C3': 48, 'C#3': 49, 'Db3': 49, 'D3': 50, 'D#3': 51, 'Eb3': 51, 'E3': 52, 'F3': 53, 'F#3': 54, 'Gb3': 54, 'G3': 55, 'G#3': 56, 'Ab3': 56, 'A3': 57, 'A#3': 58, 'Bb3': 58, 'B3': 59,
    'C4': 60, 'C#4': 61, 'Db4': 61, 'D4': 62, 'D#4': 63, 'Eb4': 63, 'E4': 64, 'F4': 65, 'F#4': 66, 'Gb4': 66, 'G4': 67, 'G#4': 68, 'Ab4': 68, 'A4': 69, 'A#4': 70, 'Bb4': 70, 'B4': 71,
    'C5': 72, 'C#5': 73, 'Db5': 73, 'D5': 74, 'D#5': 75, 'Eb5': 75, 'E5': 76, 'F5': 77, 'F#5': 78, 'Gb5': 78, 'G5': 79, 'G#5': 80, 'Ab5': 80, 'A5': 81, 'A#5': 82, 'Bb5': 82, 'B5': 83,
    'C6': 84, 'C#6': 85, 'Db6': 85, 'D6': 86, 'D#6': 87, 'Eb6': 87, 'E6': 88, 'F6': 89, 'F#6': 90, 'Gb6': 90, 'G6': 91, 'G#6': 92, 'Ab6': 92, 'A6': 93, 'A#6': 94, 'Bb6': 94, 'B6': 95,
    'C7': 96, 'C#7': 97, 'Db7': 97, 'D7': 98, 'D#7': 99, 'Eb7': 99, 'E7': 100, 'F7': 101, 'F#7': 102, 'Gb7': 102, 'G7': 103, 'G#7': 104, 'Ab7': 104, 'A7': 105, 'A#7': 106, 'Bb7': 106, 'B7': 107,
    'C8': 108, 'C#8': 109, 'Db8': 109, 'D8': 110, 'D#8': 111, 'Eb8': 111, 'E8': 112, 'F8': 113, 'F#8': 114, 'Gb8': 114, 'G8': 115, 'G#8': 116, 'Ab8': 116, 'A8': 117, 'A#8': 118, 'Bb8': 118, 'B8': 119,
    'C9': 120, 'C#9': 121, 'Db9': 121, 'D9': 122, 'D#9': 123, 'Eb9': 123, 'E9': 124, 'F9': 125, 'F#9': 126, 'Gb9': 126, 'G9': 127, 'G#9': 128, 'Ab9': 128, 'A9': 129, 'A#9': 130, 'Bb9': 130, 'B9': 131,
    'C10': 132, 'C#10': 133, 'Db10': 133, 'D10': 134, 'D#10': 135, 'Eb10': 135, 'E10': 136, 'F10': 137, 'F#10': 138, 'Gb10': 138, 'G10': 139, 'G#10': 140, 'Ab10': 140, 'A10': 141, 'A#10': 142, 'Bb10': 142, 'B10': 143
    }
    
    return note_to_pitch_dict.get(note_name)

def pitch_to_note(note_number):
    note_to_pitch_dict = {
    'C0': 12, 'C#0': 13, 'Db0': 13, 'D0': 14, 'D#0': 15, 'Eb0': 15, 'E0': 16, 'F0': 17, 'F#0': 18, 'Gb0': 18, 'G0': 19, 'G#0': 20, 'Ab0': 20, 'A0': 21, 'A#0': 22, 'Bb0': 22, 'B0': 23,
    'C1': 24, 'C#1': 25, 'Db1': 25, 'D1': 26, 'D#1': 27, 'Eb1': 27, 'E1': 28, 'F1': 29, 'F#1': 30, 'Gb1': 30, 'G1': 31, 'G#1': 32, 'Ab1': 32, 'A1': 33, 'A#1': 34, 'Bb1': 34, 'B1': 35,
    'C2': 36, 'C#2': 37, 'Db2': 37, 'D2': 38, 'D#2': 39, 'Eb2': 39, 'E2': 40, 'F2': 41, 'F#2': 42, 'Gb2': 42, 'G2': 43, 'G#2': 44, 'Ab2': 44, 'A2': 45, 'A#2': 46, 'Bb2': 46, 'B2': 47,
    'C3': 48, 'C#3': 49, 'Db3': 49, 'D3': 50, 'D#3': 51, 'Eb3': 51, 'E3': 52, 'F3': 53, 'F#3': 54, 'Gb3': 54, 'G3': 55, 'G#3': 56, 'Ab3': 56, 'A3': 57, 'A#3': 58, 'Bb3': 58, 'B3': 59,
    'C4': 60, 'C#4': 61, 'Db4': 61, 'D4': 62, 'D#4': 63, 'Eb4': 63, 'E4': 64, 'F4': 65, 'F#4': 66, 'Gb4': 66, 'G4': 67, 'G#4': 68, 'Ab4': 68, 'A4': 69, 'A#4': 70, 'Bb4': 70, 'B4': 71,
    'C5': 72, 'C#5': 73, 'Db5': 73, 'D5': 74, 'D#5': 75, 'Eb5': 75, 'E5': 76, 'F5': 77, 'F#5': 78, 'Gb5': 78, 'G5': 79, 'G#5': 80, 'Ab5': 80, 'A5': 81, 'A#5': 82, 'Bb5': 82, 'B5': 83,
    'C6': 84, 'C#6': 85, 'Db6': 85, 'D6': 86, 'D#6': 87, 'Eb6': 87, 'E6': 88, 'F6': 89, 'F#6': 90, 'Gb6': 90, 'G6': 91, 'G#6': 92, 'Ab6': 92, 'A6': 93, 'A#6': 94, 'Bb6': 94, 'B6': 95,
    'C7': 96, 'C#7': 97, 'Db7': 97, 'D7': 98, 'D#7': 99, 'Eb7': 99, 'E7': 100, 'F7': 101, 'F#7': 102, 'Gb7': 102, 'G7': 103, 'G#7': 104, 'Ab7': 104, 'A7': 105, 'A#7': 106, 'Bb7': 106, 'B7': 107,
    'C8': 108, 'C#8': 109, 'Db8': 109, 'D8': 110, 'D#8': 111, 'Eb8': 111, 'E8': 112, 'F8': 113, 'F#8': 114, 'Gb8': 114, 'G8': 115, 'G#8': 116, 'Ab8': 116, 'A8': 117, 'A#8': 118, 'Bb8': 118, 'B8': 119,
    'C9': 120, 'C#9': 121, 'Db9': 121, 'D9': 122, 'D#9': 123, 'Eb9': 123, 'E9': 124, 'F9': 125, 'F#9': 126, 'Gb9': 126, 'G9': 127, 'G#9': 128, 'Ab9': 128, 'A9': 129, 'A#9': 130, 'Bb9': 130, 'B9': 131,
    'C10': 132, 'C#10': 133, 'Db10': 133, 'D10': 134, 'D#10': 135, 'Eb10': 135, 'E10': 136, 'F10': 137, 'F#10': 138, 'Gb10': 138, 'G10': 139, 'G#10': 140, 'Ab10': 140, 'A10': 141, 'A#10': 142, 'Bb10': 142, 'B10': 143
    }

    pitch_to_note_dict = {v: k for k, v in note_to_pitch_dict.items()}
    
    return pitch_to_note_dict.get(note_number)

def normal(acorde):
    
    #valores em módulo 12 
    acordepc = [x%12 for x in acorde]
    
    #elimina repetições e coloca na ordem crescente
    acorde = list(set(acordepc)) 
    acorde.sort()
    
    #valores em módulo 12 
    acordepc = [x%12 for x in acorde]
    
    #lista as rotações
    rotations = [list(np.roll(acordepc,-x)) for x in range(len(acordepc))] 
    
    #intervalos ordenados entre primeiro, segundo,...e última classe de altura
    intervalos =[[(rotations[x][i+1]-rotations[x][0])%12 for i in range(len(rotations[x])-1)] for x in range(len(rotations))]
    
    #somas dos intervalos
    somasinternas = [sum(intervalos[x]) for x in range(len(intervalos))]
    
    position = somasinternas.index(min(somasinternas))
    
    normalform = rotations[position]
    
    return(normalform)
    
    
def prima(acorde):
    
    normalform = normal(acorde)
    invnormalform = normal([(12-normalform[x])%12 for x in range(len(normalform))])
    somasinternasnormal = sum(normalform)
    somasinternasinvnormalform = sum(invnormalform)
       
    if somasinternasnormal>somasinternasinvnormalform: prima=normalform
    else: prima=invnormalform
        
    fator = 12 - prima[0]
        
    prima = [(prima[x]+fator)%12 for x in range(len(prima))]
    
        
    return(prima)

def root_force(combinatoria):
    
    root_force=[]
    
    for i in range (len(combinatoria)):
        intervalo = abs(combinatoria[i][0]-combinatoria[i][1])%12

        if intervalo == 5 :[root,force]=[combinatoria[i][1],intervalo]
        elif intervalo == 8 :[root,force]=[combinatoria[i][1],(12-intervalo)] 
        elif intervalo == 9 :[root,force]=[combinatoria[i][1],(12-intervalo)]
        elif intervalo == 2 :[root,force]=[combinatoria[i][1],intervalo]
        elif intervalo == 1 :[root,force]=[combinatoria[i][1],intervalo]
        
        elif intervalo == 7 :[root,force] = [combinatoria[i][0],(12-intervalo)]
        elif intervalo == 4 :[root,force] = [combinatoria[i][0],intervalo]
        elif intervalo == 3 :[root,force] = [combinatoria[i][0],intervalo]
        elif intervalo == 10:[root,force] = [combinatoria[i][0],(12-intervalo)]
        elif intervalo == 11:[root,force] = [combinatoria[i][0],(12-intervalo)] 
        
        else: [root,force] = [(0),0]
        
        root_force.append ([root,force])
          
    return root_force

def hindemith (acorde, note_name = True, mostra = True):

    if note_name:
        acorde = [note_to_pitch(note_name) for note_name in acorde]

    listagem = list(combinations(acorde, 2)) #relações binárias intervalares
    intervalos = [(abs(x[1]-x[0]))%12 for x in listagem] #intervalos
    root_force_values = root_force(listagem) #cria lista com roots e forças
    cardinality = len(acorde) #cardinalidade do acorde
    forcemax = max([x[1] for x in root_force_values]) #valor máximo de força
    forces = [x[1] for x in root_force_values]  #tabela de forças
    
    #posições de ocorrencias do valor máximo
    
    ocurrences = []
    
    for i, j in enumerate(forces):
        if j == forcemax:
            ocurrences.append(i)
    
    #verificando que melhor intervalo tem a nota mais grave = essa nota é a fundamental
    
    possible_roots = [root_force_values[x][0] for x in ocurrences]
    
    
    ocurtritone = intervalos.count(6) #quantidade de tritones
    
    root = min(possible_roots) #fundamental
    
    inter = [(acorde[x+1] - acorde[x]) for x in range(len(acorde)-1)]
    
    if prima(acorde)==[0,4,8] or inter == [5,5]:
        tipo = 'V'
        root = 0
        
    elif prima(acorde)==[0,3,6] or prima(acorde)==[0,3,6,9]:
        tipo = 'VI'
        root = 0
            
    else:
        if 6 in intervalos:
            if 1 in intervalos or 11 in intervalos:
                
                if root == acorde[0]: tipo = 'IV.1'
                else: tipo = 'IV.2'
                
            else:
                if (10 in intervalos and 2 not in intervalos) and ocurtritone==1:
                    if root == acorde[0]: tipo = 'IIa'
                    else: tipo = 'IIb.2'
                elif (10 in intervalos or 2 in intervalos) and ocurtritone==1:    
                    if root == acorde[0]: tipo = 'IIb.1'
                    else: tipo = 'IIb.2'
                elif ocurtritone >= 2: tipo = 'IIb.3' 
        else:
            if 1 in intervalos or 2 in intervalos or 10 in intervalos or 11 in intervalos:
                if root == acorde[0]: tipo = 'III.1'
                else: tipo = 'III.2'
            else:
                if root == acorde[0]: tipo = 'I.1'
                else: tipo = 'I.2'
    
    if mostra:
        print ('Sonority =', acorde)
        print ('Relações binárias intervalares =', listagem)
        print ('Intervals =',intervalos)
        print ('Roots e forças =',root_force_values)
        print ('Forças =',forces)
        print ('Cardinalidade =',cardinality)
        print ('Valor máximo =',forcemax)
        
        print ('Posições onde ocorrem o máximo =', ocurrences)
        print ('Fundamentais possíveis =', possible_roots)
        print ('Número de trítonos =', ocurtritone)
        
        print ('Tipo =', tipo, ' Root =',root, ' Baixo =', acorde[0])
        print ('=============================')

    return tipo

def gera_hindemith(tipo, mais_grave, mais_aguda, cardinalidade, tentativas):
    mais_grave_midi = note_to_pitch(mais_grave)
    mais_aguda_midi = note_to_pitch(mais_aguda)

    chords = []

    for _ in range(tentativas):
        random_chord = list(np.random.choice(a = range(mais_grave_midi + 1, mais_aguda_midi + 1), replace = False, size = cardinalidade - 1))
        random_chord.append(mais_grave_midi)
        random_chord.sort()

        tipo_chord = hindemith(random_chord, note_name = False, mostra = False)

        if tipo_chord == tipo:
            chord = [pitch_to_note(note_number) for note_number in random_chord]
            chords.append(chord)
        else:
            continue
      
    print(set([tuple(chord) for chord in chords]))
