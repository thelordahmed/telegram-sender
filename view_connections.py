
class Connections:
    def __init__(self, view_obj, main_obj):
        self.view = view_obj
        self.main = main_obj
        self.view.addAccount_btn.clicked.connect(self.main.get_inputDialog_value)
        self.view.removeAccount_btn.clicked.connect(self.main.remove_account)
        self.view.sheet_btn.clicked.connect(lambda: self.view.browse_singleFile_btn(self.view.sheet_le,
                                                                                    "choose the contacts source sheet",
                                                                                    "*.xlsx *.csv"))
        self.view.attachments_btn.clicked.connect(lambda: self.view.browse_multipleFiles_btn(self.view.attachments_le,
                                                                                             "choose attachmet files",
                                                                                             ""))
        self.view.pushButton.clicked.connect(lambda: self.view.appendToPlainTextBox(self.view.message_text, "{name}"))
        self.view.append_newmessage.clicked.connect(
            lambda: self.view.appendToPlainTextBox_newmessage(self.view.message_text))
        # Familiar
        self.view.sheet_btn_2.clicked.connect(lambda: self.view.browse_singleFile_btn(self.view.sheet_le_2,
                                                                                      "choose the contacts source sheet",
                                                                                      "*.xlsx *.csv"))
        self.view.attachments_btn_2.clicked.connect(
            lambda: self.view.browse_multipleFiles_btn(self.view.attachments_le_2,
                                                       "choose attachmet files",
                                                       ""))
        self.view.pushButton_2.clicked.connect(
            lambda: self.view.appendToPlainTextBox(self.view.message_text_2, "{name}"))
        self.view.append_newmessage_2.clicked.connect(
            lambda: self.view.appendToPlainTextBox_newmessage(self.view.message_text_2))
