from PyQt5 import QtCore, QtGui, QtWidgets


def warning(widget, title, message):
    "shows a warning"
    button = QtWidgets.QMessageBox.Ok
    QtWidgets.QMessageBox.warning(widget, title, message, button)


def error(widget, title, message):
    "shows an error"
    button = QtWidgets.QMessageBox.Ok
    QtWidgets.QMessageBox.critical(widget, title, message, button)


def question(widget, title, message):
    '''
    ask a question and returns true or false
    true  -> yes
    false -> no
    '''
    button = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
    answer = QtWidgets.QMessageBox.question(widget, title, message, button)
    if answer == QtWidgets.QMessageBox.No:
        return False
    elif answer == QtWidgets.QMessageBox.Yes:
        return True


def info(widget, title, message):
    "shows an info message"
    button = QtWidgets.QMessageBox.Ok
    QtWidgets.QMessageBox.question(widget, title, message, button)


def about(widget):
    message = """
Rovelli is a free GUI tool for generating an overview of the <br>
current year and also a progress bar that visualizes this overview.<br>
The name Rovelli is derived from the famous Italian physicist,<br>
Carlo Rovelli, that based on his theory time is an illusion!<br><br>
Developed by Aref Alikhani.<br><br>
Follow Me:<br>
<a href="https://github.com/ArefDev">GitHub</a><br>
<a href="https://twitter.com/ArefDev">Twitter</a><br><br>
For donation <a href="https://github.com/ArefDev/Rovelli#donation"> click </a> here.<br><br>
Rovelli is distributed under the GPLv2 license.
"""
    info(widget, 'About...', message)
