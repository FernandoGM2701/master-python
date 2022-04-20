"""
Ejercicio 3. Escribir un programa que muestre los cuadrados, de los 60 primeros números naturales

con for y con while


"""

contador = 0
producto = 0

numero = input("Ingrese el número máximo: ")

print("**************CON FOR**************")

for contador in range(0,int(numero)+1):
    producto = contador*contador
    print(f"El cuadrado de {contador} es igual a: {producto}")

print("**************CON WHILE**************")

contador_while = 0
while contador_while <= int(numero):
    producto = contador_while*contador_while
    print(f"El cuadrado de {contador_while} es igual a: {producto}")
    contador_while = contador_while + 1
