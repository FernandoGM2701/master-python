"""
Ejercicio 8. ¿Cuánto es el X por ciento de X número?
             20% de 150
"""

numero = int(input("Ingrese el número por favor: "))
porcentaje = int(input("Ingrese la cantidad de porcentaje: "))

resultado = int((porcentaje / 100) * numero)

print(f"El {porcentaje} % de {numero} es: {resultado} %")

