import sqlite3 as dbapi
from gi.repository import Gtk


class ConexionBD:
    def __init__(self):
        self.db = dbapi.connect("../BD/basedatos.dat")
        self.cursor = self.db.cursor()
        self.lista = []
        print(self.db)

    def createTable(self):
        self.cursor.execute("""create table componentes(id text primary key,tipo text, marca text,
               modelo text,precio integer, uStock integer, uAlmacen integer)""")
        self.db.commit()

    def select(self, button):
        self.cursor.execute("""select * from componentes""")
        for result in self.cursor:
            print("ID: " + result[0] +
                  " - Tipo: " + result[1] +
                  " - Marca: " + result[2] +
                  " - Modelo: " + str(result[3]) +
                  " - Precio: " + str(result[4]) +
                  " - UStock: " + str(result[5]) +
                  " - UAlmacen: " + str(result[6]))
            self.lista.append([result[0], result[1], result[2], result[3], result[4], result[5], result[6]])

    def insert(self):
        self.cursor.execute("""insert into componentes values('0001','Procesador','Intel','I5',150,5,3)""")
        self.db.commit()
