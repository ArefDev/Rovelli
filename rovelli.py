# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from res.logic.main_win import QMainWindow
from res.ui import rovelli_ui
from res.logic import messages
import datetime
import jdatetime
import pyperclip
import sqlite3


def init(dialog, self):
    self.about_pushButton.clicked.connect(
        lambda: messages.about(dialog)
        )
    self.generate_pushButton.clicked.connect(
        lambda: generate(dialog, self)
        )
    self.predefined_comboBox.currentIndexChanged.connect(
        lambda: set_chars(dialog, self)
        )
    self.copy_pushButton.clicked.connect(
        lambda: copy(dialog, self)
        )
    self.save_pushButton.clicked.connect(
        lambda: save(dialog, self)
        )
    self.calendar_type_comboBox.currentTextChanged.connect(
        lambda: generate(dialog, self)
        )
    self.predefined_comboBox.currentTextChanged.connect(
        lambda: generate(dialog, self)
        )
    self.char_settings_groupBox.clicked.connect(
        lambda: generate(dialog, self)
        )
    self.passed_lineEdit.textChanged.connect(
        lambda: generate(dialog, self)
        )
    self.remaining_lineEdit.textChanged.connect(
        lambda: generate(dialog, self)
        )
    self.length_spinBox.valueChanged.connect(
        lambda: generate(dialog, self)
        )
    self.description_checkBox.clicked.connect(
        lambda: generate(dialog, self)
        )
    self.exit = ExitSignal()
    self.exit.exit_signal.connect(
        lambda: close(dialog, self)
        )
    connect_to_database(dialog, self)
    set_settings(dialog, self)
    generate(dialog, self)


def connect_to_database(dialog, self):
    self.conn = sqlite3.connect('res/settings.db')
    self.cursor = self.conn.cursor()


def generate(dialog, self):
    custom = self.char_settings_groupBox.isChecked()
    if custom:
        passed_char = self.passed_lineEdit.text()
        remaining_char = self.remaining_lineEdit.text()
        length = self.length_spinBox.value()
    else:
        passed_char, remaining_char = get_chars(dialog, self)
        length = 10
    calendar_type = self.calendar_type_comboBox.currentText()
    if calendar_type == 'Gregorian':
        current_date = datetime.datetime.now()
        leap = QtCore.QDate.isLeapYear(int(current_date.year))
    else:
        current_date = jdatetime.datetime.now()
        leap = current_date.isleap()
    current_day = int(current_date.strftime("%j"))
    if leap:
        total_days = 366
    else:
        total_days = 365
    if passed_char == '':
        passed_char = '⬛'
    if remaining_char == '':
        remaining_char = '⬜'
    progress = (current_day * length) / total_days
    progress_bar = int(progress) * passed_char
    progress_bar = progress_bar.ljust(length, remaining_char)
    year = current_date.strftime("%Y")
    remaining = total_days - current_day
    description_checked = self.description_checkBox.isChecked()
    if description_checked:
        description = get_description(
            year,
            current_day,
            remaining,
            calendar_type,
            leap
            )
    else:
        description = ''
    info = 'Developed by @ArefDev :)'
    percentage = current_day/total_days * 100
    description = '\n'.join(description)
    percentage = str(round(percentage, 2))
    if calendar_type == 'Jalali':
        description = convert_to_persian(dialog, self, description)
        percentage = convert_to_persian(dialog, self, percentage, True)
    text = '{description}\n{progress} {percentage}%\n\n{info}'.format(
        description=description,
        progress=progress_bar,
        percentage=percentage,
        info=info
    )
    self.progress_textEdit.setText(text.strip())


def get_chars(dialog, self):
    chars = self.predefined_comboBox.currentText()
    return chars[0], chars[-1]


def set_chars(dialog, self):
    checked = self.char_settings_groupBox.isChecked()
    if checked:
        passed_char, remaining_char = get_chars(dialog, self)
        self.passed_lineEdit.setText(passed_char)
        self.remaining_lineEdit.setText(remaining_char)


