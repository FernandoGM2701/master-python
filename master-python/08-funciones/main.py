"""
FUNCIONES: 
Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocando a la función tantas veces como sea necesario.

def nombreFuncion(parámetros)
    # BLOQUE / CONJUNTOS DE INSTRUCCIONES


Invocarla:    nombreFuncion(mi_parametro)    
"""

# Ejemplo 1
print("###### EJEMPLO 1 #######")

# Definir función
def muestraNombre():
    print("Fernando")
    print("Alberto")

#Incovar Función
muestraNombre()


#Ejemplo 2
print("###### EJEMPLO 2 #######")

def mostrarNombre(nombre, edad):
    print(f"Tu nombres es: {nombre}")

    if(edad >= 18):
        print(f"Y tu edad es: {edad}")


nombreI = input("Escriba su nombre: ")
edadI = int(input("Escriba su edad: "))
mostrarNombre(nombreI, edadI)

#Ejemplo 3
print("###### EJEMPLO 3 #######")
def tablaMultiplicar(n):
    for contador in range(1,11):
        print(f"{n} X {contador} = {n*contador}")


numero = int(input("Escriba el número de la tabla de multiplicar que quiera: "))
tablaMultiplicar(numero)
