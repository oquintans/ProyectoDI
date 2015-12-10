from gi.repository import Gtk
from BD.ConexionBD import ConexionBD
from Clases import Componentes
from Ventanas.VentanaLogIn import WindowL
# from Ventanas.VentanaCliente import WindowC


# Instanciar
fiestra = WindowL()
fiestra.set_position(Gtk.WindowPosition.CENTER)
fiestra.set_resizable(False)
fiestra.connect("delete-event", Gtk.main_quit)
fiestra.show_all()
Gtk.main()

