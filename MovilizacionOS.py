import os
import glob
import shutil

os.chdir("/Users/erick/Downloads")

# Inicializamos la variable que cuenta los archivos

cantidad = 0

# Recorremos el directorio buscando los archivos

for contenido in os.listdir():
    cantidad = cantidad + 1

print(f'Cantidad de archivos: {cantidad}')

# Fundamentos de Bases de Datos
FBDpdf = glob.glob("FBD*.pdf")
FBDword = glob.glob("FBD*.docx")

# Fundamentos de Redes
FRzip = glob.glob("*.zip")
FRpkt = glob.glob("*.pkt")
FRtxt = glob.glob("*.txt")
FRpdf = glob.glob("FR*.pdf")
FRword = glob.glob("FR*.docx")

# Sistemas Operativos
SOpdf = glob.glob("SO*.pdf")
SOword = glob.glob("SO*.docx")
SOExcel = glob.glob("SO*.xlsx")

# Probabilidad y estadistica
PYEpdf = glob.glob("PYE*.pdf")
PYEword = glob.glob("PYE*.docx")
PYEexcel = glob.glob("PYE*.xlsx")

# Compiladores
CLpdf = glob.glob("Cl*.pdf")
Clword = glob.glob("Cl*.docx")

# Definimos destinos

src = r'C:\Users\erick\Downloads'

# Fundamentos de Bases de Datos

FBDdest = r'C:\Users\erick\Desktop\Fundamentos de Bases de Datos'

for k in FBDpdf:
    shutil.move(f"{src}/{k}", FBDdest)

for ar in FBDword:
    shutil.move(f"{src}/{ar}", FBDdest)

# Fundamentos de redes
FRdest = r'C:\Users\erick\Desktop\Fundamentos de Redes'

for k in FRpdf:
    shutil.move(f"{src}/{k}", FRdest)

for z in FRpkt:
    shutil.move(f"{src}/{z}", FRdest)

for op in FRtxt:
    shutil.move(f"{src}/{op}", FRdest)

for jk in FRzip:
    shutil.move(f"{src}/{jk}", FRdest)

for mi in FRword:
    shutil.move(f"{src}/{mi}", FRdest)

# Compiladores y Lenguajes
CLdest = r'C:\Users\erick\Desktop\Compiladores'

for kl in Clword:
    shutil.move(f"{src}/{kl}", CLdest)

for mj in CLpdf:
    shutil.move(f"{src}/{mj}", CLdest)

# Sistemas Operativos
SOdest = r'C:\Users\erick\Desktop\Sistemas Operativos'

for ko in SOpdf:
    shutil.move(f"{src}/{ko}", SOdest)

for ki in SOExcel:
    shutil.move(f"{src}/{ki}", SOdest)

for kyu in SOword:
    shutil.move(f"{src}/{kyu}", SOdest)

# Probabilidad y estadistica
PYEdest = r'C:\Users\erick\Desktop\Probabilidad y estadistica'

for hi in PYEpdf:
    shutil.move(f"{src}/{hi}", PYEdest)

for ho in PYEword:
    shutil.move(f"{src}/{ho}", PYEdest)

for hu in PYEexcel:
    shutil.move(f"{src}/{hu}", PYEdest)

print('Todo salio bien SIUUUUUU')
