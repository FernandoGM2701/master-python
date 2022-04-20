"""
Ejercicio 9. Hacer un programa que pida números al usuario indefinidamente
hasta meter el número 111

"""

numero = int(input("Ingrese el número:"))

while numero != 111 :
    input(f"El número es: {numero}")
    numero = int(input("Ingrese nuevamente el número:"))


