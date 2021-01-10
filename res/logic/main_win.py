from PyQt5 import QtCore, QtGui, QtWidgets


class QMainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def closeEvent(self, event):
        self.parent.exit.exit_signal.emit()
        event.accept()
