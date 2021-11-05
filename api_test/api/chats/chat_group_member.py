from feishu.api_test.api.base_api import BaseApi
from feishu.utils.logger import logger


class ChatGroupMember(BaseApi):

    def get_members(self, chat_id):
        logger.info("Getting chat group member information...")
        path = f"/im/v1/chats/{chat_id}/members"
        params = {
            "member_id_type": "user_id"
        }
        r = self.send_request("GET", f"{self.base_url}{path}", params=params)
        return r.json()

    def add_members(self, chat_id, user_ids):
        logger.info("Adding chat group member...")
        path = f"/im/v1/chats/{chat_id}/members"
        params = {
            "member_id_type": "user_id"
        }
        data = {
            "id_list": user_ids
        }
        r = self.send_request("POST", f"{self.base_url}{path}", params=params, json=data)
        return r.json()

    def remove_members(self, chat_id, user_ids):
        logger.info("Removing chat group member...")
        path = f"/im/v1/chats/{chat_id}/members"
        params = {
            "member_id_type": "user_id"
        }
        data = {
            "id_list": user_ids
        }
        r = self.send_request("DELETE", f"{self.base_url}{path}", params=params, json=data)
        return r.json()
