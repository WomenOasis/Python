#Creando una factura 
import detetime 
import reportlaqb.pdfgen import canvas 
import reportlab.lib.pagazis import letter 
import platform 
import os
import time 

Glows = ['Brillo MAgic Oro gold', 'Labial Colageno FLor Base', 'Jabon Facial de Arroz', 'Crema hidratante de Arroz', 
'Tarrro Colageno Labios', 'Colageno de ojera Unidad', 'Contorno de ojeras Arroz', 'Pestañina I love Super Volumen', 'Polvo Hadas RPK', 
'Velo Facial VItamina C']

class Factura: 

    hora= datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    segundos = datetime.datetime.now().second

    informacion  = {"nomre_empresa": 'Glows Skincare','TEL': 3237341591, 
    'cedula':'1096194036', 'ciudad':'Bucaramanga'}

    def _int-(self) -> None:
        pass
    def preguntar_cliente(self,diccionario):

        self.CLiente = input("nombre del cliente"); diccionario ["Cliente"] = self.clientesel
        sef.cc = int(input("C.C. :"));diccionario["CEDULA"] = self.ccs
        self.numero = int(input("Celular: "));diccionario["Celular"] = self.numero

    def preguntar_producto(self, diccionario):
        self.Descripcion = input("Digital el producto: ")
        self.Cantidad = in(input("Cantidad de productos"))
        self.Precio = float(input("Digita el precio del producto:  $"))
        self.pagar = input("Forma de pago: ")
        self.Cajero = input("Digita el nombre del cajero: ")
        diccionario["Cajero"] = self.Cajero
def Limpiar(self):
    time.sleep(2)

    if platform.system() == 'Windows':
        print("Preparando Factura....")
        time.sleep(2)
        os.system('cls')
    else:
        os.system('clear')

def Mostrar(self, diccionario):

    self.sub = self.Cantidad * self.Precio
    self.pp = self.sub - (self.sub * .19)
    self.Value = diccionario.items()
    print("\t              ",list(self.Value)[0][1])
    print("\t            NIT: ",list(self.Value)[1][1])
    print("\t        RESPONSABLE DE IVA. ",list(self.Value)[2][1]) ",list(self.Value)[3][1])
    print("\t            ",list(self.Value)[3][1])
    print("\t            TELEFONO:", list(self.Value) [4][1])
    print("\t          ",list(self.Value)[5][1])
    print("\t             ",list(self.Value)[6][1])
    print("\t        ",list(self.Value)[7][1])
    print("\n\t            ",list(self.Value)[8][1], FEC 01/04/2022")
    print("\t           Desde ",list(self.Value)[9][1], "    Hasta", list(self.Value) [10][1])
    print("\t             DCTO/EQUIVALENTE POS:", list(self.Value) [11][1])
    print("\t             VIGENCIA HASTA: 31/03/2023")
    print("\t          FECHA: ",datetime.datetime.now().day,"/",datetime.datetime.now().month,"/", datetime.datetime.
    now().year,          Hora:", self.hora,":", self.minuto,":", self.segundos)
    print("\t            CAJERO: ",self.Cajero)
    print("\t       CLIENTE: ",self.Cliente)
    print("\t        NIT/C.C: ",self.CC)
    print("\t         CIUDAD: Neiva")
    print("\t        Celular: ",self.numero)
    print("\t       =========================================")
    print("\t      Uds PRODUCT.DESCRIPCION    PRECIO      TOTAL")

    def Mostrar_PDF(self):
        print("Hola")
        w, h = letter
        C = canvas.Canvas("Factura.pdf",pagesize=letter)
        C.setLineWidth(.2)
        C.setFont('Helvetica',10)
        C.rect(160,h-660,300,655) #Ancho 300 y alto = 660
        C.drawString(250, h-30, list(self.Value)[0][1])
        C.drawString(251, h-42, f"NIT: {list(self.Value) [1][1]}")
        C.drawString(198, h-55, f"RESPONSABLE DE IVA. (list(self.Value)[2][1]}")
        C.drawString(238, h-67, list(self.Value)[3][1])
        C.drawString(236, h-79, f"TELEFONO: (list(self.Value)[4][1]}")
        C.drawString(210, h-90, list(self.Value)[5][1])
        C.drawString(248, h-101, list(self.Value)[6][1])
        C.drawString(248, h-113, list(self.Value)[7][1])
        C.drawString(175, h-140, f"{list(self.Value)[8][1]}
        C.drawString(175 , h-152, f"Desde (list(self.Value)[9][1]} C.drawString(175, h-164, f"DCTO/EQUIVALENTE POS: (list(self.Value) [7] [1]}")
        C.drawString(175, h-176, "VIGENCIA HASTA: 31/03/2023")
        FEC 01/04/2022")
        Hasta {list(self.Value) [10][1]}")
        C.drawString(175, h-188, f"FECHA: {datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.