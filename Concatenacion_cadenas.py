#Programa: Ejemplo de concatenación con cadenas

#1. Usando el operador +
nombre = "Lucas"
apellido = "Bravo"
nombre_comleto = nombre + " " + apellido
print("Usando + : ", nombre_comleto)

#2. Usando el método print

edad = 29
print("Usando comas: ", "Nombre:", nombre , ", Edad: ", edad)

#3. Usando F-String
ciudad = "Bogotá"
pais = "Colombia"
profesion = "Inge"
presentacion = f"Hola, soy {nombre_comleto}, tengo {edad+1} años, vivo en {ciudad}, {pais} y soy {profesion}"
print(presentacion)