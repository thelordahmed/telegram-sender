from threading import Thread


class State:
    def __init__(self, view, main):
        self.view = view
        self.main = main

    def default_state(self):
        self.view.container_tabwid.setCurrentIndex(1)
        self.view.tabWidget_2.setCurrentIndex(0)
        self.view.tabWidget.setCurrentIndex(0)
        self.view.stop_btn.setDisabled(True)
        self.view.stop_btn_2.setDisabled(True)

    def start_state(self, mode):
        if mode == "anony":
            self.view.start_btn.setDisabled(True)
            self.view.stop_btn.setEnabled(True)
            self.view.tabWidget.setCurrentIndex(2)
            self.view.familiar.setDisabled(True)
            Thread(target=self.main.process_anony).start()
        else:
            self.view.start_btn_2.setDisabled(True)
            self.view.stop_btn_2.setEnabled(True)
            self.view.tabWidget_2.setCurrentIndex(1)
            self.view.anonymous.setDisabled(True)
            Thread(target=self.main.process_familiar).start()
        self.view.state = "started"

    def stop_state(self, mode):
        if mode == "anony":
            self.view.start_btn.setEnabled(True)
            self.view.stop_btn.setDisabled(True)
            self.view.familiar.setEnabled(True)
        else:
            self.view.start_btn_2.setEnabled(True)
            self.view.stop_btn_2.setDisabled(True)
            self.view.anonymous.setEnabled(True)
        self.view.state = "stopped"

