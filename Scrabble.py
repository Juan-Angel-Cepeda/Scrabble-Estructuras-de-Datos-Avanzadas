from ast import Str
import random
import string
from typing import List


class TablaHash:
    
    def __init__(self,cantidad_de_palabras):
        
        #cantidad de palabras, hay que mandar las palabras en el archivo de texto
        almacenaje = int(cantidad_de_palabras+(cantidad_de_palabras*.2))
        
        self.palabras = [None] * almacenaje
        self.almacenaje = almacenaje
        self.key = None

    #Funcion hash
    #hay que pasar Str
    def buscar(self,llave,palabraOriginal):
        if(self.palabras[llave] == None):
            self.palabras[llave] = palabraOriginal
            print("Usted coloco {} en el tablero".format(palabraOriginal))
        else:
            self.palabras[llave] == palabraOriginal
            print("La palabra {} ya se utilizó".format(palabraOriginal))
            
    
    def hash_funcion(self,palabra:Str):
        
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

#Creamos nuestra clase jugador
class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = None
        self.fichas = [None]*7

#Creamos nuestras clases fichas        
class Fichas():
    def __init__(self):
        #Asignamos el valor a las fichas
        self.fichas = {"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,
                       "h":4,"i":1,"j":8,"k":5,"l":1,"m":3,"n":1,
                       "o":1,"p":3,"q":5,"r":1,"s":1,"t":1,"u":1,
                       "v":4,"w":5,"x":8,"y":4,"z":10}

#Creamos la clase tablero
class Tablero():
    #Comprueba el limite de las fichas
    def __init__(self):
        self.tablero = []
        for i in range(15):
            a = [" "]*15
            self.tablero.append(a)
            ++i      
    
    def imprimirTablero(self):
        for i in range(15):
            print(self.tablero[i])
    
    #Funcion que reparte las fichas a los jugadores
    def repartirFichas(self,numeroFichas:int ,jugador:Jugador):
        
        #CUANTAS FICHAS HAY 
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
    
    def colocarPalabraEnTablero(self,palabra,posicion1,posicion2,orientacion):
        longitudPalabra = len(palabra)
        if (orientacion == 1):
            for i in range(0,longitudPalabra):
                self.tablero[posicion1][posicion2 + i] = palabra[i]
        elif(orientacion == 2):
            for i in range(0,longitudPalabra):
                self.tablero[posicion1 + i][posicion2] = palabra[i]
        else:
            print("No le pique a otro numero no se IDIOTA\n")
                
def main():
    
    orientacion = 0
    posX = 7
    posY = 7
    flag = True
    fichas = Fichas()
    tablero = Tablero()
    numeroFichas = 7
    check = False
    revisar_palabras_repetidas = TablaHash(50)
    
    palabras_almacenar = Trie()    
    palabras_a_insertar = lectura_insercion_archivo('C:\Ejercicios Progra\Estructuras de Datos Avanzadas\\0_palabras.txt')
    
    for palabra in palabras_a_insertar:
        palabras_almacenar.add_palabra(palabra)
            
    print("""+++++++++++++++Scrable+++++++++++++\n""")
    
    
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
            tablero.imprimirTablero()
            tablero.repartirFichas(numeroFichas,jugador1)
            print("Sus fichas son: ",jugador1.fichas)
            print("Ingresa la palabra para jugar")
            print("Si desea pasar presione 1.")
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
                palabra = ''.join(palabra)
                
                if palabras_almacenar.search_palabra(palabra):
                    print("La palabra {} es valida para el Juego".format(palabra))
                    revisar_palabras_repetidas.hash_funcion(palabra)
                    print("Ingresar la posición y orientación para poner la palabra\n")
                    print("************ORIENTACIÓN DE LA PALABRA ************")
                    print("1. Derecha")
                    print("2. Abajo\n")
                    print("************POSICIÓN DE LA PALABRA ************")
                    posX = int(input("Poscición en X: "))
                    posY = int(input("Poscición en Y: "))
                    
                    orientacion = int(input("Ingresar la orientación: "))
                    palabra_en_tablero = list(palabra)
                    tablero.colocarPalabraEnTablero(palabra_en_tablero,posX,posY,orientacion)
                    tablero.imprimirTablero()
                    
                else:
                    print("La palabra {} no es valida para el Juego".format(palabra))  
                
            #tablero.imprimirTablero()
            
        elif(opcion == 11):
            flag = False
        
    
main()
