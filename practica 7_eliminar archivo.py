import os

# Nombre del archivo que deseas eliminar
nombre_archivo = "practica 7_daniel_arguijo_1325.txt"

# Verificar si el archivo existe antes de intentar eliminarlo
if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print(f"El archivo '{nombre_archivo}' ha sido eliminado.")
else:
    print(f"El archivo '{nombre_archivo}' no existe.")
