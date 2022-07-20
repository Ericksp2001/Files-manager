class directorio:
    #Definicion de variables
    
    #Cantidad de extension
    cantExtension = 0
    #Cantidad maxima de extensiones
    maxExt=6
    #Array que contiene las distintas extensiones
    extension = [None]*cantExtension
    #Banderas de las distintas extensiones
    pdf=False
    word=False
    excel=False
    zip=False
    png=False
    jpg=False
    
    #Definicion de constructores
    def __init__(self , extension, cantExtension):
        self.cantExtension = cantExtension
        self.extension = extension
        
    def __init__(self):
        self.cantExtension = 0
    
    #Definicion de metodos
    def setearExt(self, pdf, word, excel, zip, png, jpg):
        self.pdf=pdf
        self.word=word
        self.excel=excel
        self.zip=zip
        self.png=png
        self.jpg=jpg
        
    