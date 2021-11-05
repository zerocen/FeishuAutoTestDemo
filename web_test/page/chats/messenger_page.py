from feishu.utils.configurator import config
from feishu.utils.logger import logger
from feishu.web_test.page.base_page import BasePage


class MessengerPage(BasePage):

    page_function_file = f"{config['data_dir']['page_function']}/messenger_page.yml"

    def create_chat_group(self, group_name):
        params = {
            "group_name": group_name,
        }
        logger.info(f"Create chat group. Params: {params}")
        self.perform_function(self.page_function_file, "create_chat_group", params=params)
        return self

    def get_current_chat_title_name(self):
        params = {
            "chat_title_storage_key": "chat_title",
        }
        logger.info(f"Get current chat title name.")
        info = self.perform_function(self.page_function_file, "get_current_chat_title_name", params=params)
        logger.info(f"Current chat title name: {info}")
        return info[params["chat_title_storage_key"]]
