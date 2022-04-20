
nada = None
nombre_de_la_variable = "Fernando"

#mostrar tipo de dato
print(nada)
print(type(nada))

print("*****************")

print(nombre_de_la_variable)
print(type(nombre_de_la_variable))


entero = 99
flotante = 4.2
booleano = True
#la variable lista es como un array o como arreglo o matriz, 
#básicamente una lista es una colección de muchas variables (datos)
lista = [5, 10]

#tupla es lista que no cambia
tupla = ("fernando", 21)

#diccionario : documento JSON(colección tiene clave y valor)
diccionario = {
    "nombre":"Fernando",
    "apellido":"Gutierrez",
    "curso": "Master en Python"
}
#otro tipo de variable rango
rango = range(5)

#variable tipo byte, delante pongo una letra b para decir que es tipo bye
byte = b"tipo byte"

print(lista)

print(tupla)

print(diccionario)

print(rango)

print(byte)

#con la función str cambio cualquiera variable a string
nombre = "Fernando"
numero = str(25)

print(type(numero))

print("Hola me llamo " +nombre +" y tengo " + numero + " años")
