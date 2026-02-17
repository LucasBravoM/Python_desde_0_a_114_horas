# Generador de un Email

nombre = "Lucas Andres Bravo"
empresa = "Capital BM"
dominio = "com.co"

#print(nombre, empresa, dominio)

nombre_minuscula = nombre.lower()
empresa_minuscula = empresa.lower()

print(nombre_minuscula, empresa_minuscula, dominio)

nombre_junto = nombre_minuscula.replace(" ",".")
nombre_junto = nombre_junto.__add__("@")
print(nombre_junto)

empresa_junto = empresa_minuscula.replace(" ","")
empresa_junto = empresa_junto.__add__(".")
print(nombre_junto, empresa_junto, dominio)

correo= nombre_junto+empresa_junto+dominio
print(correo)


# ==== Ahora como el profe lo hizo xD ====

print()
print("\n*** Generador de Emails ***")

#Nombre completo del usuario
nombre_normalizado = ' Lucas Andres Bravo  '
print(f'Nombre usuario:{nombre_normalizado}')

# Procesar o normalizar el nombre de usuario
nombre_normalizado = nombre_normalizado.strip()
print(f'Nombre usuario:{nombre_normalizado}')

#Reemplazar espacios por puntos
nombre_normalizado = nombre_normalizado.replace(" ",".")
print(f'Nombre usuario:{nombre_normalizado}')

#Convertimos en minúsculas
nombre_normalizado = nombre_normalizado.lower()
print(f'Nombre usuario:{nombre_normalizado}')

#Datos de la empresa
nombre_empresa = "  Capital BM "
print(f'\nNombre de la empresa: {nombre_empresa}')
extension_dominio = ".com.co"
print(f'Extensión del dominio: {extension_dominio}')

#Quitamos espacios en blanco y convertir en minuscula
nombre_empresa_normalizado = nombre_empresa.replace(" ","").lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio del email normalizado: {dominio_email_normalizado}')
email =f'{nombre_normalizado}{dominio_email_normalizado}'
print(f'\nEmail final: {email}')

