from webbrowser import open

class Connections:
    def __init__(self, view_obj, main_obj):
        self.view = view_obj
        self.main = main_obj


        self.view.telegram_link.clicked.connect(lambda: open("http://my.telegram.org/"))
        self.view.connect_btn.clicked.connect(self.main.connect_btn_func)
        self.view.refresh_groups_btn.clicked.connect(self.main.connected_action)
        self.view.confirm_code_btn.clicked.connect(self.main.confirm_btn_func)
        self.view.output_btn.clicked.connect(lambda: self.view.output_le.setText(self.view.get_folder_path("choose the output folder")))
        self.view.extract_btn.clicked.connect(self.main.extract_group)
        self.main.signals.ok_message.connect(self.view.ok_message)
        self.view.addAccount_btn.clicked.connect(self.main.get_inputDialog_value)
        self.view.removeAccount_btn.clicked.connect(self.main.remove_account)
        self.view.sheet_btn.clicked.connect(lambda: self.main.import_contacts("anony"))
        self.view.attachments_btn.clicked.connect(lambda: self.view.browse_multipleFiles_btn(self.view.attachments_le,
                                                                                             "choose attachmet files",
                                                                                             ""))
        self.view.pushButton.clicked.connect(lambda: self.view.appendToPlainTextBox(self.view.message_text, "{name}"))
        self.view.append_newmessage.clicked.connect(
            lambda: self.view.appendToPlainTextBox_newmessage(self.view.message_text))
        # Familiar
        self.view.sheet_btn_2.clicked.connect(lambda: self.main.import_contacts("familiar"))
        self.view.attachments_btn_2.clicked.connect(
            lambda: self.view.browse_multipleFiles_btn(self.view.attachments_le_2,
                                                       "choose attachmet files",
                                                       ""))
        self.view.pushButton_2.clicked.connect(
            lambda: self.view.appendToPlainTextBox(self.view.message_text_2, "{name}"))
        self.view.append_newmessage_2.clicked.connect(
            lambda: self.view.appendToPlainTextBox_newmessage(self.view.message_text_2))

        self.view.start_btn.clicked.connect(lambda: self.main.start_event("anony"))
        self.view.start_btn_2.clicked.connect(lambda: self.main.start_event("familiar"))
        self.view.stop_btn.clicked.connect(lambda: self.main.stop_event("anony"))
        self.view.stop_btn_2.clicked.connect(lambda: self.main.stop_event("familiar"))
        self.view.newSession_btn.clicked.connect(lambda: self.main.newSession("anony"))
        self.view.newSession_btn_2.clicked.connect(lambda: self.main.newSession("familiar"))
        self.view.license_btn.clicked.connect(lambda: self.main.license.validate(self.view.license_le.text()))
        self.view.commandLinkButton.clicked.connect(self.view.copyrights)


