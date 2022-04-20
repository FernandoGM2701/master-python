"""
Ejercicio 4. Pedir dos números al usuario y hacer todas las operaciones básicas de una 
calculadora y mostrarlo por pantalla

"""

n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")

suma = int(n1) +  int(n2)
if int(n1) > int(n2):
    resta = int(n1) - int(n2)
    if int(n2) != 0:
        division = int(n1) / int(n2)
    else: 
        print("Ingrese un número diferente de cero")    
else:
    resta = int(n2) - int(n1)  
    if int(n1) != 0:
        division = int(n2) / int(n1)
    else: 
        print("Ingrese un número diferente de cero")    


multiplicacion = int(n1) * int(n2)

print("********C A L C U L A D O R A**********")
print(f"La suma del número {n1} y el número {n2} es: {suma}")
print(f"La resta del número {n1} y el número {n2} es: {resta}")
print(f"La multiplicación del número {n1} y el número {n2} es: {multiplicacion}")
print(f"La división del número {n1} y el número {n2} es: {division}")