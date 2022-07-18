import os
import glob
import shutil

# Seleccionamos el directorio

os.chdir("/Users/erick/Downloads")

# Inicializamos la variable que cuenta los archivos

cantidad = 0

# Recorremos el directorio buscando los archivos

for contenido in os.listdir():
    print(contenido)
    cantidad = cantidad + 1

print(f'Cantidad de archivos: {cantidad}')

# Creamos la carpeta

if os.path.exists("Libros"):
    pass
else:
    os.mkdir("Libros")

# Agrupamos los archivos por extensiones

pdf = glob.glob("*.pdf")
word = glob.glob("*.docx")

# Movemos los archivos

for i in pdf:
    shutil.move(i, "Libros")
