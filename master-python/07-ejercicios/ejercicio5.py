"""
Ejercicio 5. Hacer un programa que muestre todos los número entre dos números que diga el usuario

"""

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))


contador = 0

if (n1 > n2):
    for contador in range(n2+1,n1):
        print(f"Los números entre {n2} y {n1} son: {contador}")
else:
    for contador in range(n1+1,n2):
        print(f"Los números entre {n1} y {n2} son: {contador}")       