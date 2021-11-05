from feishu.api_test.api.base_api import BaseApi
from feishu.utils.logger import logger


class ChatGroupMessage(BaseApi):

    def get_message_content(self, message_id):
        logger.info("Getting message content...")
        path = f"/im/v1/messages/{message_id}"
        r = self.send_request("GET", f"{self.base_url}{path}")
        return r.json()

    def send_text_message(self, chat_id, content):
        logger.info("Sending message...")
        path = f"/im/v1/messages"
        params = {
            "receive_id_type": "chat_id"
        }
        data = {
            "receive_id": chat_id,
            "content": f"{{\"text\":\"{content}\"}}",
            "msg_type": "text"
        }
        r = self.send_request("POST", f"{self.base_url}{path}", params=params, json=data)
        return r.json()

    def recall_message(self, message_id):
        logger.info("Recalling message...")
        path = f"/im/v1/messages/{message_id}"
        r = self.send_request("DELETE", f"{self.base_url}{path}")
        return r.json()
