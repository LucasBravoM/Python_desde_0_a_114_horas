#Programa: Función Bool

# 1. Números (int y float)

print(bool(0))  #False (El vacío numérico)
print(bool(0.0)) #False
print(bool(42))  #True

#2. Texto (Strings)
#Cadena vacía = nada = false
print(bool("")) #False

# Cadena con espacio o texto = algo = true

print(bool(" ")) # True

print(bool("Hola")) #True

# 3. None (Ausencia total)
vacio = None
print(bool(vacio))  #False

print(bool(False))
print(bool(True))
