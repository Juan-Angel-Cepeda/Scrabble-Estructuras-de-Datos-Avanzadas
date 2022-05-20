import random

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = None
        self.fichas = [None]*7
            
class Fichas():
    def __init__(self):
        #da valor a las fichas
        self.fichas = {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,
                       "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
                       "O":1,"P":3,"Q":5,"R":1,"S":1,"T":1,"U":1,
                       "V":4,"W":5,"X":8,"Y":4,"Z":10}

class Tablero():
    #reparte fichas, compruebael limite de las fichas
    def __init__(self):
        self.tablero = ["+"]
    
    def crearTablero(self):
        for i in range(15):
            a = ["+"]*15
            self.tablero.append(a)
            ++i  
    
    def repartirFichas(numeroFichas:int ,jugador:Jugador):
        cantidadesFichas = [12,2,4,5,12,2,3,2,6,1,1,4,2,5,9,2,1,5,6,4,5,1,1,1,1]
        #                    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
        arregloFichas= ["A","B","C","D","E","F","G","H","I","J","K",
                      "L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"]
        
        for i in range(0,numeroFichas):
            x = random.randint(0, 24)
            
            if(cantidadesFichas[x]> 0): 
                jugador.fichas[i] = arregloFichas[x]
                cantidadesFichas[x] = cantidadesFichas[x]-1
            else:
                --i
                continue
    
    def imprimirTablero(self):
        for i in range(0,14):
                for j in range(0,14):
                    print(self.tablero[i][j])
                    print("\n")
                    ++j
                ++i     
    
def main():
    
    flag = True
    fichas = Fichas
    tablero = Tablero
    numeroFichas = 7
    
    print("""++++++Scrable+++++++\n""")
    
    while(flag):
        
        opcion = int(input("""1. Ingresar Jugador
                              2. Iniciar Juego
                              ingresa opcion: 
                            """)) 
        if(opcion == 1):
            nombreJugador = input("Ingresar el nombre del jugador: ")
            jugador1 = Jugador(nombreJugador)
            continue
        elif(opcion == 2):
            
            tablero.repartirFichas(numeroFichas,jugador1)
            print(jugador1.fichas)
            tablero.crearTablero
            tablero.imprimirTablero
            
                    
        
        elif(opcion == 11):
            flag = False
            
main()        

        
    
    