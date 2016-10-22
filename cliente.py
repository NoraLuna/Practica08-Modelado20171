import sys
from PyQt4 import QtGui, QtCore, uic

#clase principal
class MainWindow(QtGui.QMainWindow):
    #constructor de la clase
    def __init__(self):
        super(MainWindow, self).__init__()
        self.carga_cliente()
        self.tabla_tam()

    #Creamos una funcion para llamar el archivo .ui
    def carga_cliente(self):
        uic.loadUi('cliente.ui', self)

    #Creamos una funcion para redimensionar las celdas
    def tabla_tam(self):
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())