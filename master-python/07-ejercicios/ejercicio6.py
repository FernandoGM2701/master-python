"""
Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10
Mostrando el título de la tabla y luego las multiplicaciones del 1 al 10

"""

#numero = int(input("Ingrese el número del que desee la tabla de mul"))



for contador in range (1,11):
    print(f"******TABLA DE MULTIPLICAR DEL {contador}******")    
    for producto in range (1,11):
        print(f"{contador} X {producto} = {contador*producto}")
    
