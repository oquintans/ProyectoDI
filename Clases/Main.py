from gi.repository import Gtk
from Ventanas.VentanaLogIn import WindowL
from Ventanas.VentanaCliente import WindowC
from Ventanas.VentanaAdmin import WindowA
from BD.ConexionBD import ConexionBD
from Clases import Componentes

# Instanciar
fiestra = WindowL()
fiestra.set_position(Gtk.WindowPosition.CENTER)
fiestra.set_resizable(False)
fiestra.connect("delete-event", Gtk.main_quit)
fiestra.show_all()
Gtk.main()
