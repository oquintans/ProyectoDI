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

    def select(self):
        self.lista = []
        self.cursor.execute("""select * from componentes""")
        for result in self.cursor:
            self.lista.append([result[0], result[1], result[2], result[3], result[4], result[5], result[6]])
        return self.lista

    def select2(self, tipo, marca, precio):
        self.lista = []
        if (tipo == "Tipo" and marca == "Marca" and precio == "Precio"):
            self.cursor.execute("""select * from componentes""")
        elif (tipo == "Tipo" and marca == "Marca" and precio != "Precio"):
            reg = (precio,)
            self.cursor.execute("""select * from componentes where precio<? """, reg)
        elif (tipo == "Tipo" and marca != "Marca" and precio == "Precio"):
            reg = (marca,)
            self.cursor.execute("""select * from componentes where marca=? """, reg)
        elif (tipo == "Tipo" and marca != "Marca" and precio != "Precio"):
            reg = (marca, precio,)
            self.cursor.execute("""select * from componentes where marca=? and precio<? """, reg)
        elif (tipo != "Tipo" and marca == "Marca" and precio == "Precio"):
            reg = (tipo,)
            self.cursor.execute("""select * from componentes where tipo=? """, reg)
        elif (tipo != "Tipo" and marca == "Marca" and precio != "Precio"):
            reg = (tipo, precio,)
            self.cursor.execute("""select * from componentes where tipo=? and precio<? """, reg)
        elif (tipo != "Tipo" and marca != "Marca" and precio == "Precio"):
            reg = (tipo, marca,)
            self.cursor.execute("""select * from componentes where tipo=? and marca=? """, reg)
        elif (tipo != "Tipo" and marca != "Marca" and precio != "Precio"):
            reg = (tipo, marca, precio,)
            self.cursor.execute("""select * from componentes where tipo=? and marca=? and precio<? """, reg)

        for result in self.cursor:
            self.lista.append([result[0], result[1], result[2], result[3], result[4], result[5], result[6]])
        return self.lista

    def insert(self):
        self.cursor.execute("""insert into componentes values('0001','Procesador','Intel','I5',150,5,3)""")
        self.cursor.execute("""insert into componentes values('0002','T. Grafica','ASUS','GTX650',98,2,3)""")
        self.cursor.execute("""insert into componentes values('0003','Placa Base','ASUS','M587',90,1,8)""")
        self.cursor.execute("""insert into componentes values('0004','T. Grafica','MSI','GTX980',400,5,3)""")
        self.cursor.execute("""insert into componentes values('0005','RAM','Kingston','Merda',150,5,3)""")
        self.cursor.execute("""insert into componentes values('0006','HDD','SeaGate','Caviar',150,8,3)""")
        self.cursor.execute("""insert into componentes values('0007','Procesador','Intel','I7',150,5,3)""")
        self.cursor.execute("""insert into componentes values('0008','Placa Base','GigaByte','Z377-B',67,2,2)""")
        self.cursor.execute("""insert into componentes values('0009','T. Grafica','GigaByte','GT540',40,1,0)""")
        self.cursor.execute("""insert into componentes values('0010','RAM','Crucial','Dios',777,7,7)""")
        self.cursor.execute("""insert into componentes values('0011','HDD','SeaGate','Caviar',700,5,3)""")
        self.cursor.execute("""insert into componentes values('0012','Procesador','AMD','FX6300',105,0,3)""")
        self.cursor.execute("""insert into componentes values('0013','Placa Base','ASUS','8845z',150,5,3)""")
        self.db.commit()

    def update(self, ustock, id):
        us = ustock - 1
        reg = (us, id)
        self.cursor.execute("""update componentes set uStock=? where id=?""", reg)
        self.db.commit()

    def close(self):
        self.db.close()
