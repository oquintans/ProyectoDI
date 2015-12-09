from gi.repository import Gtk


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cliente")
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

        # TreeView
        self.tree = Gtk.TreeView()
        self.insertarCols(5)

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


        # Labels
        l_tipo = Gtk.Label("Tipo")
        l_marca = Gtk.Label("Marca")
        l_modelo = Gtk.Label("Modelo")

        # ComboBox
        self.cbTipo = Gtk.ComboBoxText()
        self.cbMarca = Gtk.ComboBoxText()
        self.cbModelo = Gtk.ComboBoxText()
        self.cbTipo.insert_text(1, "Procesadores")

        # Botones
        self.b_comprar = Gtk.Button(label="Comprar")
        self.b_consultar = Gtk.Button(label="Consultar")
        self.b_salir = Gtk.Button(label="Salir")

        self.v_box1.add(l_tipo)
        self.v_box1.add(l_marca)
        self.v_box1.add(l_modelo)

        self.v_box2.add(self.cbTipo)
        self.v_box2.add(self.cbMarca)
        self.v_box2.add(self.cbModelo)

        self.v_box3.add(self.b_comprar)
        self.v_box3.add(self.b_consultar)
        self.v_box3.add(self.b_salir)


        self.list_box.add(self.row1)
        self.list_box.add(self.row2)
        self.list_box.add(self.row3)
        self.list_box.add(self.tree)

    def insertarCols(self, num):
        for i in range(num):
            colum = Gtk.TreeViewColumn(title=str(i))
            colum.set_visible(True)
            colum.set_resizable(True)
            colum.add_attribute()
            self.tree.append_column(colum)


# Instanciar
fiestra = Window()
# Posicion Ventana
fiestra.set_position(Gtk.WindowPosition.CENTER)
# Resizable
fiestra.set_resizable(True)
# Cierre on Click
fiestra.connect("delete-event", Gtk.main_quit)
# Mostrar ventana
fiestra.show_all()
# fiestra.set_decorated(True)
# Activar atencion de eventos
Gtk.main()
