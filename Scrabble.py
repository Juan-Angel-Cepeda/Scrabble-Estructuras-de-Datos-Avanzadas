#SCRABBLE
#INTEGRANTES
#Fecha de Entrega 25/03/22
#a338832 Juan Angel Cepeda Fernandez
#a334144 Eduardo Rodriguez Chaparro
#a330836 Manuel Balderrama Chaparro

#>>>>>>>PROS
#Reparte fichas - Verifica palabras validas - Verifica palabras no repetidas - Verifica palabras con fichas repartidas
#Guarda las palabras, Calcula puntaje, repone fichas, y da el puntaje del jugador
#De 1 a 2 jugadores
#>>>>>>>CONTRAS
#No usamos Heaps
#Las letras en tablero, no pueden ser usadas, ni tampoco hay multiplicadores.

import random
import string

class Palabra: #Clase para las palabras
    def __init__(self,palabra,puntaje):
        self.palabra = palabra
        self.puntaje = puntaje


class TablaHash: #Tabla Hash
    
    def __init__(self,cantidad_de_palabras):
        
        #cantidad de palabras, hay que mandar las palabras en el archivo de texto
        almacenaje = int(cantidad_de_palabras+(cantidad_de_palabras*.2))
        
        self.palabras = [None] * almacenaje
        self.almacenaje = almacenaje
        self.key = None

   
    #hay que pasar Str
    def buscar(self,llave,palabraOriginal):
        if(self.palabras[llave] == None):
            self.palabras[llave] = palabraOriginal
            print("Usted coloco {} en el tablero".format(palabraOriginal))
        else:
            self.palabras[llave] == palabraOriginal
            print("La palabra {} ya se utilizó".format(palabraOriginal))
            
    #Funcion hash
    def hash_funcion(self,palabra:str):
        
        palabraorg = palabra
        key = palabra
        key = list(key)
        suma = 0
        valoresASCII = []
        for i in key:
            valoresASCII.append(ord(i))
        for valor in valoresASCII:
            suma = valor + suma
        key = suma % self.almacenaje
        self.key = key
        self.buscar(key,palabraorg)
          
#Trie
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
    
def lectura_insercion_archivo(path):
        
        archivoTexto = open(path,'r',encoding="utf8")
        contenido = archivoTexto.read()
        contSinPuntuacion = contenido.translate(str.maketrans('','',string.punctuation))
        palabras = contSinPuntuacion.split()
        return palabras

#Creamos nuestra clase jugador
class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0
        self.fichas = [None]*7

#Creamos nuestras clases fichas        
class Fichas():
    def __init__(self):
        #Asignamos el valor a las fichas
        self.fichas = ["a",1,"b",3,"c",3,"d",2,"e",1,"f",4,"g",2,
                       "h",4,"i",1,"j",8,"k",5,"l",1,"m",3,"n",1,
                       "o",1,"p",3,"q",5,"r",1,"s",1,"t",1,"u",1,
                       "v",4,"w",5,"x",8,"y",4,"z",10]

