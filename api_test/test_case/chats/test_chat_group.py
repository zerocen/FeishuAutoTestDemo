import pytest


class TestChatGroup:

    @pytest.mark.parametrize("chat_group_name, chat_group_description", [
        ("Test Chat Group", "This is a test chat group")
    ])
    def test_get_chat_group_info(self, chat_group, chat_group_name, chat_group_description):
        # create a chat group before get the information
        chat_id = chat_group.create_chat_group(chat_group_name, chat_group_description)["data"]["chat_id"]

        r = chat_group.get_chat_group_info(chat_id)
        assert r["data"]["name"] == chat_group_name

    @pytest.mark.parametrize("chat_group_name, chat_group_description", [
        ("Test Chat Group", "This is a test chat group")
    ])
    def test_create_chat_group(self, chat_group, chat_group_name, chat_group_description):
        r = chat_group.create_chat_group(chat_group_name, chat_group_description)
        chat_id = r["data"]["chat_id"]
        assert r["data"]["name"] == chat_group_name

        r = chat_group.get_chat_group_info(chat_id)
        assert r["data"]["name"] == chat_group_name

    @pytest.mark.parametrize("old_name, old_description, new_name, new_description", [
        ("Test Chat Group", "This is a test chat group", "Updated name", "Updated Description")
    ])
    def test_update_chat_group_info(self,  chat_group, old_name, old_description, new_name, new_description):
        chat_id = chat_group.create_chat_group(old_name, old_description)["data"]["chat_id"]
        r = chat_group.update_chat_group_info(chat_id, new_name, new_description)
        assert r["code"] == 0

        r = chat_group.get_chat_group_info(chat_id)
        assert r["code"] == 0 and r["data"]["name"] == new_name
        assert r["code"] == 0 and r["data"]["description"] == new_description

    @pytest.mark.parametrize("chat_group_name, chat_group_description", [
        ("Test Chat Group", "This is a test chat group")
    ])
    def test_dissolve_chat_group(self, chat_group, chat_group_name, chat_group_description):
        chat_id = chat_group.create_chat_group(chat_group_name, chat_group_description)["data"]["chat_id"]
        r = chat_group.dissolve_chat_group(chat_id)
        assert r["code"] == 0

        r = chat_group.dissolve_chat_group(chat_id)
        assert r["code"] == 232009
