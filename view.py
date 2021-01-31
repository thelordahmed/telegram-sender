import os
import platform
from PySide2 import QtCore, QtGui
from PySide2.QtGui import QCloseEvent, Qt
from PySide2.QtWidgets import *
from webbrowser import open
# Import your design class
from design import Ui_MainWindow as design
import controller
from models import Session, Settings


class View(QMainWindow, design):
    def __init__(self, api_url, parent=None):
        super(View, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.show()
        # NEW SESSION BUTTON IS NOT NEEDED BECAUSE IMPORT CONTACTS BUTTON DO THE SAME TASK
        self.newSession_btn.hide()
        self.newSession_btn_2.hide()
        self.session = Session()
        self.state = "idle"
        self.api_url = api_url
        self.setWindowTitle(f"Telegram Bulk Sender {controller.version}")
        self.container_tabwid.tabBar().hide()
        # hidding all to validate license first
        # TODO - DEBUUGING
        # self.tabWidget_2.hide()
        self.license_frame.hide()
        self.adjustSize()
        self.commandLinkButton.setText(f"Copyright © 2020 {controller.copyright_text}")


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
            text = res[0].replace("/", "").replace("\\", "").replace("=", "").replace("-", "").replace("+", "").replace(
                "^", ""). \
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

    @staticmethod
    def editItemInTableWidget(tablewidget_object: QTableWidget, textToFind: str, value: str, column: int):
        item = tablewidget_object.findItems(textToFind, Qt.MatchEndsWith)[0]
        row = tablewidget_object.row(item)
        tablewidget_object.setItem(row, column, QTableWidgetItem(value))


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

    def get_file_path(self, title, extensions_range):
        path = QFileDialog.getOpenFileName(self, title, "", extensions_range)
        return path[0]

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

    def load_settings(self):
        settings = self.session.query(Settings).first()
        if settings is not None:
            if settings.anonyMode == 1:
                self.container_tabwid.setCurrentIndex(0)
            else:
                self.container_tabwid.setCurrentIndex(1)
            if settings.usernameModeAnony == 1:
                self.username_rb.setChecked(True)
            else:
                self.phone_rb.setChecked(True)
            if settings.usernameModeFamiliar == 1:
                self.username_rb_2.setChecked(True)
            else:
                self.phone_rb_2.setChecked(True)
            self.messages_sb.setValue(settings.messages)
            if settings.textFirstAnony == 1:
                self.textFirst_rb.setChecked(True)
            else:
                self.attachFirst_rb.setChecked(True)
            if settings.textFirstFamiliar == 1:
                self.textFirst_rb_2.setChecked(True)
            else:
                self.attachFirst_rb_2.setChecked(True)
            self.attachments_le.setText(settings.attachAnony)
            self.attachments_le_2.setText(settings.attachFamiliar)
            self.message_text.setPlainText(settings.messageAnony)
            self.message_text_2.setPlainText(settings.messageFamiliar)
            # updating the listwidget
            self.listWidget.setCurrentRow(self.container_tabwid.currentIndex())

    def save_settings(self, session: Session):
        anonyMode = 1 if self.anonymous.isVisible() else 0
        usernameAnony = 1 if self.username_rb.isChecked() else 0
        usernameFamiliar = 1 if self.username_rb_2.isChecked() else 0
        messages = self.messages_sb.value()
        textFirstAnony = 1 if self.textFirst_rb.isChecked() else 0
        textFirstFamiliar = 1 if self.textFirst_rb_2.isChecked() else 0
        attachAnony = self.attachments_le.text()
        attachFamiliar = self.attachments_le_2.text()
        messageAnony = self.message_text.toPlainText()
        messageFamiliar = self.message_text_2.toPlainText()
        settings = Settings(anonyMode=anonyMode,
                            usernameModeAnony=usernameAnony,
                            usernameModeFamiliar=usernameFamiliar,
                            messages=messages,
                            textFirstAnony=textFirstAnony,
                            textFirstFamiliar=textFirstFamiliar,
                            attachFamiliar=attachFamiliar,
                            attachAnony=attachAnony,
                            messageAnony=messageAnony,
                            messageFamiliar=messageFamiliar)
        session.query(Settings).delete()
        session.add(settings)
        session.commit()