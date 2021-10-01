import csv
from . import FICHERO

class Movimiento():
    def __init__(self, fecha, concepto, es_ingreso, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.es_ingreso = es_ingreso
        self.cantidad = cantidad

class ListaMovimientos():    #sólo va a leer y escribir la lista de moviminetos
    def __init__(self):
        self.movimientos = []
    def leer(self):
        self.movimientos = []
        fichero = open(FICHERO, "r")
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