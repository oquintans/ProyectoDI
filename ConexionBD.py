import sqlite3 as dbapi
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from gi.repository import Gtk


class ConexionBD:
    def __init__(self):
        """
        Inicializa la conexion a la base de datos
        """
        self.db = dbapi.connect("../BD/basedatos.dat")
        self.cursor = self.db.cursor()
        self.lista = []
        print(self.db)

    def createTable(self):
        """
        Crea las tablas de la base de datos
        """
        self.cursor.execute("""create table componentes(id text primary key,tipo text, marca text,
               modelo text,precio integer, uStock integer, uAlmacen integer)""")
        self.db.commit()

    def select(self):
        """
        Ejecuta el comando select mostrando todos los registros almacenados en la BD
        """
        self.lista = []
        self.cursor.execute("""select * from componentes""")
        for result in self.cursor:
            self.lista.append([result[0], result[1], result[2], result[3], result[4], result[5], result[6]])
        return self.lista

    def select2(self, tipo, marca, precio):
        """
        Select específico para mostra los registros de la base de datos dependiendo de los parametros indicados
        :param tipo: tipo de componente
        :param marca: marca del componente
        :param precio: precio del componente
        """
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
        """
        Inserta valores por defecto en la BD

        """
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
        """
        Actualiza la base de datos cambiando el stock del registro con id x.
        :param ustock: Unidades de stock nuevas
        :param id: Id del componente

        """
        us = ustock - 1
        reg = (us, id)
        self.cursor.execute("""update componentes set uStock=? where id=?""", reg)
        self.db.commit()

    def close(self):
        """
        Cierra la conexion con la BD

        """
        self.db.close()

    def informe(self):
        self.cursor.execute("select * from componentes")
        taboaBaseDatos = []

        for fila in self.cursor:
            taboaBaseDatos.append(fila)

        taboa = Table(taboaBaseDatos)

        guion = []
        guion.append(taboa)

        documento = SimpleDocTemplate("../BD/Informe.pdf", pagesize=A4, showBoundary=0)
        documento.build(guion)
        print("by Platypus")
        print("Informe Creado con éxito")
