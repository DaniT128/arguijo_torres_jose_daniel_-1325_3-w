# Nombre del archivo a abrir
nombre_archivo = "practica 1_daniel_arguijo_1325.txt"

# Abrir y leer el archivo
try:
    with open(nombre_archivo, "r") as f:
        contenido = f.read()  # Leer todo el contenido del archivo
        print(contenido)       # Imprimir el contenido
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
except IOError:
    print("Ocurrió un error al intentar leer el archivo.")
