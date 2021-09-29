#aquí creamos la apliación flask
from flask import Flask

FICHERO = "data/movimientos.csv"

app = Flask(__name__)

from balance import views