def get_description(year, passed, remaining, calendar_type, leap):
    if calendar_type == 'Gregorian':
        title = 'Overview of the Year {}'.format(year)
        passed_unit, remaining_unit = tuple(
            map(
                lambda value: 'Day' if value <= 1 else 'Days',
                (passed, remaining)
                )
            )
        passed = 'Passed: {} {}'.format(passed, passed_unit)
        remain = 'Remaining: {} {}'.format(remaining, remaining_unit)
        if leap:
            leap = ''
        else:
            leap = 'not'
        leap = '{} is {} a leap year.'.format(year, leap)
    else:
        title = 'وضعیت سال {}'.format(year)
        passed = 'گذشته: {} روز'.format(passed)
        remain = ' باقی‌مانده: {} روز'.format(remaining)
        if leap:
            leap = 'است'
        else:
            leap = 'نیست'
        leap = 'سال {} کبیسه {}.'.format(year, leap)
    return title.strip(), passed.strip(), remain.strip(), leap.strip()


def copy(dialog, self):
    text = self.progress_textEdit.toPlainText()
    pyperclip.copy(text)
    message = 'Text has been copied to the clipboard.'
    messages.info(dialog, 'Info', message)


def convert_to_persian(dialog, self, text, percentage=False):
    PERSIAN_NUMS = '۰۱۲۳۴۵۶۷۸۹'
    for char in text:
        if char.isdigit():
            value = int(char)
            text = text.replace(char, PERSIAN_NUMS[value])
    if percentage:
        text = text.replace('.', '/')
    return text


def save(dialog, self, close=False):
    calendar_type = self.calendar_type_comboBox.currentText()
    progress_bar_type = self.predefined_comboBox.currentIndex()
    custom = int(self.char_settings_groupBox.isChecked())
    passed_char = self.passed_lineEdit.text()
    remaining_char = self.remaining_lineEdit.text()
    length = self.length_spinBox.value()
    description = int(self.description_checkBox.isChecked())
    update_settings(self, 'calendar_type', calendar_type)
    update_settings(self, 'progress_bar_type', progress_bar_type)
    update_settings(self, 'custom', custom)
    update_settings(self, 'passed_char', passed_char)
    update_settings(self, 'remaining_char', remaining_char)
    update_settings(self, 'length', length)
    update_settings(self, 'description', description)
    if not close:
        message = 'Changes has been saved to the database!'
        messages.info(dialog, 'Info', message)


def set_settings(dialog, self):
    calendar_type = fetch_settings(self, 'calendar_type')
    progress_bar_type = int(fetch_settings(self, 'progress_bar_type'))
    custom = int(fetch_settings(self, 'custom'))
    passed_char = fetch_settings(self, 'passed_char')
    remaining_char = fetch_settings(self, 'remaining_char')
    length = int(fetch_settings(self, 'length'))
    description = int(fetch_settings(self, 'description'))
    self.calendar_type_comboBox.setCurrentText(calendar_type)
    self.predefined_comboBox.setCurrentIndex(progress_bar_type)
    if custom:
        self.char_settings_groupBox.setChecked(True)
    self.passed_lineEdit.setText(passed_char)
    self.remaining_lineEdit.setText(remaining_char)
    self.length_spinBox.setValue(length)
    if description:
        self.description_checkBox.setChecked(True)


def fetch_settings(self, option):
    sql = 'SELECT value FROM settings WHERE option="{}";'.format(option)
    self.cursor.execute(sql)
    option = self.cursor.fetchall()[0][0]
    return option


def update_settings(self, option, value):
    sql = 'UPDATE settings set value="{}" WHERE option="{}"'.format(
        value,
        option
        )
    self.cursor.execute(sql)
    self.conn.commit()


def close(dialog, self):
    message = 'Do you want to save the changes?'
    yes = messages.question(dialog, 'Confirmation', message)
    if yes:
        save(dialog, self, True)


class ExitSignal(QtCore.QObject):
    exit_signal = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QObject.__init__(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = rovelli_ui.Ui_dialog()
    dialog = QMainWindow(ui)
    ui.setupUi(dialog)
    init(dialog, ui)
    dialog.show()
    sys.exit(app.exec_())
