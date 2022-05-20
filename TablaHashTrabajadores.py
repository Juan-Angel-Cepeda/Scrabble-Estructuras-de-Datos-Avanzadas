#colisones en metdo cuadratico
class Trabajador:
    
    def __init__(self,RFC,nombre,salario):
        self.RFC = RFC
        self.nombre = nombre
        self.salario = salario
        self.key = None
        
  
class TablaHash(Trabajador):
    
    def __init__(self,cantidad_de_trabajadores):
        
        almacenaje = int(cantidad_de_trabajadores+(cantidad_de_trabajadores*.2))
        
        self.trabajadores = [None]* almacenaje
        self.almacenaje = almacenaje
    
    def hash_funcion(self,trabajador):
        
        suma = 0
        key = trabajador.RFC
        key = key[-3:]
        valoresASCII = []
        for i in key:
            valoresASCII.append(ord(i))
        for valor in valoresASCII:
            suma = valor + suma
        
        key = suma % self.almacenaje    
        
        trabajador.key = key
        return key
    
    def buscar(self,key):
        if self.trabajadores[key] == None:
            print("No hay trabajador con esta llave")
        else:
            print("El trabajador de nombre {}, con RFC: {} obtiene un salario de {}".format(
                self.trabajadores[key].nombre, self.trabajadores[key].RFC, self.trabajadores[key].salario))

    
    def eliminar(self,key):
        
        if self.trabajadores[key] != None:
            print("El trabajador {} se eliminará. ".format(self.trabajadores[key].nombre))
            self.trabajadores[key] = None
            print("Trabajador Eliminado")
        else:
            print("HECHO")
            
    
    def insertar(self,trabajador):
        Flag = True
        
        while(Flag):
            if self.trabajadores[trabajador.key] == None:
                self.trabajadores[trabajador.key] = trabajador
                Flag = False
            else:
                trabajador.key = pow(trabajador.key,2)
                trabajador.key = trabajador.key % self.almacenaje
            
                    
def main():
    
    Flag = True
    print("""TABLA HASH PARA TRABAJADORES\n""")
    cantidad_de_trabajadores = int(input("Cuantos trabajadores se va a almacenar: "))
    tabla_Principal = TablaHash(cantidad_de_trabajadores)
    
    while(Flag):
        print("""1. Ingresar un trabajador
                 2. Buscar Un trabajador
                 3. Eliminar un trabajador
                 4. Imprimir trabajadores
                 5. Salir\n""")

        opc = int(input("Ingresa una opcion: "))
        
        if opc == 1:
            
            for i in range(0,cantidad_de_trabajadores):
                nombre = str(input("Ingresa el nombre del trabajador: "))
                RFC = str(input("Ingresa el RFC del trabajador: "))
                salario = str(input("Ingresa el salario del trabajador: "))
                trabajadorActual = Trabajador(RFC,nombre,salario)
                tabla_Principal.hash_funcion(trabajadorActual)
                tabla_Principal.insertar(trabajadorActual)
                print("El trabajador ha sido registrado bajo la llave: ",trabajadorActual.key)
                salida = int(input("Presiona 2 para salir\n 1. Para continuar"))
                if (salida == 2):
                    break
                continue

        elif opc == 2:
            trabajador_a_buscar = int(input("Ingresa la llave del trabajador: "))
            tabla_Principal.buscar(trabajador_a_buscar)

        elif opc == 3:
            trabajador_a_eliminar = int(input("Ingresa la llave del trabajador: "))
            tabla_Principal.eliminar(trabajador_a_eliminar)
        
        elif opc == 4:
            for i in range(0,cantidad_de_trabajadores):
                if(tabla_Principal.trabajadores[i] == None):
                    continue
                else:
                    print("""Trabajadores
                          Nombre:{}
                          RFC: {}
                          Salario: {} """.format(tabla_Principal.trabajadores[i].nombre,
                                                 tabla_Principal.trabajadores[i].RFC,
                                                 tabla_Principal.trabajadores[i].salario))
        elif opc == 5:
            Flag = False

main()



