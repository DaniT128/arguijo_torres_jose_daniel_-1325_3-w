import os

# Nombre del archivo que deseas eliminar
archivo = "practica 8_daniel_arguijo_1325.txt"

# Verificar si el archivo existe
if os.path.exists(archivo):
    # Eliminar el archivo
    os.remove(archivo)
    print(f"{archivo} ha sido eliminado.")
else:
    print(f"{archivo} no existe.")
