__author__ = 'oquintansocampo'

from distutils.core import setup

setup(name="Aplicacion de componentes",
      version="1.0",
      description="Interfaz grafica para comprar componentes",
      author="Oscar Quintans",
      author_email="oquintansocampo@danielcastelao.org",
      license="GPL",
      scripts=["Main.py"],
      py_modules=["ConexionBD","Componentes","Main","VentanaAdmin","VentanaCliente","VentanaLogin"]
      )
