# Abrir el archivo "demofile3.txt" en modo escribir (sobrescribir)
f = open("practica 6_daniel_arguijo_1325.txt", "w", encoding='utf-8')
f.write("jose daniel arguijo torres sale a entrenar los martes y jueves ")
f.close()

# Abrir y leer el archivo después de sobrescribir
f = open("practica 6_daniel_arguijo_1325.txt", "r", encoding='utf-8')
print(f.read())
f.close()
