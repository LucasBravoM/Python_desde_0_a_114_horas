#Programa: Aplicar el concepto de slicing

texto = "PROGRAMACION"

# 1. Básico [inicio:fin]
print(texto[0:4]) # "PROG" El idice 4 no se imprime

# 2. Atajo desde el inicio [:fin]

print(texto[:4]) # PROG (Asume inicio 0)

# 3. Atajo hasta el final [inicio:]

print(texto[8:]) # "CION" (Hasta el utlimo char)

# 4. ïndices negativos

print(texto[-4:]) # "CION" ( Los últimos 4)

# 5. Pasos [::paso]

print(texto[::1]) #"NOICAMARGOP"





