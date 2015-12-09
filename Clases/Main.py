from Clases import Componentes

comp= Componentes.Componentes("A0001", "T.Grafica", "Nvidia", "GTX650", 100, 10, 5)
comp.to_string()
compra=comp.comprar()
while(compra!=True):
    comp.comprar()
comp.to_string()