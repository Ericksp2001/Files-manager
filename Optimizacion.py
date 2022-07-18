import os
import glob
import shutil

os.chdir("/Users/erick/Downloads")

repeticion = True
direcciones = ["FBD*.pdf", "FBD*.docx", "*.zip", "*.pkt", "FR*.pdf", "FR*.docx", "SO*.pdf", "SO*.docx", "SO*.xlsx",
               "PYE*.pdf", "PYE*.docx", "PYE*.xlsx", "Cl*.pdf", "Cl*.docx"]
Cantidades = [2,4,3,3,2]

src = r'C:\Users\erick\Downloads'

destinos = [r'C:\Users\erick\Desktop\Sistemas Operativos', r'C:\Users\erick\Desktop\Fundamentos de Bases de Datos',
            r'C:\Users\erick\Desktop\Fundamentos de Redes', r'C:\Users\erick\Desktop\Compiladores',
            r'C:\Users\erick\Desktop\Probabilidad y estadistica']

contador = 0

movimientos = 0


# Falta corregir el hecho de que los destinos son solo 5 y se acaban antes de que termine de iterar posiblemente podemos usar un is empty
for direc in direcciones:
    archivos = glob.glob(f"{direc}")
    for arch in archivos:
        if repeticion:
            if os.path.isfile(f"{src}/{arch}"):
                pass
            else:
                shutil.move(f"{src}/{arch}", destinos[contador])
                movimientos = movimientos + 1
        else:
            shutil.move(f"{src}/{arch}", destinos[contador])
            movimientos = movimientos + 1


print(f'Cantidad de movimientos realizada {movimientos}')
