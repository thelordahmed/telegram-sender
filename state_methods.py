from threading import Thread


class State:
    def __init__(self, view, main):
        self.view = view
        self.main = main

    def default_state(self):
        self.view.listWidget.setCurrentRow(self.view.container_tabwid.currentIndex())
        self.view.tabWidget_2.setCurrentIndex(0)
        self.view.tabWidget.setCurrentIndex(0)
        self.view.stop_btn.setDisabled(True)
        self.view.stop_btn_2.setDisabled(True)

    def start_state(self, mode):
        if mode == "anony":
            start_btn = self.view.start_btn
            stop_btn = self.view.stop_btn
            tab_item_toDisable = self.view.familiar
            self.view.tabWidget.setCurrentIndex(2)
        else:
            start_btn = self.view.start_btn_2
            stop_btn = self.view.stop_btn_2
            tab_item_toDisable = self.view.anonymous
            self.view.tabWidget_2.setCurrentIndex(1)
        start_btn.setDisabled(True)
        stop_btn.setEnabled(True)
        tab_item_toDisable.setDisabled(True)


    def stop_state(self, mode):
        if mode == "anony":
            start_btn = self.view.start_btn
            stop_btn = self.view.stop_btn
            tab_item_toEnable = self.view.familiar
        else:
            start_btn = self.view.start_btn_2
            stop_btn = self.view.stop_btn_2
            tab_item_toEnable = self.view.anonymous
        start_btn.setEnabled(True)
        stop_btn.setDisabled(True)
        stop_btn.setText("")
        tab_item_toEnable.setEnabled(True)

