import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk
from BD.ConexionBD import ConexionBD

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='FileMenu'>
      <menu action='FileNew'>
        <menuitem action='FileNewStandard' />
        <menuitem action='FileNewFoo' />
        <menuitem action='FileNewGoo' />
      </menu>
      <separator />
      <menuitem action='FileQuit' />
    </menu>
    <menu action='EditMenu'>
      <menuitem action='EditCopy' />
      <menuitem action='EditPaste' />
      <menuitem action='EditSomething' />
    </menu>
    <menu action='ChoicesMenu'>
      <menuitem action='ChoiceOne'/>
      <menuitem action='ChoiceTwo'/>
      <separator />
      <menuitem action='ChoiceThree'/>
    </menu>
  </menubar>
  <toolbar name='ToolBar'>
    <toolitem action='FileNewStandard' />
    <toolitem action='FileQuit' />
  </toolbar>
  <popup name='PopupMenu'>
    <menuitem action='EditCopy' />
    <menuitem action='EditPaste' />
    <menuitem action='EditSomething' />
  </popup>
</ui>
"""


class WindowC(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cliente")
        self.set_border_width(10)
        self.set_default_size(500, 100)
        self.conn = ConexionBD()

        # LayoutBox
        self.box = Gtk.Box(spacing=6)
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.box.set_border_width(1)
        self.add(self.box)

        # Menu
        action_group = Gtk.ActionGroup("my_actions")
        self.add_file_menu_actions(action_group)
        self.add_edit_menu_actions(action_group)
        self.add_choices_menu_actions(action_group)
        self.ui_manager = self.create_ui_manager()
        self.ui_manager.insert_action_group(action_group)
        self.menubar = self.ui_manager.get_widget("/MenuBar")
        self.box.pack_start(self.menubar, False, False, 0)

        # ListBox
        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)
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

        # Toolbar
        toolbar = self.ui_manager.get_widget("/ToolBar")
        self.v_box1.add(toolbar)

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
        self.b_comprar = Gtk.Button(label="Comprar", stock=Gtk.STOCK_ADD)
        self.b_consultar = Gtk.Button(label="Consultar", stock=Gtk.STOCK_INFO)
        self.b_salir = Gtk.Button(label="Salir", stock=Gtk.STOCK_QUIT)

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
                self.conn.update(ustock, id)
                self.consultar(None)

    def cerrar(self, button):
        """Cierra el programa"""
        self.close()
        self.conn.close()

    def add_file_menu_actions(self, action_group):
        """Añade acciones al menu File.

        :param action_group:

        """
        action_filemenu = Gtk.Action("FileMenu", "File", None, None)
        action_group.add_action(action_filemenu)

        action_filenewmenu = Gtk.Action("FileNew", None, None, Gtk.STOCK_NEW)
        action_group.add_action(action_filenewmenu)

        action_new = Gtk.Action("FileNewStandard", "_New",
                                "Create a new file", Gtk.STOCK_NEW)
        action_new.connect("activate", self.on_menu_file_new_generic)
        action_group.add_action_with_accel(action_new, None)

        action_group.add_actions([
            ("FileNewFoo", None, "New Foo", None, "Create new foo",
             self.on_menu_file_new_generic),
            ("FileNewGoo", None, "_New Goo", None, "Create new goo",
             self.on_menu_file_new_generic),
        ])

        action_filequit = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
        action_filequit.connect("activate", self.on_menu_file_quit)
        action_group.add_action(action_filequit)

    def add_edit_menu_actions(self, action_group):
        """Añade acciones al menu Editar.

        :param action_group:
        """
        action_group.add_actions([
            ("EditMenu", None, "Edit"),
            ("EditCopy", Gtk.STOCK_COPY, None, None, None,
             self.on_menu_others),
            ("EditPaste", Gtk.STOCK_PASTE, None, None, None,
             self.on_menu_others),
            ("EditSomething", None, "Something", "<control><alt>S", None,
             self.on_menu_others)
        ])

    def add_choices_menu_actions(self, action_group):
        """Añade acciones al menu Choices.

        :param action_group:
        """
        action_group.add_action(Gtk.Action("ChoicesMenu", "Choices", None,
                                           None))

        action_group.add_radio_actions([
            ("ChoiceOne", None, "One", None, None, 1),
            ("ChoiceTwo", None, "Two", None, None, 2)
        ], 1, self.on_menu_choices_changed)

        three = Gtk.ToggleAction("ChoiceThree", "Three", None, None)
        three.connect("toggled", self.on_menu_choices_toggled)
        action_group.add_action(three)

    def create_ui_manager(self):
        """Enlaza el xml UI con las acciones de los menus


        """
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager

    def on_menu_file_new_generic(self, widget):
        """Boton new del menu
        Llama al metodo informe de la clase ConexionBD
        :param widget:

        """
        self.conn.informe()

    def on_menu_file_quit(self, widget):
        """Cierra la ventana

        :param widget:

        """
        Gtk.main_quit()

    def on_menu_others(self, widget):
        """Boton menu others

        :param widget:
        """
        print("Menu item " + widget.get_name() + " was selected")

    def on_menu_choices_changed(self, widget, current):
        """Boton menu opciones cambiadas

        :param widget:
        """
        print(current.get_name() + " was selected.")

    def on_menu_choices_toggled(self, widget):
        """Boton menu opciones

        :param widget:
        """
        if widget.get_active():
            print(widget.get_name() + " activated")
        else:
            print(widget.get_name() + " deactivated")
