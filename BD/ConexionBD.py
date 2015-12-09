import sqlite3 as dbapi


class ConexionBD:
    def __init__(self):
        self.db = dbapi.connect("basedatos.dat")
        self.cursor = self.db.cursor()
        print(self.db)

    def createTable(self):
        self.cursor.execute("""create table componentes(id text primary key,tipo text, marca text,
               modelo text,precio integer, uStock integer, uAlmacen integer)""")
        self.db.commit()

    def select(self):
        self.cursor.execute("""select * from componentes""")
        for result in self.cursor:
            print(result[0] + " - " + result[1] + " - " + result[2] + " - " + str(result[3]) + " - " + str(
                result[4]) + " - " + str(result[5]))

    def insert(self):
        self.cursor.execute("""insert into componentes values('0001','Procesador','Intel','I5',150,5,3)""")
        self.db.commit()


conn = ConexionBD()

conn.select()
