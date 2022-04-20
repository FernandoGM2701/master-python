"""
# BUCLE FOR

for variable in elemento_iterable (lista, rango, etc) algo que se pueda recorrer
    BLOQUE DE INSTRUCCIONES


"""

contador = 0
resultado = 0

for contador in range(0, 5):
    print("Voy por el "+ str(contador))
    
    resultado = resultado + contador


print(f"El resultado es: {resultado}")



# Ejemeplo tablas de multiplicar

print("*************TABLA DE MULTIPLICAR*************")

num1 = int(input("Ingrese el número para la tabla de multiplicar: "))

if(num1 < 1):
    num1 = 1


for contador in range(0,10):
    print(f" {num1} X {contador} = {num1*contador}")
else:
    print("La multiplicación acabó") 

 
