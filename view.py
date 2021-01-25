import os
import platform
from PySide2 import QtCore, QtGui
from PySide2.QtGui import QCloseEvent, Qt
from PySide2.QtWidgets import *
from webbrowser import open
# Import your design class
from design import Ui_MainWindow as design
import controller


class View(QMainWindow, design):
    def __init__(self, api_url, parent=None):
        super(View, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.show()
        self.state = "idle"
        self.api_url = api_url
        self.setWindowTitle(f"Telegram Bulk Sender {controller.version}")
        self.stop_state()
        # hidding all to validate license first
        # TODO - DEBUUGING
        # self.tabWidget_2.hide()
        self.license_frame.hide()
        self.adjustSize()

        self.commandLinkButton.setText(f"Copyright © 2020 {controller.copyright_text}")


    ######################################
    ######### SLOTS ######################


    def start_state(self):
        self.state = "started"
        self.start_btn.setDisabled(True)
        self.stop_btn.setEnabled(True)
        if self.anonymous.isVisible():
            self.tabWidget.setCurrentIndex(2)
            self.familiar.setDisabled(True)
        else:
            self.tabWidget_2.setCurrentIndex(1)
            self.anonymous.setDisabled(True)


    def stop_state(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setDisabled(True)
        self.familiar.setEnabled(True)
        self.anonymous.setEnabled(True)
        if self.state != "idle":
            self.state = "stopped"

    @staticmethod
    def copyrights():
        open(controller.copyright_url)

    ######################################

    # Customizing the close event
    def closeEvent(self, event: QCloseEvent):
        if platform.system() == "Darwin":
            os.system("killall chromedriver")
            os.system("killall 'Google Chrome'")
        else:
            os.system("taskkill /t /F /im chromedriver.exe")

    def input_dialog(self):
        res = QInputDialog.getText(self, "Add account", "Type an account name or its number")
        if res[0] != "":
            text = res[0].replace("/", "").replace("\\", "").replace("=", "").replace("-", "").replace("+", "").replace("^", "").\
                replace("_", "").replace("%", "").replace("&", "").replace("*", "")
            return text
        else:
            return False

    @staticmethod
    def addToTableWidget(data: tuple, tablewidget_object: QTableWidget):  # slot >> trigger singal
        """
        Use this method if you have TableWidget to add items in rows
        """
        row_pos = tablewidget_object.rowCount()
        tablewidget_object.insertRow(row_pos)

        for index, info in enumerate(data):
            tablewidget_object.setItem(row_pos, index, QTableWidgetItem(info))
            tablewidget_object.scrollToBottom()


    def confirmMessage(self, title: str, text: str, mode="question"):
        """
        use this method to show a confirm dialog
        :return: True if yes clicked - False if No clicked
        """
        if mode == "warning":
            re = QMessageBox.warning(self, title, text, QMessageBox.Yes | QMessageBox.No)
        else:
            re = QMessageBox.question(self, title, text, QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:
            return True
        else:
            return False

    def ok_message(self, title, text):
        QMessageBox.information(self, title, text, QMessageBox.Ok)

    def saveDialog(self):
        """:return saving path"""
        path = QFileDialog.getSaveFileName(self, "save data", "data", "*.csv")
        return path[0]


    def browse_singleFile_btn(self, lineedit_object: QLineEdit, title: str, extensions_range: str = ""):
        """
        use this on the browser button to get a file path and pass it to QLineEdit
        :return a tuple (path, file extension)
        """
        widget = lineedit_object
        path = QFileDialog.getOpenFileName(self, title, "", extensions_range)
        widget.setText(path[0])


    def browse_multipleFiles_btn(self, lineedit_object: QLineEdit, title: str, extensions_range: str = ""):
        """:return a tuple (path, file extension)"""
        path = QFileDialog.getOpenFileNames(self, title, "", extensions_range)
        if len(path[0]) > 0:
            lineedit_object.setText(str(path[0]))


    @staticmethod
    def appendToPlainTextBox(plaintextedit_object: QPlainTextEdit, text: str):
        plaintextedit_object.insertPlainText(text)

    @staticmethod
    def appendToPlainTextBox_newmessage(plaintextedit_object: QPlainTextEdit):
        plaintextedit_object.insertPlainText("\n\n\n{new message}\n\n")
        plaintextedit_object.moveCursor(QtGui.QTextCursor.End)

    def changeStateToStopped(self):
        self.statusbar.showMessage(f"   >> Stopping in progress... <<")
        self.state = "stopped"

    def loadInterfaceValues(self, data):
        """
        :param data: list of tuples
        :return: None
        """
        if len(data) != 0:
            values = data[-1]
            self.sheet_le.setText(values[0])
            self.messages_sbox.setValue(int(values[1]))
            self.minutes_sbox.setValue(int(values[2]))
            if values[3] == 1:
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
            self.attachments_le.setText(values[4])
            self.message_text.setPlainText(values[5])
            self.contactCard_le.setText(values[6])



