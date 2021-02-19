import os
import random
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, Channel, Chat
import controller
from controller import browserData, accountsFolder
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from telethon.sync import TelegramClient
import asyncio
from telethon.errors.rpcerrorlist import PhoneCodeInvalidError

# search with username
# https://web.telegram.org/#/im?p=@USERNAME


class Telegram:
    client = None
    groups = None
    _handle = None
    _window = None
    search_input = '//div[@class="im_dialogs_panel"]/div[@class="im_dialogs_search"]/input'
    # x_button = '//div[@class="im_dialogs_panel"]/div[@class="im_dialogs_search"]/a'
    # first_result = '//div[@class="im_dialogs_col" and @my-dialogs-list]//ul/li[1]'
    # CLICK DORPDOWN FIRST
    dropdown_btn = '//div[@class="icon-hamburger-wrap"]'
    # THEN CLICK CONTACTS
    contacts_btn = '//a[@ng-click="openContacts()"]'
    # THEN CLICK ADD NEW CONTACT
    add_new_contact = '//button[@ng-click="importContact()"]'
    phone_input = '//input[@name="phone"]'
    saveContact_btn = '//button[@ng-click="doImport()"]'
    message_input = '//div[@class="composer_rich_textarea"]'
    attachment_input = '//input[@class="im_media_attach_input"]'
    # document_input = '//input[@class="im_attach_input"]'
    # if this div appeared.. means the connection is lost
    connectionLost_div = '//div[@class="tg_head_connecting_wrap" and @ng-switch="offlineConnecting"]'
    # this will show if username not found
    error_modal = '//div[@class="error_modal_wrap md_simple_modal_wrap"]'
    error_modal_okBtn = '//div[@class="error_modal_wrap md_simple_modal_wrap"]//button'
    # this will be visible if this is channel (unable to send)
    channel_div = '//div[@ng-switch-when="channel"]'
    modal_close_btn = '//a[@class="md_modal_action md_modal_action_close"]'
    # GROUP SECTION

    phone_div = '//div[@ng-if="user.phone"]/div[1]'
    username_div = '//div[@ng-if="user.username"]/div[1]'

    @classmethod
    def open(cls, account = browserData) -> object:
        """
        opens telegram on the browser and returns the window object
        """
        if account != browserData:
            account = os.path.join(accountsFolder, account)
        args = ["hide_console", ]
        chrome_options = Options()
        chrome_options.add_argument(r'--user-data-dir=' + account)
        if cls._handle is None:
            cls._window = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, service_args=args )
            cls._window.get("https://web.telegram.org")
            cls._handle = cls._window.current_window_handle
            # waiting for the telegram to login
            WebDriverWait(cls._window, 1000).until(ec.presence_of_element_located((
                By.XPATH, cls.search_input)))
            return cls._window
        else:
            # if browser was opened before >> switch focus to it
            cls._window.switch_to.window(cls._handle)
            return cls._window

    @classmethod
    def close(cls):
        cls._handle = None
        cls._window.close()

    @staticmethod
    def validate_phone(number):
        symbols = [" ", "-", "+", "/", "\\", "(", ")", "[", "]"]
        for i in symbols:
            number = number.replace(i, "")
        return number

    @classmethod
    def search_phone(cls, number: str) -> None or False:
        """
        opens the contact chat - returns False if contact not foound
        """
        # VALIDATING THE NUMBER
        number = cls.validate_phone(number)
        # CHECKING ON ANY OPENED MODAL BEFORE STARTING
        try:
            cls._window.find_element_by_xpath(cls.modal_close_btn).click()
        except NoSuchElementException:
            pass
        # CLICKING THE DROPDOWN BUTTON
        try:
            cls._window.find_element_by_xpath(cls.dropdown_btn).click()
        except NoSuchElementException:
            cls._window.refresh()
            cls.search_phone(number)
        # ADDING NEW CONTACT
        try:
            sleep(1)
            cls._window.find_element_by_xpath(cls.contacts_btn).click()
        except ElementNotInteractableException:
            sleep(1)
            cls._window.find_element_by_xpath(cls.contacts_btn).click()
        sleep(1)
        cls._window.find_element_by_xpath(cls.add_new_contact).click()
        sleep(1)
        cls._window.find_element_by_xpath(cls.phone_input).send_keys(number)
        cls._window.find_element_by_xpath(cls.saveContact_btn).click()
        # WAITING FOR ADDING MODAL TO DISAPPEAR
        WebDriverWait(cls._window, 20).until(ec.invisibility_of_element_located((By.XPATH, cls.saveContact_btn)))
        # CHECKING FOR ERROR MESSAGE
        try:
            cls._window.find_element_by_xpath(cls.error_modal)
            sleep(1)
            cls._window.find_element_by_xpath(cls.error_modal_okBtn).click()
            return False
        except NoSuchElementException:
            pass


    @classmethod
    def search_username(cls, username: str) -> None or False or str:
        """
        opens the contact chat - returns False if contact not foound - or "channel" if it's a channel
        """
        username = username.replace("@", "")
        # TRY OPENING THE USERNAME
        print("debug")
        cls._window.get(f"https://web.telegram.org/#/im?p=@{username}")
        sleep(random.randint(1, 3))
        # CHECK ON CONNECTION
        if cls.network_still_connected() is False:
            WebDriverWait(cls._window, 3600).until(ec.invisibility_of_element_located((By.XPATH, cls.connectionLost_div)))
            cls._window.get(f"https://web.telegram.org/#/im?p=@{username}")
        # CHECK ON NOT FOUND ERROR MESSAGE
        try:
            WebDriverWait(cls._window, 2).until(ec.presence_of_element_located((By.XPATH, cls.error_modal_okBtn))).click()
            return False
        except TimeoutException:
            pass
        # CHECK IF IT'S CHANNEL
        try:
            cls._window.find_element_by_xpath(cls.channel_div)
            return "channel"
        except NoSuchElementException:
            pass

    @classmethod
    def sending_text(cls, message: str) -> None:
        message_lines = message.split("\n")
        message_input = cls._window.find_element_by_xpath(cls.message_input)
        actions = ActionChains(cls._window)
        actions.move_to_element(message_input)
        actions.click()
        for line in message_lines:
            actions.send_keys(line)
            actions.key_down(Keys.SHIFT)
            actions.key_down(Keys.ENTER)
            actions.key_up(Keys.SHIFT)
            actions.key_up(Keys.ENTER)
        actions.perform()
        sleep(random.randint(1, 3))
        message_input.send_keys(Keys.ENTER)



    @classmethod
    def sending_attachment(cls, paths: list):
        # (ALGORITHM) PASSING MULTIPLE FILES TO INPUT ELEMENT
        if len(paths) != 0:
            multiple_paths = paths[0]
        else:
            return False
        if len(paths) > 1:
            for path in paths[1:]:
                multiple_paths += "\n" + path
        sleep(1)
        cls._window.find_element_by_xpath(cls.attachment_input).send_keys(multiple_paths)
        sleep(random.randint(1, 2))


    @classmethod
    def network_still_connected(cls) -> True or False:
        """
        returns True if still connected - and False if connection is lost
        """
        try:
            cls._window.find_element_by_xpath(cls.connectionLost_div)
            return False
        except NoSuchElementException:
            return True


    @classmethod
    def wait_for_connection(cls):
        WebDriverWait(cls._window, 3600).until(ec.invisibility_of_element_located((By.XPATH, cls.connectionLost_div)))


    @classmethod
    def api_client_connect(cls, phone, api_id, api_hash):
        if "+" not in phone:
            phone = "+" + phone
        session_path = os.path.join(f"{controller.data_folder}", phone)
        cls.client = TelegramClient(session_path, api_id, api_hash)
        cls.client.connect()
        if not cls.client.is_user_authorized():
            print("not authorized")
            cls.client.send_code_request(phone)
            return False
        print("Authorized!")

    @classmethod
    def api_confirm_signin(cls, phone, code):
        """
        returns "invalid code" if confirmation code was wrong and false if something wrong happened
        """
        if "+" not in phone:
            phone = "+" + phone
        try:
            cls.client.sign_in(phone, code)
        except PhoneCodeInvalidError:
            return "invalid code"
        except:
            return False

    @classmethod
    def api_extract_groups(cls):
        chats = []
        groups = []
        last_date = None
        chunk_size = 200

        result = cls.client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))

        # print(result.stringify())

        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.__class__ == Channel or chat.__class__ == Chat:
                    if chat.__class__ == Chat:
                        if chat.deactivated is False and chat.left is False:
                            groups.append(chat)
                    else:
                        groups.append(chat)

            except:
                continue

        # for chat in chats:
        #     try:
        #         if chat.megagroup:
        #             groups.append(chat)
        #     except:
        #         continue
        cls.groups = groups


