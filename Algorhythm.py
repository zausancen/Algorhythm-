#Programa que indica la tonalidad en la que estas mediante los grados armónicos (mayor)  
def degrees(list):
    return dict(zip(list, degree))

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
degree  =['I','IIm','IIIm','IV','V','VIm','VIIdim']

scale_super_list = []

scales = [C,CS,D,DS,E,F,FS,G,GS,A,AS,B]

for scale in scales:
    scale_super_list.append(degrees(scale))

    
chords = []
amount = input("How many chords does your progression have?:")


try:
    int(amount)
    pass
except ValueError:
    print("Please enter a integer number")
    exit() 
    
    
for i in range (1, int(amount) + 1) :
    chord = input(f"Enter the chord {i}: ")
    chords.append(chord)

answers = []
without_repeats = []

for scale in scale_super_list:
    for keys in scale:
        for chord in chords:
            if keys == chord:
                answers.append(scale)
                break
            
            
for answer in answers:
    if answer not in without_repeats:
        without_repeats.append(answer)


for elements in without_repeats:
    print(f'Match with: {elements}')

