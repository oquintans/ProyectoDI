from gi.repository import Gtk
from VentanaLogIn import WindowL
from VentanaCliente import WindowC
from VentanaAdmin import WindowA
from ConexionBD import ConexionBD
from Componentes import Componentes

# Instanciar
fiestra = WindowL()
fiestra.set_position(Gtk.WindowPosition.CENTER)
fiestra.set_resizable(False)
fiestra.connect("delete-event", Gtk.main_quit)
fiestra.show_all()
Gtk.main()
