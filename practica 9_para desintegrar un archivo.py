import os

# Nombre de la carpeta que deseas eliminar
carpeta = "practica 9_daniel_arguijo_1325.txt"

# Intentar eliminar la carpeta
try:
    os.rmdir(carpeta)
    print(f"La carpeta '{carpeta}' ha sido eliminada.")
except FileNotFoundError:
    print(f"La carpeta '{carpeta}' no existe.")
except OSError:
    print(f"La carpeta '{carpeta}' no está vacía o no se puede eliminar.")