#Creamos la clase tablero
class Tablero():
    #Comprueba el limite de las fichas
    def __init__(self):
        self.tablero = []
        for i in range(16):
            a = [" "]*16
            self.tablero.append(a)
            ++i
      
        self.cantidadesFichas = [12,2,4,5,12,2,3,2,6,1,1,4,2,5,9,2,1,5,6,4,5,1,1,1,1,1]
        #                        A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
        self.arregloFichas= ["a","b","c","d","e","f","g","h","i","j","k",
                      "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    def imprimirTablero(self):
        for i in range(15):
            print(self.tablero[i])
        print(self.cantidadesFichas)
    
    #Funcion que reparte las fichas a los jugadores
    def repartirFichas(self,numeroFichas:int ,jugador:Jugador):
        i = 0
        while(i < numeroFichas):
            x = random.randint(0,25)
            if(self.cantidadesFichas[x]> 0): 
                jugador.fichas[i] = self.arregloFichas[x]
                self.cantidadesFichas[x] = self.cantidadesFichas[x]-1
                i = i+1
            else:
                i = i-1
    #Funcion para poder colocar la palabra en la matriz-tablero
    def colocarPalabraEnTablero(self,palabra,posicion1,posicion2,orientacion):
        longitudPalabra = len(palabra)
        if (orientacion == 1):
            for i in range(0,longitudPalabra):
                self.tablero[posicion1][posicion2 + i] = palabra[i]
        elif(orientacion == 2):
            for i in range(0,longitudPalabra):
                self.tablero[posicion1 + i][posicion2] = palabra[i]
        else:
            print("No le pique a otro numero plox\n")
    #Funcion para reponer fichas usadas
    def reponerFichas(self,jugador:Jugador,palabra):
        letrasUsadas = len(palabra)
        contador = 0   
        for i in range(0,letrasUsadas):
            for j in range(0,6):
                if(palabra[i] == jugador.fichas[j] and contador < letrasUsadas):
                    x = random.randint(0, 24)
                    if(self.cantidadesFichas[x]> 0): 
                        jugador.fichas[j] = self.arregloFichas[x]
                        self.cantidadesFichas[x] = self.cantidadesFichas[x]-1
                        contador = contador+1
                    else:
                        i = i-1
                        continue
        pass
    
#Se crea el jugador           
def crearJugador(nombre:str):
    jugador = Jugador(nombre)
    return jugador

def main():
    
    orientacion = 0 #Variable para orientacion
    #Variables para la posicion en la matris
    posX = 7
    posY = 7
    #Instancias de fichas y tablero
    fichas = Fichas()
    tablero = Tablero()
    #Numero de fichas por jugador
    numeroFichas = 7
    #Una variable de check
    check = False
    revisar_palabras_repetidas = TablaHash(50)
    
    palabras_almacenar = Trie()    
    palabras_a_insertar = lectura_insercion_archivo('C:\Ejercicios Progra\Estructuras de Datos Avanzadas\\0_palabras_todas.txt')
    
    for palabra in palabras_a_insertar:
        palabras_almacenar.add_palabra(palabra)
            
    print("""+++++++++++++++Scrable+++++++++++++\n""")
    
    cantidadDeJugadores = int(input("Ingresa la cantidad de jugadores, hasta 2 jugadores: "))
    
    while(cantidadDeJugadores > 2):
        print("El juego solo es de 1 o 2 jugadores")
        print("Intenta nuevamente")
        cantidadDeJugadores = int(input("Ingresa la cantidad de jugadores, solo 2: "))
        
    jugadores = []*cantidadDeJugadores
    
    for i in range(0,cantidadDeJugadores):
        nuevoJugador = crearJugador(input("Ingresa el nombre del jugador: "))
        jugadores.append(nuevoJugador)
    
    opcion = int(input("Para ingresar el Juego presiona 2.\nPara terminar presiona 11 : "))
    
    jugadas = 2
    turno = 0
    
    while(opcion == 2):
        
        if(jugadas%2 == 0 and len(jugadores) != 1):
            turno = 0
        elif(jugadas%2 != 0 and len(jugadores) != 1):
            turno = 1
        else:
            turno = 0
        
        print("Turno de {}".format(jugadores[turno].nombre))
        tablero.imprimirTablero()
        if(jugadores[turno].puntaje == 0):
            tablero.repartirFichas(numeroFichas, jugadores[turno])
            print("Ingresa la palabra para jugar")
            print("Si desea pasar presione 1.")
            print("Para Terminar Juego Presione 11. ")
            print("Sus fichas son: ",jugadores[turno].fichas)
            palabra = (str(input("""Palabra: """)))
        
        else:
            print("Sus fichas son: ",jugadores[turno].fichas)
            print("Ingresa la palabra para jugar")
            print("Si desea pasar presione 1.")
            print("Si desea cambiar todas las fichas presione 2.")
            print("Para Terminar Juego Presione 11.")
            palabra = (str(input("""Palabra: """)))
        
        if(palabra == "1"):
            #cambia el turno del jugador
            jugadas = jugadas+1
            continue
        elif(palabra == "2"):
            tablero.repartirFichas(numeroFichas, jugadores[turno])
            jugadas = jugadas+1
            continue
        
        elif(palabra == "11"):
            break
        
        else:                
            palabra = list(palabra)
            for i in range(len(palabra)):
                for j in range(0,6):
                    if(palabra[i] == jugadores[turno].fichas[j]):
                        check = True
                        break
                    else:
                        check = False

            for i in range(len(palabra)):
                for j in range(0,52):
                    if(palabra[i] == fichas.fichas[j]):
                        jugadores[turno].puntaje = jugadores[turno].puntaje + fichas.fichas[j+1]
            
        
        if(check == False):
            print("No puede crear su palabra con sus letras\n")
        
        else:   
            #Pedimos que nos indique la orientacion de la palabra ya sea horizontal o vertical
            palabra = ''.join(palabra)    
            if palabras_almacenar.search_palabra(palabra):
                print("La palabra {} es valida para el Juego".format(palabra))
                revisar_palabras_repetidas.hash_funcion(palabra)
                print("Ingresar la posición y orientación para poner la palabra\n")
                print("************ORIENTACIÓN DE LA PALABRA ************")
                print("1. Derecha")
                print("2. Abajo\n")
                print("************POSICIÓN DE LA PALABRA ************")
                #Ingresamos las posiciones
                posX = int(input("Poscición en X: "))
                posY = int(input("Poscición en Y: "))
            
                orientacion = int(input("Ingresar la orientación: "))
                palabra_en_tablero = list(palabra)
                tablero.colocarPalabraEnTablero(palabra_en_tablero,posX,posY,orientacion)
                
                #volvemos a imprimir el tablero
                tablero.imprimirTablero()
                jugadas = jugadas+1
                print("\nEl puntaje de {} es: {}".format(jugadores[turno].nombre,jugadores[turno].puntaje))
                tablero.reponerFichas(jugadores[turno],palabra)
                
            else:
                print("La palabra {} no es valida para el Juego\n".format(palabra))  
                
    #Declaramos el ganador del juego segun el puntaje
    if(jugadores[0].puntaje > jugadores[1].puntaje):
        print("El ganador del juego es: {} con un puntaje de {}".format(jugadores[0].nombre,jugadores[0].puntaje))
    else:
        print("El ganador del juego es: {}".format(jugadores[1].nombre,jugadores[1].puntaje))
            
main()
