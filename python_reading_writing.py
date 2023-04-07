# Abrir el archivo
archivo = open("archivo.txt", "r")

# Leer el contenido del archivo
contenido = archivo.read()

# Cerrar el archivo
archivo.close()

# Imprimir el contenido del archivo
print("El contenido del archivo es: ")
print(contenido)

# Abrir el archivo en modo de escritura
archivo = open("archivo.txt", "w")

# Escribir una línea en el archivo
archivo.write("¡Hola, mundo!\n")

# Cerrar el archivo
archivo.close()

# Imprimir mensaje de éxito
print("La línea '¡Hola, mundo!' se ha escrito en el archivo.")
