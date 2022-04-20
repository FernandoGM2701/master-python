"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto.
"""

nombre_de_variable = "Esta es una variable"
numero = 24
letra = "24"


#print(nombre_de_variable)
#print(numero)
#print(letra)

"""
Concatenación de variables

Con un "+", con una "f" delante de un String, con la función "format"

"""

nombre = "Fernando"
apellido = "Gutierrez Mejía"
alias = "Fercho"

#Con el +
print(nombre + " " + apellido + " - "+ alias)

#Con la f
print(f"{nombre} {apellido} - {alias}")

#Con la función format
print("{} {} - {}".format(nombre, apellido, alias))



