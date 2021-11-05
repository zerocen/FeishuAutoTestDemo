import json
import pytest


class TestChatGroupMessage:

    @pytest.mark.parametrize("chat_id, message_content", [
        ("oc_c93ef2e680ae4417d22271911a15e24c", "A test message")
    ])
    def test_get_message_content(self, chat_group_message, chat_id, message_content):
        message_id = chat_group_message.send_text_message(chat_id, message_content)["data"]["message_id"]
        r = chat_group_message.get_message_content(message_id)
        json_content = r["data"]["items"][0]["body"]["content"]
        text_content = json.loads(json_content)["text"]
        assert text_content == message_content

    @pytest.mark.parametrize("chat_id, message_content", [
        ("oc_c93ef2e680ae4417d22271911a15e24c", "A test message")
    ])
    def test_send_text_message(self, chat_group_message, chat_id, message_content):
        r = chat_group_message.send_text_message(chat_id, message_content)
        assert r["code"] == 0

        message_id = r["data"]["message_id"]
        r = chat_group_message.get_message_content(message_id)
        json_content = r["data"]["items"][0]["body"]["content"]
        text_content = json.loads(json_content)["text"]
        is_deleted = r["data"]["items"][0]["deleted"]
        assert text_content == message_content and not is_deleted

    @pytest.mark.parametrize("chat_id, message_content", [
        ("oc_c93ef2e680ae4417d22271911a15e24c", "A test message")
    ])
    def test_recall_message(self, chat_group_message, chat_id, message_content):
        message_id = chat_group_message.send_text_message(chat_id, message_content)["data"]["message_id"]
        r = chat_group_message.recall_message(message_id)
        assert r["code"] == 0

        r = chat_group_message.get_message_content(message_id)
        is_deleted = r["data"]["items"][0]["deleted"]
        assert is_deleted
