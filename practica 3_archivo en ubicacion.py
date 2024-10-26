# Abrir un archivo en una ubicación específica
f = open("practica 3_daniel_arguijo_1325.txt", "r", encoding='utf-8')

# Leer el contenido del archivo
contenido = f.read()

# Imprimir el contenido
print(contenido)

# Cerrar el archivo
f.close() 
