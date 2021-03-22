import os
import platform



version = "1.0.2"
copyright_text = "AhmeDSaeeD | (lordahmed on Fiverr)"
copyright_url = "https://fiverr.com/lordahmed"


# paths
if platform.system() == "Darwin":
    data_folder = f"{os.path.expanduser('~')}/Library/TelegramData"
    browserData = f"{data_folder}/browserData"
    accountsFolder = f"{data_folder}/Accounts"
else:
    data_folder = "Data"
    browserData = f"Data\\browserData"
    accountsFolder = f"Data\\Accounts"