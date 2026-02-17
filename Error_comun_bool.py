# ERROR COMUN DE PRINCIPIANTE

respuesta_usuario = "False" # Esto es texto

# La función bool evalúa si el string está vacío
es_verdad = bool(respuesta_usuario)

print(f"El valor es: {es_verdad}")

# Output: El valor es:True
# Porque el string tiene letras, no está vacío

texto_vacio = ""
print(bool(texto_vacio)) #False


