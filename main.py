import csv
import shutil
from datetime import datetime, timedelta

from PySide2 import QtCore
from openpyxl import load_workbook
from selenium.common.exceptions import TimeoutException

import controller
from PySide2.QtWidgets import QApplication
from view import View
from telegram import Telegram
from time import sleep
from threading import Thread
import os
from view_connections import Connections
from models import Account, Session, ContactsAnony, ContactsFamiliar
from state_methods import State
from ast import literal_eval


# todo - (feature update) load the contacts to the interface in another thread

class Signals(QtCore.QObject):
    ok_message = QtCore.Signal(str, str)


class Main:
    def __init__(self):
        api_url = "https://softwarekeys.herokuapps.com"
        self.view = View(api_url)
        self.session = Session()
        self.state = State(self.view, self)
        self.signals = Signals()
        try:
            os.mkdir(os.path.join(controller.accountsFolder))
        except FileExistsError:
            pass
        self.onStart_event()

        #################
        Connections(self.view, self)
        #################

    def onStart_event(self):
        self.state.default_state()
        # loading accounts
        accounts = self.session.query(Account).all()
        for query in accounts:
            self.view.accounts_listwidget.addItem(query.name)
        # loading settings
        self.view.load_settings()
        # loading contacts
        contacts_anony = self.session.query(ContactsAnony).all()
        contacts_familiar = self.session.query(ContactsFamiliar).all()
        for cont_anony in contacts_anony:
            sender = cont_anony.sender.name if cont_anony.sender is not None else "--"
            if self.view.username_rb.isChecked():
                data = (cont_anony.name, sender, cont_anony.username, cont_anony.status)
            else:
                data = (cont_anony.name, sender, cont_anony.number, cont_anony.status)
            self.view.addToTableWidget(data, self.view.tableWidget)
        for cont_familiar in contacts_familiar:
            if self.view.username_rb_2.isChecked():
                data = (cont_familiar.name, cont_familiar.username, cont_familiar.status)
            else:
                data = (cont_familiar.name, cont_familiar.number, cont_familiar.status)
            self.view.addToTableWidget(data, self.view.tableWidget_2)

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
        account = Account(name=name)
        session = Session()
        session.add(account)
        session.commit()
        self.view.accounts_listwidget.addItem(name)

    def remove_account(self):
        if self.view.accounts_listwidget.count() != 0:
            re = self.view.confirmMessage("Confirm removing", "Are you sure you want to remove this account?")
            if re:
                name = self.view.accounts_listwidget.currentItem().text()
                row = self.view.accounts_listwidget.currentRow()
                self.view.accounts_listwidget.takeItem(row)
                shutil.rmtree(os.path.join(controller.accountsFolder, name))
                account = self.session.query(Account).filter_by(name=name).first()
                self.session.delete(account)
                self.session.commit()

    def import_contacts(self, mode: str):
        """
        :param mode: "anony" or "familiar"
        """
        if mode == "anony":
            contacts_table = ContactsAnony
            table_widget = self.view.tableWidget
            username_rb = self.view.username_rb
        else:
            contacts_table = ContactsFamiliar
            table_widget = self.view.tableWidget_2
            username_rb = self.view.username_rb_2
        # CONFIRMING STARTING A NEW SESSION IF DATA FOUND
        contacts_count = self.session.query(contacts_table).count()
        if contacts_count != 0:
            res = self.view.confirmMessage("Warning", "the current session data will be lost.\n"
                                                      "are you sure you wanna start a new session?", "warning")
        else:
            res = True
        if res:
            path = self.view.get_file_path("Choose the contacts source", "*.xlsx *.csv")
            if path == "":
                return None
            # RESETING AND ADDING DATA TO DB
            self.session.query(contacts_table).delete()
            self.session.commit()
            self.getDataFromSheet_toDB(path, mode)
            # UPDATING THE TABLEWIDGET
            contacts = self.session.query(contacts_table).all()
            table_widget.setRowCount(0)
            for contact in contacts:
                if mode == "anony":
                    sender = contact.sender.name if contact.sender is not None else "--"
                    if username_rb.isChecked():
                        data = (contact.name, sender, contact.username, contact.status)
                    else:
                        data = (contact.name, sender, contact.number, contact.status)
                else:
                    if username_rb.isChecked():
                        data = (contact.name, contact.username, contact.status)
                    else:
                        data = (contact.name, contact.number, contact.status)
                self.view.addToTableWidget(data, table_widget)

    def getDataFromSheet_toDB(self, path: str, mode: str):
        """
        this method will get data from sheet and add it to Contacts table
        * it will check first if number of data in sheet is not equal to number of data in table
          to check on newly added data on sheet when software restarts. if it's not equal, it will
          start adding the data and check on every object
        """
        if ".xlsx" in path:
            wb = load_workbook(path)
            sheet = wb.active
            data = sheet.values
            clean_data = []
            # removing the empty rows
            for row in data:
                if row[0] is not None or row[1] is not None:
                    clean_data.append(row)
            for name, numOrUsername in clean_data:
                if self.view.username_rb.isChecked():
                    if name is not None:
                        contact = ContactsAnony(name=name, username=numOrUsername,
                                                status="--") if mode == "anony" else ContactsFamiliar(name=name,
                                                                                                      username=numOrUsername,
                                                                                                      status="--")
                    else:
                        contact = ContactsAnony(username=numOrUsername,
                                                status="--") if mode == "anony" else ContactsFamiliar(
                            username=numOrUsername, status="--")
                else:
                    if name is not None:
                        contact = ContactsAnony(name=name, number=numOrUsername,
                                                status="--") if mode == "anony" else ContactsFamiliar(name=name,
                                                                                                      number=numOrUsername,
                                                                                                      status="--")
                    else:
                        contact = ContactsAnony(number=numOrUsername,
                                                status="--") if mode == "anony" else ContactsFamiliar(
                            number=numOrUsername, status="--")
                self.session.add(contact)
                self.session.commit()
        elif ".csv" in path:
            with open(path, encoding="utf-8") as csvf:
                data = csv.reader(csvf)
                for row in data:
                    # check if name column not empty
                    try:
                        name = row[0]
                        numOrUsername = row[1]
                    except IndexError:
                        name = None
                        numOrUsername = row[0]

                    if self.view.username_rb.isChecked():
                        if name is not None:
                            contact = ContactsAnony(name=name, username=numOrUsername,
                                                    status="--") if mode == "anony" else ContactsFamiliar(name=name,
                                                                                                          username=numOrUsername,
                                                                                                          status="--")
                        else:
                            contact = ContactsAnony(username=numOrUsername,
                                                    status="--") if mode == "anony" else ContactsFamiliar(
                                username=numOrUsername, status="--")
                    else:
                        if name is not None:
                            contact = ContactsAnony(name=name, number=numOrUsername,
                                                    status="--") if mode == "anony" else ContactsFamiliar(name=name,
                                                                                                          number=numOrUsername,
                                                                                                          status="--")
                        else:
                            contact = ContactsAnony(number=numOrUsername,
                                                    status="--") if mode == "anony" else ContactsFamiliar(
                                number=numOrUsername, status="--")
                    self.session.add(contact)
                    self.session.commit()

    def newSession(self, mode):
        if mode == "anony":
            if self.view.tableWidget.rowCount() != 0:
                re = self.view.confirmMessage("Confirmation", "Are you sure you want to start a new session?")
            else:
                re = False
            if re:
                self.session.query(Account).delete()
                self.session.query(ContactsAnony).delete()
                self.session.commit()
                self.view.tableWidget.setRowCount(0)
        else:
            if self.view.tableWidget_2.rowCount() != 0:
                re = self.view.confirmMessage("Confirmation", "Are you sure you want to start a new session?")
            else:
                re = False
            if re:
                self.session.query(ContactsFamiliar).delete()
                self.session.commit()
                self.view.tableWidget_2.setRowCount(0)


    def _sending_process(self, mode: str, number: str or None, username: str or None, message: str,
                         telegram_class: Telegram.__class__):
        """
        -- returns --
            "not found" : if number or username not found
            "channel" : if username is channel (unable to send)
            "connection lost" : if connection was lost

        """
        if mode == "anony":
            textFirst_rb = self.view.textFirst_rb
            paths = literal_eval(self.view.attachments_le.text())
        else:
            textFirst_rb = self.view.textFirst_rb_2
            paths = literal_eval(self.view.attachments_le.text())
        # CHECK CONNECTION
        if Telegram.network_still_connected():
            # SEARCH FOR NUMBER OR USERNAME
            if number is not None:
                if telegram_class.search_phone(number) is False:
                    return "not found"
            else:
                res = telegram_class.search_username(username)
                if res is False:
                    return "not found"
                elif res == "channel":
                    return "channel"
            # SENDING TEXT & ATTACHMENTS
            if textFirst_rb.isChecked():
                telegram_class.sending_text(message)
                telegram_class.sending_attachment(paths)
            else:
                telegram_class.sending_attachment(paths)
                telegram_class.sending_text(message)
        else:
            try:
                Telegram.wait_for_connection()
                self._sending_process(mode, number, username, message, telegram_class)
            except TimeoutException:
                return "connection lost"

    def _status_update(self, table_widget: View, contact: ContactsAnony or ContactsFamiliar, session: Session, number: str, username: str, status: str, column: int):
        # UPDATING STATUS IN DB
        contact.status = status
        session.commit()
        # UPDATING STATUS ON THE INTERFACE
        if number is not None:
            self.view.editItemInTableWidget(table_widget, number, status, column)
        else:
            self.view.editItemInTableWidget(table_widget, username, status, column)


    def process_anony(self):
        session = Session()
        self.view.save_settings(session)
        messages = self.view.messages_sb.value()
        accounts = session.query(Account).all()
        for acc in accounts:
            # TO CHECK REASON OF BREAKING CONTACTS LOOP
            loop_check = "Completed"  # "Completed" | "Error" | "Account Limit"
            if acc.sentCounter == messages:
                if (datetime.utcnow() - acc.sentDate) > timedelta(hours=24):
                    # RESET SENT COUNTER OF THE ACCOUNT
                    acc.sentCounter = 0
                    session.commit()
                else:
                    # SKIP TO NEXT ACCOUNT
                    continue
            # OPEN THE ACCOUNT BROWSER WINDOW
            Telegram.open(acc.name)
            # GET CONTACTS WITH STATUS "--"
            contacts = session.query(ContactsAnony).filter_by(status="--").all()
            # CONTACTS LOOP
            for contact in contacts:
                # CHECK IF ACCOUNT REACHED SENDING LIMIT
                if acc.sentCounter == messages:
                    acc.sentDate = datetime.utcnow()
                    session.commit()
                    loop_check = "Account Limit"
                    break
                # SENDING
                if self.view.username_rb.isChecked():
                    number = None
                    username = contact.username
                else:
                    number = contact.number
                    username = None
                message = self.view.message_text.toPlainText().replace("{name}", contact.name)
                res = self._sending_process("anony", number, username, message, Telegram)
                # SENDING ERRORS CHECK
                if res == "not found":
                    self._status_update(self.view.tableWidget, contact, session, number, username,
                                        "Not Found on Telegram!", 3)
                elif res == "channel":
                    self._status_update(self.view.tableWidget, contact, session, number, username,
                                        "Channel Found.. unable to send!", 3)
                elif res == "connection lost":
                    loop_check = "Error"
                    break
                else:
                    self._status_update(self.view.tableWidget, contact, session, number, username,
                                        "Message Sent!", 3)
                    # INCREASING SENT COUNER IN ACCOUNT
                    acc.sentCounter += 1
                    session.commit()

            # CLOSE THE CURRENT ACCOUNT IF LIMIT REACHED
            if loop_check == "Account Limit":
                Telegram.close()
                sleep(2)
            elif loop_check == "Error":
                self.signals.ok_message.emit("Error", "Connection was lost for more 1 hour\nPlease check your network then try again")
                break
            elif loop_check == "Completed":
                self.signals.ok_message.emit("Completed", "Session Completed Successfully ^_^")
                break


    def process_familiar(self):
        session = Session()
        self.view.save_settings(session)
        # loop on messages


if __name__ == '__main__':
    app = QApplication()
    main = Main()
    app.exec_()
