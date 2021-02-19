import os
import webbrowser
from json.decoder import JSONDecodeError
from controller import version
import requests
from requests.exceptions import ConnectionError
from getmac import get_mac_address as gma
from view import View


class License:
    def __init__(self, api_url: str, download_url: str, view_object: View
                 , app: str, data_folder: str, mainWindow_frame: View, app_name: str):
        self.api_url = api_url
        self.view = view_object
        self.app = app
        self.data_folder = data_folder
        self.mainWindow_frame = mainWindow_frame
        self.download_page = download_url
        self.app_name = app_name
        self.license_frame = self.view.license_frame
        self.license_input = self.view.license_le
        self.license_button = self.view.license_btn
        self.status_label = self.view.license_status_label
        self.default_state()
        try:
            with open(f"{data_folder}/license_key.txt", "r") as f:
                key = f.read()
            self.validate(key)
        except FileNotFoundError:
            pass



        self.license_button.clicked.connect(lambda: self.validate(None))


    def default_state(self):
        self.mainWindow_frame.hide()
        self.license_frame.show()
        self.view.adjustSize()

    def show(self):
        # hide license frame
        self.view.license_frame.hide()
        # show hidden interface
        self.mainWindow_frame.show()

    def validate(self, key=None):
        # if key is None, that means this method was called on app start with pre-saved key
        if key is None:
            key = self.license_input.text().strip()
        try:
            if key != "":
                self.view.license_btn.setDisabled(True)
                mac = gma()
                try:
                    res = requests.put(f"{self.api_url}/key/{key}/{mac}/{self.app}").json()
                except JSONDecodeError:
                    self.view.license_status_label.setText(
                        "Invalid key. \nplease visit link below to order a valid key\n\nhttps://www.fiverr.com/share/5ADL24 ")
                    self.view.license_btn.setEnabled(True)
                    return False
                self.license_input.setText(key)
                if res["response"] == "expired":
                    self.view.license_status_label.setText("Sorry, this license has expired. \nplease visit link below to renew your key\n\nhttps://www.fiverr.com/share/5ADL24")
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "invalid":
                    self.view.license_status_label.setText("Invalid key. \nplease visit link below to order a valid key\n\nhttps://www.fiverr.com/share/5ADL24 ")
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "different device":
                    self.view.license_status_label.setText("Sorry, this key is registed to another device. \nplease contact the seller.")
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "valid":
                    with open(os.path.join(self.data_folder, "license_key.txt"), "w") as f:
                        f.write(key)


                    # # increasing online counter
                    # if res["user"] != "admin" and res["user"] != "admin_PC":
                    #     requests.put(f"{self.api_url}/connected/increase")
                    self.view.setWindowTitle(f"{self.app_name} {version} ---- Expire Date: {res['date']}")
                    self.show()
                    self.view.adjustSize()
                    if version != res["version"]:
                        confim = self.view.confirmMessage("New Update Available!", "New Update is availabe for the software!\nDo you want to download it?")
                        if confim is True:
                            webbrowser.open(self.download_page)

                # FIXING A BUG ON MAC WHEN SHOWING - LABEL DOESN'T SHOW UP WHEN CHANGING BEFORE CLICKING ON IT
                self.view.license_status_label.hide()
                self.view.license_status_label.show()
        except ConnectionError:
            self.view.license_status_label.setText("Connection Error!")
            self.view.license_btn.setEnabled(True)
            # FIXING A BUG ON MAC WHEN SHOWING - LABEL DOESN'T SHOW UP WHEN CHANGING BEFORE CLICKING ON IT
            self.view.license_status_label.hide()
            self.view.license_status_label.show()






