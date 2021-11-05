import json
from selenium import webdriver
from feishu.utils.configurator import config
from feishu.web_test.page.base_page import BasePage
from feishu.web_test.page.chats.messenger_page import MessengerPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            driver_config = config["driver_config"]
            browser = driver_config["browser"]

            if browser == "Chrome":
                options = webdriver.ChromeOptions()
                if driver_config["using_headless"]:
                    options.add_argument("--headless")
                if driver_config["debugger"]["using_debugger"]:
                    options.debugger_address = driver_config["debugger"]["debugger_address"]
                self.driver = webdriver.Chrome(options=options)
            elif browser == "Firefox":
                self.driver = webdriver.Firefox()
                options = webdriver.FirefoxOptions()
                if driver_config["using_headless"]:
                    options.add_argument("--headless")
                self.driver = webdriver.Chrome(options=options)
            elif browser == "Edge":
                self.driver = webdriver.Edge()
            elif browser == "Safari":
                self.driver = webdriver.Safari()

            self.driver.maximize_window()
            self.driver.implicitly_wait(driver_config["default_implicit_waiting_time"])
        return self

    def stop(self):
        self.driver.quit()

    def open_page_with_user_cookies(self):
        # with open("data/cookie", "r") as f:
        #     cookie_text = f.read()
        # cookie_list = [kv.split("=", 1) for kv in cookie_text.split("; ")]
        # cookies = []
        # for cookie_item in cookie_list:
        #     cookie_dict = {
        #         "name": cookie_item[0],
        #         "value": cookie_item[1]
        #     }
        #     cookies.append(cookie_dict)

        with open("data/cookie", "r", encoding="utf-8") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def save_user_cookie(self):
        with open("data/cookie", "w", encoding="utf-8") as f:
            cookies = self.driver.get_cookies()
            json.dump(cookies, f)

    def go_to_messenger_page(self):
        self.driver.get(f"{config['app_url']}/messenger")
        # self.open_page_with_user_cookies()
        # self.save_user_cookie()
        return MessengerPage(self.driver)
