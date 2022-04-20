"""
Ejercicio 2.
    - Escribir un script que nos muestre por pantalla todos los número pares del 1 al 120
"""

ccontador = 1

for contador in range (0,121):
    if contador%2 == 0:
        print(contador)