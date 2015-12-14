from DistUpgrade.GtkProgress import GtkAcquireProgress
from gi.repository import Gtk
from BD.ConexionBD import ConexionBD


class WindowC(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cliente")
        self.set_border_width(10)
        self.set_default_size(500, 100)
        self.conn = ConexionBD()

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
        self.model = Gtk.ListStore(str, str, str, str, int, int, int)
        self.tree = Gtk.TreeView(self.model)

        # TreeViewColumn
        cellRenderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("ID", cellRenderer, text=0)
        column2 = Gtk.TreeViewColumn("Tipo", cellRenderer, text=1)
        column3 = Gtk.TreeViewColumn("Marca", cellRenderer, text=2)
        column4 = Gtk.TreeViewColumn("Modelo", cellRenderer, text=3)
        column5 = Gtk.TreeViewColumn("Precio", cellRenderer, text=4)
        column6 = Gtk.TreeViewColumn("U.Stock", cellRenderer, text=5)
        column7 = Gtk.TreeViewColumn("U.Almacen", cellRenderer, text=6)
        self.tree.append_column(column)
        self.tree.append_column(column2)
        self.tree.append_column(column3)
        self.tree.append_column(column4)
        self.tree.append_column(column5)
        self.tree.append_column(column6)
        self.tree.append_column(column7)

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

        # ComboBox
        self.cbTipo = Gtk.ComboBoxText()
        self.cbMarca = Gtk.ComboBoxText()
        self.cbPrecio = Gtk.ComboBoxText()

        self.cbTipo.insert_text(0, "Tipo")
        self.cbTipo.insert_text(1, "Procesador")
        self.cbTipo.insert_text(2, "T. Grafica")
        self.cbTipo.insert_text(3, "RAM")
        self.cbTipo.insert_text(4, "HDD")
        self.cbTipo.insert_text(5, "Placa Base")

        self.cbMarca.insert_text(0, "Marca")
        self.cbMarca.insert_text(1, "ASUS")
        self.cbMarca.insert_text(2, "Intel")
        self.cbMarca.insert_text(3, "AMD")
        self.cbMarca.insert_text(4, "MSI")
        self.cbMarca.insert_text(5, "GigaByte")

        self.cbPrecio.insert_text(0, "Precio <")
        self.cbPrecio.insert_text(1, "20")
        self.cbPrecio.insert_text(2, "50")
        self.cbPrecio.insert_text(3, "100")
        self.cbPrecio.insert_text(4, "200")
        self.cbPrecio.insert_text(5, "500")

        self.cbTipo.set_active(0)
        self.cbMarca.set_active(0)
        self.cbPrecio.set_active(0)

        # Botones
        self.b_comprar = Gtk.Button(label="Comprar")
        self.b_consultar = Gtk.Button(label="Consultar")
        self.b_salir = Gtk.Button(label="Salir")

        self.b_comprar.connect("clicked", self.comprar)
        self.b_consultar.connect("clicked", self.consultar)
        self.b_salir.connect("clicked", self.cerrar)

        self.v_box2.add(self.cbTipo)
        self.v_box2.add(self.cbMarca)
        self.v_box2.add(self.cbPrecio)

        self.v_box3.add(self.b_comprar)
        self.v_box3.add(self.b_consultar)
        self.v_box3.add(self.b_salir)

        self.list_box.add(self.row1)
        self.list_box.add(self.row2)
        self.list_box.add(self.row3)
        self.list_box.add(self.tree)

    def consultar(self, button):
        """Consuta en la base de datos e introduce los datos en el TreeView"""
        mod = Gtk.ListStore(str, str, str, str, int, int, int)
        for i in self.conn.select2(self.cbTipo.get_active_text(), self.cbMarca.get_active_text(),
                                   self.cbPrecio.get_active_text()):
            mod.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        self.model = mod
        self.tree.set_model(self.model)

    def comprar(self, button):
        """Compra una unidad reduciendo en uno la cantidad en stock"""
        click = self.tree.get_selection()
        model, treeiter = click.get_selected()
        if treeiter != None:
            ustock = model[treeiter][5]
            if (ustock > 0):
                id = model[treeiter][0]
                self.conn.update(ustock,id)
                self.consultar(None)

    def cerrar(self, button):
        """Cierra el programa"""
        self.close()
        self.conn.close()
