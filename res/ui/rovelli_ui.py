# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rovelli.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(447, 544)
        self.centralwidget = QtWidgets.QWidget(dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.settings_groupBox = QtWidgets.QGroupBox(self.frame)
        self.settings_groupBox.setObjectName("settings_groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.settings_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.calendar_type_comboBox = QtWidgets.QComboBox(self.settings_groupBox)
        self.calendar_type_comboBox.setObjectName("calendar_type_comboBox")
        self.calendar_type_comboBox.addItem("")
        self.calendar_type_comboBox.addItem("")
        self.gridLayout_4.addWidget(self.calendar_type_comboBox, 0, 1, 1, 1)
        self.calendar_type_label = QtWidgets.QLabel(self.settings_groupBox)
        self.calendar_type_label.setObjectName("calendar_type_label")
        self.gridLayout_4.addWidget(self.calendar_type_label, 0, 0, 1, 1)
        self.pre_defined_label = QtWidgets.QLabel(self.settings_groupBox)
        self.pre_defined_label.setObjectName("pre_defined_label")
        self.gridLayout_4.addWidget(self.pre_defined_label, 1, 0, 1, 1)
        self.predefined_comboBox = QtWidgets.QComboBox(self.settings_groupBox)
        self.predefined_comboBox.setObjectName("predefined_comboBox")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.predefined_comboBox.addItem("")
        self.gridLayout_4.addWidget(self.predefined_comboBox, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.description_checkBox = QtWidgets.QCheckBox(self.settings_groupBox)
        self.description_checkBox.setObjectName("description_checkBox")
        self.gridLayout_3.addWidget(self.description_checkBox, 2, 0, 1, 1)
        self.char_settings_groupBox = QtWidgets.QGroupBox(self.settings_groupBox)
        self.char_settings_groupBox.setCheckable(True)
        self.char_settings_groupBox.setChecked(False)
        self.char_settings_groupBox.setObjectName("char_settings_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.char_settings_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.passed_label = QtWidgets.QLabel(self.char_settings_groupBox)
        self.passed_label.setObjectName("passed_label")
        self.gridLayout.addWidget(self.passed_label, 0, 0, 1, 1)
        self.passed_lineEdit = QtWidgets.QLineEdit(self.char_settings_groupBox)
        self.passed_lineEdit.setClearButtonEnabled(True)
        self.passed_lineEdit.setObjectName("passed_lineEdit")
        self.gridLayout.addWidget(self.passed_lineEdit, 0, 1, 1, 1)
        self.remaining_label = QtWidgets.QLabel(self.char_settings_groupBox)
        self.remaining_label.setObjectName("remaining_label")
        self.gridLayout.addWidget(self.remaining_label, 1, 0, 1, 1)
        self.remaining_lineEdit = QtWidgets.QLineEdit(self.char_settings_groupBox)
        self.remaining_lineEdit.setClearButtonEnabled(True)
        self.remaining_lineEdit.setObjectName("remaining_lineEdit")
        self.gridLayout.addWidget(self.remaining_lineEdit, 1, 1, 1, 1)
        self.length_label = QtWidgets.QLabel(self.char_settings_groupBox)
        self.length_label.setObjectName("length_label")
        self.gridLayout.addWidget(self.length_label, 2, 0, 1, 1)
        self.length_spinBox = QtWidgets.QSpinBox(self.char_settings_groupBox)
        self.length_spinBox.setMinimum(5)
        self.length_spinBox.setMaximum(1000)
        self.length_spinBox.setProperty("value", 10)
        self.length_spinBox.setObjectName("length_spinBox")
        self.gridLayout.addWidget(self.length_spinBox, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.char_settings_groupBox, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.settings_groupBox, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.progress_textEdit = QtWidgets.QTextEdit(self.frame)
        self.progress_textEdit.setMinimumSize(QtCore.QSize(0, 150))
        self.progress_textEdit.setObjectName("progress_textEdit")
        self.gridLayout_5.addWidget(self.progress_textEdit, 0, 1, 1, 1)
        self.progress_label = QtWidgets.QLabel(self.frame)
        self.progress_label.setObjectName("progress_label")
        self.gridLayout_5.addWidget(self.progress_label, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.save_pushButton.setObjectName("save_pushButton")
        self.gridLayout_7.addWidget(self.save_pushButton, 0, 2, 1, 1)
        self.generate_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.gridLayout_7.addWidget(self.generate_pushButton, 0, 0, 1, 1)
        self.about_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.about_pushButton.setObjectName("about_pushButton")
        self.gridLayout_7.addWidget(self.about_pushButton, 0, 7, 1, 1)
        self.copy_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.copy_pushButton.setObjectName("copy_pushButton")
        self.gridLayout_7.addWidget(self.copy_pushButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 8, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        dialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.calendar_type_comboBox, self.predefined_comboBox)
        dialog.setTabOrder(self.predefined_comboBox, self.char_settings_groupBox)
        dialog.setTabOrder(self.char_settings_groupBox, self.passed_lineEdit)
        dialog.setTabOrder(self.passed_lineEdit, self.remaining_lineEdit)
        dialog.setTabOrder(self.remaining_lineEdit, self.length_spinBox)
        dialog.setTabOrder(self.length_spinBox, self.description_checkBox)
        dialog.setTabOrder(self.description_checkBox, self.progress_textEdit)
        dialog.setTabOrder(self.progress_textEdit, self.generate_pushButton)
        dialog.setTabOrder(self.generate_pushButton, self.copy_pushButton)
        dialog.setTabOrder(self.copy_pushButton, self.save_pushButton)
        dialog.setTabOrder(self.save_pushButton, self.about_pushButton)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Year Progress"))
        self.settings_groupBox.setTitle(_translate("dialog", "Settings"))
        self.calendar_type_comboBox.setItemText(0, _translate("dialog", "Gregorian"))
        self.calendar_type_comboBox.setItemText(1, _translate("dialog", "Jalali"))
        self.calendar_type_label.setText(_translate("dialog", "Calendar Type:"))
        self.pre_defined_label.setText(_translate("dialog", "Progress Bar Type:"))
        self.predefined_comboBox.setItemText(0, _translate("dialog", "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜"))
        self.predefined_comboBox.setItemText(1, _translate("dialog", "██████░░░░░░"))
        self.predefined_comboBox.setItemText(2, _translate("dialog", "██████▁▁▁▁▁▁"))
        self.predefined_comboBox.setItemText(3, _translate("dialog", "⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣀"))
        self.predefined_comboBox.setItemText(4, _translate("dialog", "■■■■■■□□□□□□"))
        self.predefined_comboBox.setItemText(5, _translate("dialog", "⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜"))
        self.predefined_comboBox.setItemText(6, _translate("dialog", "▰▰▰▰▰▰▱▱▱▱▱▱"))
        self.predefined_comboBox.setItemText(7, _translate("dialog", "◼◼◼◼◼◼▭▭▭▭▭▭"))
        self.predefined_comboBox.setItemText(8, _translate("dialog", "▮▮▮▮▮▮▯▯▯▯▯▯"))
        self.predefined_comboBox.setItemText(9, _translate("dialog", "⬤⬤⬤⬤⬤⬤◯◯◯◯◯◯"))
        self.predefined_comboBox.setItemText(10, _translate("dialog", "⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪"))
        self.predefined_comboBox.setItemText(11, _translate("dialog", "+++++++++++------------------"))
        self.predefined_comboBox.setItemText(12, _translate("dialog", "|||||||||||||---------------"))
        self.description_checkBox.setText(_translate("dialog", "Show Descriptions"))
        self.char_settings_groupBox.setTitle(_translate("dialog", "Cutstom Progress Bar:"))
        self.passed_label.setText(_translate("dialog", "Passed:"))
        self.passed_lineEdit.setText(_translate("dialog", "█"))
        self.remaining_label.setText(_translate("dialog", "Remaining:"))
        self.remaining_lineEdit.setText(_translate("dialog", "░"))
        self.length_label.setText(_translate("dialog", "Length:"))
        self.progress_label.setText(_translate("dialog", "Progress:"))
        self.save_pushButton.setText(_translate("dialog", "Save"))
        self.generate_pushButton.setText(_translate("dialog", "Generate"))
        self.about_pushButton.setText(_translate("dialog", "About"))
        self.copy_pushButton.setText(_translate("dialog", "Copy"))


