import random
import string

class Trie():
    
    def __init__(self):
        self.raiz = {"*":"*"}
    
    def add_palabra(self,palabra):
        nodo_actual = self.raiz
        
        for letra in palabra:
            if letra not in nodo_actual:
               nodo_actual[letra] = {}
            nodo_actual = nodo_actual[letra]
        nodo_actual["*"] = "*"
    
    def search_palabra(self,palabra):
        nodo_actual = self.raiz
        for letra in palabra:
            if letra not in nodo_actual:
                return False
            nodo_actual = nodo_actual[letra]
        
        return "*" in nodo_actual
    
    def starts_with(self,prefix):
        nodo_actual = self.raiz
        for letra in prefix:
            if letra not in nodo_actual:
                return False
            nodo_actual = nodo_actual[letra]
        return True

def lectura_insercion_archivo(path):
        
        archivoTexto = open(path,'r')
        contenido = archivoTexto.read()
        contSinPuntuacion = contenido.translate(str.maketrans('','',string.punctuation))
        palabras = contSinPuntuacion.split()
        return palabras

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = None
        self.fichas = [None]*7
            
class Fichas():
    def __init__(self):
        #Asignamos el valor a las fichas
        self.fichas = {"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,
                       "h":4,"i":1,"j":8,"k":5,"l":1,"m":3,"n":1,
                       "o":1,"p":3,"q":5,"r":1,"s":1,"t":1,"u":1,
                       "v":4,"w":5,"x":8,"y":4,"z":10}

class Tablero():
    #Comprueba el limite de las fichas
    def __init__(self):
        self.tablero = ["+"]
        for i in range(15):
            a = ["+"]*15
            self.tablero.append(a)
            ++i  
        print(self.tablero)
        #self.imprimirTablero()
    
    #Funcion que reparte las fichas a los jugadores
    def repartirFichas(self,numeroFichas:int ,jugador:Jugador):
        
        #CUANTAS FICHAS HAY PRRIN
        cantidadesFichas = [12,2,4,5,12,2,3,2,6,1,1,4,2,5,9,2,1,5,6,4,5,1,1,1,1]
        #                   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
        arregloFichas= ["a","b","c","d","e","f","g","h","i","j","k",
                      "l","m","n","o","p","q","r","s","t","v","w","x","y","z"]
        
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
    fichas = Fichas()
    tablero = Tablero()
    numeroFichas = 7
    check = False
    
    palabras_almacenar = Trie()    
    palabras_a_insertar = lectura_insercion_archivo('C:\Ejercicios Progra\Estructuras de Datos Avanzadas\\0_palabras.txt')
    
    for palabra in palabras_a_insertar:
        palabras_almacenar.add_palabra(palabra)
            
    print("""++++++Scrable+++++++\n""")
    
    while(flag):
        
        print("1. Ingresar Jugador")
        print("2. Comenzar Juego")
        opcion = (int(input("Ingresa opcion: ")))
        if(opcion == 1):
            nombreJugador = input("Ingresar el nombre del jugador: ")
            jugador1 = Jugador(nombreJugador)
            continue
        
        elif(opcion == 2):
            
            #tablero.repartirFichas(numeroFichas,jugador1)
            tablero.repartirFichas(numeroFichas,jugador1)
            print("Sus fichas son: ",jugador1.fichas)
            print("Ingresa la palabra para jugar")
            print("So desea pasar presione 1.")
            palabra = (str(input("""Palabra: """)))
            
            palabra = list(palabra)
            
            if(palabra != "1"):                
                for i in range(len(palabra)):
                    for j in range(0,7):
                        if(palabra[i] == jugador1.fichas[j]):
                            check = True
                            break
                        else:
                            check = False
            
            if(check == False):
                print("No puede crear su palabra con sus letras")
            
            else:
                print("BIEN :)")
                palabra = ''.join(palabra)
                
                if palabras_almacenar.search_palabra(palabra):
                    print("La palabra {} es valida para el Juego".format(palabra))
                else:
                    print("La palabra {} no es valida para el Juego".format(palabra))  
                
            #tablero.imprimirTablero()
            
            
            
        elif(opcion == 11):
            flag = False
        
    
main()
