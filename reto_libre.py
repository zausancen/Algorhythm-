#Programa que indica la tonalidad en la que estas mediante los grados armónicos (mayor)  

C     =['C','Dm','Em','F','G','Am','Bm7b5']
CS    =['C#','D#m','Fm','F#','G#','A#m','Cm7b5']
D     =['D','Em','F#m','G','A','Bm','C#m7b5']
DS    =['D#','Fm','Gm','G#','A#','Cm','Dm7b5']
E     =['E','F#m','G#m','A','B','C#m','D#m7b5']
F     =['F','Gm','Am','A#','C','Dm','Em7b5']
FS    =['F#','G#m','A#m','B','C#','D#m','Fm7b5']
G     =['G','Am','Bm','C','D','Em','F#m7b5']
GS    =['G#','A#m','Cm','C#','D#','Fm','Gm7b5']
A     =['A','Bm','C#m','D','E','F#m','G#m7b5']
AS    =['A#','Cm','Dm','D#','F','Gm','Am7b5']
B     =['B','C#m','D#m','E','F#','G#m','A#m7b5']
rank  =['I','IIm','IIIm','IV','V','VIm','VIIdim']

escale_list_super = []

Escalas = [C,CS,D,DS,E,F,FS,G,GS,A,AS,B]

def grados(list):
    return dict(zip(list, rank))

for escala in Escalas:
    escale_list_super.append(grados(escala))
    
# print(escale_list_super)
chords = []

amount = input("Cuantos acordes tiene tu progresión? :")

try:
    int(amount)
    pass
except ValueError:
    print("Ingresa por favor un numero entero")
    exit() 
    

for i in range (1, int(amount) + 1) :
    chord = input(f"Ingresa el acorde {i}: ")
    chords.append(chord)

respuesta = []

for escale in escale_list_super:
    for keys in escale:
        for chord in chords:
            if keys == chord:
                # print(escale.keys())
                respuesta.append(escale.keys())
                break
#print(type(respuesta) )
print(respuesta)


#ls = list(dict.fromkeys(respuesta))
#print(ls)
                
    #             respuesta = respuesta.append(escale.keys())
    #         else:
    #             pass 
    # print(escale.values())    



# percent = float(count/len(C))*100
# print(f"Las coincidencias con la escala {C} son de {percent}%")
