import re
import allure
import yaml
from selenium.webdriver.remote.webdriver import WebDriver
from feishu.utils.logger import logger


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find(locator).click()

    def input_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def perform_function(self, function_file, function_name, params=None):
        if params is None:
            params = {}

        response = {}
        logger.debug(f"Perform function: {function_name}")
        with open(function_file, "r", encoding="utf-8") as f:
            functions = yaml.safe_load(f)
        steps = functions[function_name]

        for step in steps:
            logger.debug(f"Execute command [{step['command']}], details: {step}")

            # Replace the placeholder in yml with the params value
            pattern = re.compile(r"{(.+?)}")
            for key in ["element", "text", "storage_key"]:
                if key in step:
                    tmp_str = str(step[key])
                    matches = pattern.findall(tmp_str)
                    for match in matches:
                        tmp_str = tmp_str.replace(f"{{{match}}}", params[match])
                    else:
                        step[key] = tmp_str

            # Parse element locator
            locator = None
            if "element" in step:
                locator = step["element"].split("=", 1)
            if locator:
                locator[0] = locator[0].replace("_", " ")

            with allure.step(step["step_name"]):
                if step["command"] == "input_text":
                    self.input_text(locator, step["text"])
                elif step["command"] == "click_element":
                    self.click_element(locator)
                elif step["command"] == "get_text":
                    response[step["storage_key"]] = self.get_text(locator)

        return response
