#word = list[randint]
#Len of word to print the empty "_" spaces.
#Check letra = A in Word
    #If letter IN word:
        #identificar donde aparece y reemplazar en el espacio correcto
    #else:
        #agregar letra a lista intentos = []
#if len(tries) == 6:
    #Game over
    #Print word
#if lista intentos no tiene mas "_"'s, Win!

from random import randint
intentos = 6
listaguess = []
letras = []
sorteo = 0
palabrajuego = 0
win = False

def dificultad():
    try:
        num = int(input("Elegir dificultad:\n1 - Fácil\n2 - Medio\n3 - Difícil\n"))
        if num == 1:
            return lista_facil
        elif num == 2:
            return lista_medio
        elif num == 3:
            return lista_dificil
        else:
            return dificultad()
    except ValueError:
        return dificultad()

def tablero(tries):
    print("  +---+", "  |   |", sep="\n")
    if tries == 6:
        print("  |", "  |", "  |", sep="\n")
    elif tries == 5:
        print("  |  👀", "  |", "  |", sep="\n")
    elif tries == 4:
        print("  |  😐", "  |   |", "  |", sep="\n")
    elif tries == 3:
        print("  |  😟", "  |  /|", "  |", sep="\n")
    elif tries == 2:
        print("  |  😲", "  |  /|\\", "  |", sep="\n")
    elif tries == 1:
        print("  |  😨", "  |  /|\\", "  |  /", sep="\n")
    print("  |", "==========", sep="\n")
    print("         [  ", end="")
    for x in range(len(listaguess)): print(f" {listaguess[x]} ", end="")
    print("  ]  ", len(listaguess))
    #print(difficulty[sorteo]) #DEBUGGING
    if letras != 0: print(f"Intentadas: {sorted(letras)}")
    print(f"Intentos restantes: {intentos}")
    return None

def adivinar():
    guess = input("Creo que tiene: ")
    guess = guess.lower()
    if len(guess) < 1 or guess in letras:
        return adivinar()
    elif len(guess) == 1:
        if guess not in palabrajuego:
            letras.insert(0, guess)
            return False
        else:
            for j in range(len(palabrajuego)):
                if palabrajuego[j] == guess:
                    listaguess[j] = guess 
            return None
    elif len(guess) > 1:
        letras.insert(0, guess)
        #if guess == difficulty[sorteo]:
        palabratemp = ''.join(palabrajuego)
        if guess == palabratemp:
            return True
        else:
            return False

#### listas
lista_facil = ["pasta", "hora", "television", "musica", "barco", "humano", "hermano", "suave", "programacion", "deporte", "universo", "dragon", "teclado", "libro", 
               "bandera", "libertad", "pelota", "celular", "telefono", "pelicula", "profesor", "religion", "politica", "economia", "naranja"]
lista_medio = ["computadora", "personaje", "submarino", "lluvia", "llavero", "rey", "tragedia", "crayon", "agudo", "fisico", "astronomo", "miembro", "membrillo", 
               "nervio", "pantorrilla", "triple", "boveda", "orquidea", "brujula", "bruja", "cobayo", "quimica", "quimera", "milpies", "monitor"]
lista_dificil = ["camuflaje", "grafiti", "conducta", "dosis", "gen", "juvenil", "clima", "ritmo", "raza", "claroscuro", "trufa", "trompo", "hilo", "burbuja", "chutar", 
                 "chip", "eonia", "trol", "wok", "grisin", "hule", "taxon", "tren", "usufructo", "blusa"]
imposible = ["Jazz"]

#### dificultad ####
difficulty = dificultad() #Funcion dificultad devuelve la lista (o variable) correspondiente
sorteo = randint(0,24)
palabrajuego = list(difficulty[sorteo])
for i in palabrajuego:
    listaguess.append("_")

#### presentar ####
while intentos != 0 and win != True:
    tablero(intentos) #intentos es necesario como argumento para mostrar el monigote correcto

#### intento ####
    win = adivinar()

#### victoria? ####
    if listaguess == palabrajuego or win == True: 
        break
    elif win == None:
        continue
    else:
        intentos -= 1
        continue

if intentos != 0:
    print("  +---+", "  |   |", sep="\n")
    print("  |", "  |    😎", "  |    /|\\", sep="\n")
    print("  |    / \\", "==========", sep="\n")
    print(f"¡Felicitaciones! Adivinaste la palabra {''.join(palabrajuego)} con {intentos} vida(s) restantes.")
elif intentos == 0:
    print("  +---+", "  |   |", sep="\n")
    print("  |  😞 👻", "  |  /|\\", "  |  / \\", sep="\n")
    print("  |", "==========", sep="\n")
    print(f"Mala suerte. La palabra era {''.join(palabrajuego)}\n¡Mejor suerte la próxima!")
else:
    print("No sé cómo terminaste acá, pero ¿querés jugar un Ta-te-ti?") #Si alguien logra que aparezca esta línea sin modificar el código, díganme cómo hicieron.

#debugging
#print(sorteo)
#print(palabrajuego)
