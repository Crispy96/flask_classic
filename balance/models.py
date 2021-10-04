from datetime import date, datetime
import csv
from . import FICHERO

class ValidationError(Exception):
    pass

class Movimiento():
    self.errores = []
    def __init__(self, diccionario):
            #podriamos creari un self.errores=[] y los vas añadiendo
        try:
            #realizamos las validaciones
            self.fecha = date.fromisoformat(diccionario["fecha"])   #lo ponemos en diccionario para poder validarlo
        except ValueError:
            raise ValidationError("Formato de fecha incorrecto")

        ahora = datetime.now()
        if self.fecha.strftime("%Y%m%d")> ahora.strftime("%Y%m%d"):
            raise ValidationError("La fecha no puede ser superior a la actual")    

        self.concepto =  diccionario["concepto"]
        if self.concepto == "":
            raise ValidationError("Informe el concepto")

        try:
            self.es_ingreso =  diccionario["ingreso_gasto"]
        except KeyError:
            raise ValidationError("Informe el tipo de movimineto(I/G)")

        try:
            self.cantidad =  float(diccionario["cantidad"])
        except ValueError:
            raise ValidationError("Cantidad debe de ser un número")
        
        if self.canitat <=0:
            raise ValueError("Cantidad debe de ser positiva")



class ListaMovimientos():    #sólo va a leer y escribir la lista de moviminetos
    def __init__(self):
        self.movimientos = []
    def leer(self):
        self.movimientos = []
        fichero = open(FICHERO, "r", encoding="utf-8")  #encoding sirve para que no se cambie 
        dreader = csv.DictReader(fichero)
        for linea in dreader:
            self.movimientos.append(linea)
        fichero.close()

    def escribir(self):
        if len(self.movimientos) == 0:    #de estar forma sólo lo hace si el fichero no esta vacio
            return

        fichero = open(FICHERO, "w")
        #nombres_campo = ["fecha", "concepto", "ingreso_gasto", "cantidad"]
        nombres_campo = list(self.movimientos[0].keys())   #lo coje directamente de la lista de movimientos 
        dwriter = csv.DictWriter(fichero, fieldnames = nombres_campo)
        dwriter.writeheader()
        for movimiento in self.movimientos:
            dwriter.writerow(movimiento)
        fichero.close()

    def anyadir(self, valor):
        movimiento =  {}
        movimiento['fecha'] = valor ['fecha']
        movimiento['concepto'] = valor ['concepto']
        movimiento['ingreso_gasto'] = valor ['ingreso_gasto']
        movimiento['cantidad'] = valor ['cantidad']
        self.movimientos.append(movimiento)