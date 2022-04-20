"""
Ejercicio 7. Hacer un programa que muestre todos los números impares
entre dos números que decida el usuario

"""

n1 = int(input("Escriba el primer número: "))
n2 = int(input("Escriba el segundo número: "))


for contador in range(n1+1,n2):
    if (contador%2 != 0):
        print(f"El número es : {contador}")

