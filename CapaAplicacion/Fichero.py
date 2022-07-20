from CapaAplicacion.Directorio import directorio


class Fichero:
    direcDest = ""
    direcOrigen = ""
    extensiones = None
    def __init__(self, direcDest , direcOrigen):
        self.direcDest = direcDest
        self.direcOrigen = direcOrigen
        self.extensiones = directorio.__init__()

    def agregarExt():
        print("Hasta aqui llegue")