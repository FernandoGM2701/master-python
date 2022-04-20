"""
    Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos y 
    sacar por pantalla cuántos han aprobado y cuántos han suspendido.

"""
aprobados = 0;
suspendidos = 0;

for contador in range(1,16):
    nota = int(input(f"Ingrese la nota {contador}: "))
    if(nota >= 11):
        aprobados = aprobados + 1
    else:
        suspendidos = suspendidos + 1

print(f"Los aprobados son: {aprobados}")
print(f"Los suspendidos son: {suspendidos}")
