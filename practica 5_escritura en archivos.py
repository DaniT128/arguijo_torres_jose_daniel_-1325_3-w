# Abrir el archivo "demofile2.txt" en modo anexar
with open("practica 5_daniel_arguijo_1325.txt", "a") as f:
    f.write("Now the file has more content!\n")  # Agregar contenido

# Abrir y leer el archivo después de agregar contenido
with open("practica 5_daniel_arguijo_1325.txt", "r") as f:
    print(f.read())  # Imprimir el contenido del archivo


