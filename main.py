import shutil
import controller
from PySide2.QtWidgets import QApplication
from view import View
from telegram import Telegram
from time import sleep
from threading import Thread
import os
from models import Account, Report
from view_connections import Connections


class Main:
    def __init__(self):
        api_url = "https://softwarekeys.herokuapps.com"
        self.view = View(api_url)
        try:
            os.mkdir(os.path.join(controller.accountsFolder))
        except FileExistsError:
            pass
        self.onStart_event()

        #################
        Connections(self.view, self)
        #################

    def onStart_event(self):
        accounts = os.listdir(controller.accountsFolder)
        self.view.accounts_listwidget.addItems(accounts)

    def get_inputDialog_value(self):
        """validating the input dialog return"""
        res = self.view.input_dialog()
        if res is not False:
            Thread(target=self.add_account, kwargs={"name": res}).start()
        else:
            pass

    def add_account(self, name):
        self.view.setDisabled(True)
        Telegram.open(name)
        sleep(5)
        Telegram.close()
        self.view.setEnabled(True)
        self.view.accounts_listwidget.addItem(name)

    def remove_account(self):
        if self.view.accounts_listwidget.count() != 0:
            re = self.view.confirmMessage("Confirm removing", "Are you sure you want to remove this account?")
            if re:
                name = self.view.accounts_listwidget.currentItem().text()
                row = self.view.accounts_listwidget.currentRow()
                self.view.accounts_listwidget.takeItem(row)
                shutil.rmtree(os.path.join(controller.accountsFolder, name))


if __name__ == '__main__':
    app = QApplication()
    main = Main()
    app.exec_()
