import string

class Trie:
    
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
        
        archivoTexto = open(path,"r")
        contenido = archivoTexto.read()
        contSinPuntuacion = contenido.translate(str.maketrans('','',string.punctuation))
        palabras = contSinPuntuacion.split()
        return palabras

def main():
    
    first_trie = Trie()
    flag = True
    while(flag):

        print("""----MENU-----\n
              1.Insertar desde archivo
              2.Buscar Palabra 
              3.Buscar Prefijo
              4.Salir""")

        opcion = int(input("Ingresa la opcion: "))
        if opcion == 1:
            path = input("Ingresa la ruta de archivo (agregar ruta sin comillas\n"
                         "ex. C:\Ejercicios Progra\Estructuras de Datos Avanzadas\\0_palabras.txt\n"
                         "ruta: ")
            palabras_a_insertar = lectura_insercion_archivo(path)
            #print(palabras_a_insertar)
            for palabra in palabras_a_insertar:
                first_trie.add_palabra(palabra)
            print("Palabras en archivo insertadas")
            
        elif opcion == 2:
            palabra = str(input("Palabra a buscar: "))
            if first_trie.search_palabra(palabra):
                print("La palabra {} existe en el trie".format(palabra))
                continue
            print("La palabra {} no existe en el trie".format(palabra))        

        elif opcion == 3:
            prefijo = str(input("Prefijo a buscar: "))
            if first_trie.starts_with(prefijo):
                print("El prefijo {} se encuetnra en el trie".format(prefijo))
                continue
            print("El prefijo {} no se encuentra en el trie".format(prefijo))

        elif opcion == 4:
            flag = False
        
main()    

            
               
        
        