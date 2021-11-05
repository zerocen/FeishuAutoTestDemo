from feishu.api_test.api.base_api import BaseApi
from feishu.utils.logger import logger


class ChatGroup(BaseApi):

    def get_chat_group_info(self, chat_id):
        logger.info("Getting chat group information...")
        path = f"/im/v1/chats/{chat_id}"
        r = self.send_request("GET", f"{self.base_url}{path}")
        return r.json()

    def get_chat_group_list(self):
        return self.get_chat_group_info("")

    def create_chat_group(self, name, description):
        logger.info("Creating chat group...")
        path = "/im/v1/chats"
        data = {
            "name": name,
            "description": description
        }
        r = self.send_request("POST", f"{self.base_url}{path}", json=data)
        return r.json()

    def update_chat_group_info(self, chat_id, name, description):
        logger.info("Updating chat group information...")
        path = f"/im/v1/chats/{chat_id}"
        data = {
            "name": name,
            "description": description
        }
        r = self.send_request("PUT", f"{self.base_url}{path}", json=data)
        return r.json()

    def dissolve_chat_group(self, chat_id):
        logger.info("Dissolving chat group...")
        path = f"/im/v1/chats/{chat_id}"
        r = self.send_request("DELETE", f"{self.base_url}{path}")
        return r.json()
