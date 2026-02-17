#Cadenas inmutables

animal = "Gato"

#animal[4] = "s" # Provoca error
#print(animal)

plural = animal + "s"

print(animal) # Salida: Gato (intacto)
print(plural) # Salida: Gatos (Nuevo objeto)

plural = f"{animal}s"
print(plural) 


