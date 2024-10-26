# Abrir el archivo en modo lectura
f = open("practica 4_daniel_arguijo_1325.txt", "r", encoding='utf-8')

# Leer los primeros 5 caracteres del archivo
primeros_caracteres = f.read(65)

# Imprimir los primeros 5 caracteres
print(primeros_caracteres)

# Cerrar el archivo
f.close()
