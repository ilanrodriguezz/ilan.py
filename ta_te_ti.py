from random import randint

tablero=[["1","2","3"],["4","X","6"],["7","8","9"]]

marco_horizontal = 13

def victory():
    #Primer control de filas
    for i in range(3):
        if tablero[i][0] == "X" and tablero[i][1] == "X" and tablero[i][2] == "X":
            return "X"
        if tablero[i][0] == "O" and tablero[i][1] == "O" and tablero[i][2] == "O":
            return "O"
        #Control de columnas
        if tablero[0][i] == "X" and tablero[1][i] == "X" and tablero[2][i] == "X":
            return "X"
        if tablero[0][i] == "O" and tablero[1][i] == "O" and tablero[2][i] == "O":
            return "O"
    #Control de cruces
    if tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X":
        return "X"
    elif tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O":
        return "O"
    elif tablero[0][2] == "X" and tablero[1][1] == "X" and tablero[2][0] == "X":
        return "X"
    elif tablero[0][2] == "O" and tablero[1][1] == "O" and tablero[2][0] == "O":
        return "O"
    #Control de empate
   
    '''for j in range(1, 10):
        if j not in tablero:
            return 0
        #En consecuencia lógica, el juego continua:
        else:
            return 1'''

def presentar_tablero():
    print("\n")
    print("-" * marco_horizontal)
    print(tablero[0][0]," | ", tablero[0][1]," | ",tablero[0][2])
    print("-" * marco_horizontal)
    print(tablero[1][0]," | ",tablero[1][1]," | ",tablero[1][2])
    print("-" * marco_horizontal)
    print(tablero[2][0]," | ",tablero[2][1]," | ",tablero[2][2])
    print("-" * marco_horizontal)
    print("\n")
   
def MakeListOfFreeFields(tablero):
    libres=[]
    for row in range(3):
        for col in range(3):
            if tablero[row][col] != "X":
                if tablero[row][col] != "O":
                    libres.append(tablero[row][col])
    return libres
   
def entermove(jugada):
   
    libres=MakeListOfFreeFields(tablero)
    print("Posiciones libres: ", libres)
   
    if str(jugada) in libres:
        if jugada >=1 and jugada <10:
            jugada = jugada - 1
            fila = jugada  // 3
            col = jugada % 3
            tablero[fila][col] = "O"
            return False
    else:
        return True
   
def pc_move():
    libres=MakeListOfFreeFields(tablero)
    play_pc = randint(1,9)
    while str(play_pc) not in libres:
        play_pc = randint(1,9)  
    if play_pc >=1 and play_pc <10:
            play_pc = play_pc - 1
            fila = play_pc  // 3
            col = play_pc % 3
            tablero[fila][col] = "X"
    return None

print("******************************************************")
print("*           TA TE TI    SUERTE PARA MI               *")
print("******************************************************")

libres = MakeListOfFreeFields(tablero)
tam_libres = len(libres)

while tam_libres != 0:    
    print(presentar_tablero())
   
    # juega el humano
    jugada = int(input("Ingrese movimiento: "))
    while entermove(jugada):
        print("Posición ocupada, ingrese una diferente ..")
        jugada = int(input("Ingrese movimiento: "))

    # Verificar si hay ganador
    if victory() == 'O':
        print("Felicitaciones GANASTE !!!!!")
        break
   
    #juega la pc
    pc_move()
    # Verificar si gano la PC
    if victory() == 'X':
        print("GANO LA PC :-( ")
        break
   
    libres = MakeListOfFreeFields(tablero)
    tam_libres = len(libres)

if tam_libres == 0:
    print("Empate ....")
   
print(presentar_tablero())
