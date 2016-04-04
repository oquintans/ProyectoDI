# -*- coding: utf-8 -*-

class Componentes:
    def __init__(self, codigo, tipo, marca, modelo, precio, ustock, ualmacen):
        self.codigo = codigo
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.u_stock = ustock
        self.u_almacen = ualmacen

    def comprar(self):
        """Metodo para comprar componenetes"""
        un = int(input("Unidades?\n"))
        if (un > self.u_stock):
            print("No quedan suficientes unidades")
        else:
            price = self.precio * un
            imp = int(input("Precio: " + str(price) + "\nIntroduzca importe\n"))
            if (imp < price):
                print("No tiene suficiente saldo")
            else:
                vuelta = imp - price
                self.u_stock -= un
                print("Producto adquirido")
                print("Su vuelta es " + str(vuelta) + "€")
                return True

    def to_string(self):
        """Imprime los valores de los atributos del objeto separados por guiones"""
        print(
            self.codigo + " - " +
            self.tipo + " - " +
            self.marca + " - " +
            self.modelo + " - " +
            str(self.precio) + " - " +
            str(self.u_stock) + " - " +
            str(self.u_almacen)
        )
