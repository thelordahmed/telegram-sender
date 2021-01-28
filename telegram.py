import os
import random
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from controller import browserData, accountsFolder
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# search with username
# https://web.telegram.org/#/im?p=@USERNAME


class Telegram:
    _handle = None
    _window = None
    search_input = '//div[@class="im_dialogs_panel"]/div[@class="im_dialogs_search"]/input'
    # x_button = '//div[@class="im_dialogs_panel"]/div[@class="im_dialogs_search"]/a'
    # first_result = '//div[@class="im_dialogs_col" and @my-dialogs-list]//ul/li[1]'
    # CLICK DORPDOWN FIRST
    dropdown_btn = '//div[@dropdown and @style]/a[@dropdown-toggle]'
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
    # this will be visible if this is channel (unable to send)
    channel_div = '//div[@ng-switch-when="channel"]'

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
            cls._window.implicitly_wait(2)
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
        cls._window.close()

    @classmethod
    def search_phone(cls, number: str) -> None or False:
        """
        opens the contact chat - returns False if contact not foound
        """
        # CLICKING THE DROPDOWN BUTTON
        try:
            cls._window.find_element_by_xpath(cls.dropdown_btn).click()
        except NoSuchElementException:
            cls._window.refresh()
            cls.search_phone(number)
        # ADDING NEW CONTACT
        cls._window.find_element_by_xpath(cls.contacts_btn).click()
        cls._window.find_element_by_xpath(cls.add_new_contact).click()
        cls._window.find_element_by_xpath(cls.phone_input).send_keys(number)
        cls._window.find_element_by_xpath(cls.saveContact_btn).click()
        # WAITING FOR ADDING MODAL TO DISAPPEAR
        WebDriverWait(cls._window, 20).until(ec.invisibility_of_element_located((By.XPATH, cls.saveContact_btn)))
        # CHECKING FOR ERROR MESSAGE
        try:
            cls._window.find_element_by_xpath(cls.error_modal)
            return False
        except NoSuchElementException:
            pass


    @classmethod
    def search_username(cls, username: str) -> None or False or str:
        """
        opens the contact chat - returns False if contact not foound - or "channel" if it's a channel
        """
        # TRY OPENING THE USERNAME
        cls._window.get(f"https://web.telegram.org/#/im?p=@{username}")
        sleep(5)
        # CHECK ON CONNECTION
        if cls.network_still_connected() is False:
            WebDriverWait(cls._window, 3600).until(ec.invisibility_of_element_located((By.XPATH, cls.connectionLost_div)))
            cls._window.get(f"https://web.telegram.org/#/im?p=@{username}")
        # CHECK ON NOT FOUND ERROR MESSAGE
        try:
            cls._window.find_element_by_xpath(cls.error_modal)
        except NoSuchElementException:
            return False
        # CHECK IF IT'S CHANNEL
        try:
            cls._window.find_element_by_xpath(cls.channel_div)
        except NoSuchElementException:
            return "channel"


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
        sleep(1)
        message_input.send_keys(Keys.ENTER)


    @classmethod
    def sending_attachment(cls, paths: list):
        # (ALGORITHM) PASSING MULTIPLE FILES TO INPUT ELEMENT
        multiple_paths = paths[0]
        if len(paths) > 1:
            for path in paths[1:]:
                multiple_paths += "\n" + path
        sleep(1)
        cls._window.find_element_by_xpath(cls.attachment_input).send_keys(multiple_paths)
        sleep(random.randint(1, 2))


    # @classmethod
    # def sending_document(cls, paths):
    #     multiple_paths = paths[0]
    #     if len(paths) > 1:
    #         for path in paths[1:]:
    #             multiple_paths += "\n" + path
    #     sleep(1)
    #     cls._window.find_element_by_xpath(cls.document_input).send_keys(multiple_paths)
    #     sleep(random.randint(1, 2))


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
