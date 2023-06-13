import networkx as nx
import matplotlib.pyplot as plt


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print("Nombre:", self.nombre)
    
    def moverse(self):
        print("El animal se mueve.")


class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero amamanta a sus crías.")


class Ave(Animal):
    def volar(self):
        print("El ave puede volar.")


class Perro(Mamifero):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def ladrar(self):
        print("El perro ladra.")
    
    def mostrar_raza(self):
        print("Raza:", self.raza)


class Aguila(Ave):
    def __init__(self, nombre, especie):
        super().__init__(nombre)
        self.especie = especie
    
    def cazar(self):
        print("El águila puede cazar presas en vuelo.")
    
    def mostrar_especie(self):
        print("Especie:", self.especie)
        
perro = Perro("Fido", "Labrador")
perro.mostrar_nombre()
perro.mostrar_raza()
perro.ladrar()
perro.moverse()
perro.amamantar()  # Heredado de la clase Mamifero

aguila = Aguila("Aguilucho", "Águila Real")
aguila.mostrar_nombre()
aguila.mostrar_especie()
aguila.volar()
aguila.moverse()
aguila.cazar()  # Heredado de la clase Ave

