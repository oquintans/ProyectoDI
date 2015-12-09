from gi.repository import Gtk

__author__ = 'oquintansocampo'


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Login")
        self.set_border_width(10)
        self.set_default_size(500, 100)

        # LayoutBox
        self.box = Gtk.Box(spacing=6)
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # ListBox
        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        print(self.list_box.get_selection_mode())
        self.box.pack_start(self.list_box, True, True, 0)

        # Row1
        self.row1 = Gtk.ListBoxRow()
        self.hor_box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row1.add(self.hor_box1)
        self.v_box1 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box1.pack_start(self.v_box1, True, True, 1)

        # Row2
        self.row2 = Gtk.ListBoxRow()
        self.hor_box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row2.add(self.hor_box2)
        self.v_box2 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box2.pack_start(self.v_box2, True, True, 1)

        # Row3
        self.row3 = Gtk.ListBoxRow()
        self.hor_box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row3.add(self.hor_box3)
        self.v_box3 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box3.pack_start(self.v_box3, True, True, 1)

        # Row4
        self.row4 = Gtk.ListBoxRow()
        self.hor_box4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row4.add(self.hor_box4)
        self.v_box4 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box4.pack_start(self.v_box4, True, True, 1)

        # Labels
        label_title = Gtk.Label("WELCOME")
        label_user = Gtk.Label("User: ")
        label_pass = Gtk.Label("Password: ")

        # TextFields
        field_user = Gtk.Entry()
        field_pass = Gtk.Entry()

        # Buttons
        log_button = Gtk.Button(label="Entrar")

        self.v_box1.pack_start(label_title, True, True, 1)
        self.v_box2.pack_start(label_user, True, True, 1)
        self.v_box2.pack_start(field_user, True, True, 1)
        self.v_box3.pack_start(label_pass, True, True, 1)
        self.v_box3.pack_start(field_pass, True, True, 1)
        self.v_box4.pack_start(log_button, True, True, 1)

        self.list_box.add(self.row1)
        self.list_box.add(self.row2)
        self.list_box.add(self.row3)
        self.list_box.add(self.row4)


# Instanciar
fiestra = Window()
# Posicion Ventana
fiestra.set_position(Gtk.WindowPosition.CENTER)
# Resizable
fiestra.set_resizable(False)
# Cierre on Click
fiestra.connect("delete-event", Gtk.main_quit)
# Mostrar ventana
fiestra.show_all()
#fiestra.set_decorated(True)
# Activar atencion de eventos
Gtk.main()