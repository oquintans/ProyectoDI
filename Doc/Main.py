# -*- coding: utf-8 -*-

from gi.repository import Gtk
from VentanaLogIn import WindowL


# Instanciar
fiestra = WindowL()
fiestra.set_position(Gtk.WindowPosition.CENTER)
fiestra.set_resizable(False)
fiestra.connect("delete-event", Gtk.main_quit)
fiestra.show_all()
Gtk.main()

