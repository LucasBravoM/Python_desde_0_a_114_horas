# Reemplazar texto en python

mensaje = "Hola mundo, mundo"

print(mensaje)
# Reemplazar TODAS las apariciones

nuevo = mensaje.replace("mundo","Python")

print(nuevo)
#Salida: Hola Python, Phyton

uno_solo = mensaje.replace("mundo","Dev", 1)
#Hola Dev, mundo

print(uno_solo)