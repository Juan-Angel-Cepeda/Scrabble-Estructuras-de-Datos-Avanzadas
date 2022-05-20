class MaxHeap:
    
    def __init__(self,capacidad):
        self.almacenamiento = [{0:"Nombre"}]*capacidad
        self.capacidad = capacidad
        self.tamaño = 0
    
    def getIndiceDelPadre(self,indice):
        return (indice-1)//2
    
    def getIndiceHijoIzquierdo(self,indice):
        return 2*indice+1
    
    def getIndiceHijoDerecho(self,indice):
        return 2*indice+2
    
    def tienePadre(self,indice):
        return self.getIndiceDelPadre(indice) >= 0
    
    def tieneHijoIzquierdo(self,indice):
        return self.getIndiceHijoIzquierdo(indice) < self.tamaño
    
    def tieneHijoDerecho(self, indice):
        return self.getIndiceHijoDerecho(indice) < self.tamaño
    
    def padre(self,indice):
        return self.almacenamiento[self.getIndiceDelPadre(indice)]
    
    def hijoIzquierdo(self,indice):
        return self.almacenamiento[self.getIndiceHijoIzquierdo(indice)]
    
    def hijoDerecho(self,indice):
        return self.almacenamiento[self.getIndiceHijoDerecho(indice)]
    
    def estaLleno(self):
        return self.tamaño == self.capacidad
    
    def cambio(self,indice1,indice2):
        
        auxiliar = self.almacenamiento[indice1]
        self.almacenamiento[indice1] = self.almacenamiento[indice2]
        self.almacenamiento[indice2] = auxiliar
    
    def incrementarHeap(self,indice):
        
        if self.tienePadre(indice) and self.padre(indice) < self.almacenamiento[indice]:
            self.cambio(self.getIndiceDelPadre(indice),indice)
            self.incrementarHeap(self.getIndiceDelPadre(indice))
    
    def decrementarHeap(self,indice):
        
        Maximo = indice
        if (self.tieneHijoIzquierdo(indice) and self.almacenamiento[Maximo] < self.hijoIzquierdo(indice)):
            Maximo = self.getIndiceHijoIzquierdo(indice)
        if (self.tieneHijoDerecho(indice) and self.almacenamiento[Maximo] < self.hijoDerecho(indice)):
            Maximo = self.getIndiceHijoDerecho(indice)
        if (Maximo != indice):
            self.cambio(indice,Maximo)
            self.decrementarHeap(Maximo)
            
    def insertar(self, data ,nombre):
        
        if(self.estaLleno()):
            raise("El arreglo del Heap está lleno")
        self.almacenamiento[self.tamaño] = {data:nombre}
        self.tamaño += 1
        self.incrementarHeap(self.tamaño-1)
    
    def eliminarMaximo(self):
        if(self.tamaño == 0):
            raise("Heap vacio")
        data = self.almacenamiento[0]
        self.almacenamiento[0] = self.almacenamiento[self.tamaño -1]
        self.tamaño -=1 
        self.decrementarHeap(0)
        return data
    
    """def getMaximo(self):
        maximo = max(self.almacenamiento)
        return maximo"""
            
hospital = MaxHeap(20)
hospital.insertar(5,"angel")
hospital.insertar(12,"pedro")
hospital.insertar(19,"fuers")
hospital.insertar(40,"eliot")
#print(hospital.getMaximo())
hospital.insertar(18,"master")

hospital.eliminarMaximo()


#flag = True
#opcion = 1
#salaDeHospital = MaxHeap(20)
#while(flag):
#    print("""Bienvendio a la sala de hospial
#          La sala solo tiene espacio para 20 pacientes
#          1. Ingresar Pacientes
#          2. Mostrar siguiente paciente
#          3. Atender paciente
#          4. Abandonar sistema
#          5. Lista de pacientes""")
#    opcion = int(input("Ingresa tu opcion: "))
#    codigo_de_emergencia = (int(input("Ingresar prioridad entre más bajo, mayor prioridad: ")))
#    if opcion == 1:
#        salaDeHospital.insertar(codigo_de_emergencia)
#    
#    elif opcion == 2:
#        print(salaDeHospital.minimo)
#    
#    elif opcion == 3:
#        salaDeHospital.eliminarMinimo()
#        print("Paciente Atendido")        
#    elif opcion == 4:
#        flag = False
#    elif opcion == 5:
#        print(salaDeHospital.almacenamiento)
        
        
        
    
    
            