import pytest


class TestChatGroupMember:

    @pytest.mark.parametrize("chat_id", [
        "oc_c93ef2e680ae4417d22271911a15e24c"
    ])
    def test_get_chat_group_members(self, chat_group_member, chat_id):
        r = chat_group_member.get_members(chat_id)
        assert r["code"] == 0

    @pytest.mark.parametrize("chat_id, user_ids", [
        ("oc_c93ef2e680ae4417d22271911a15e24c", ["d2e929g7"])
    ])
    def test_add_chat_group_members(self, chat_group_member, chat_id, user_ids):
        chat_group_member.remove_members(chat_id, user_ids)
        r = chat_group_member.add_members(chat_id, user_ids)
        assert r["code"] == 0

        r = chat_group_member.get_members(chat_id)
        members = list(filter(lambda x: x["member_id"] in user_ids, r["data"]["items"]))
        assert len(members) == len(user_ids)

    @pytest.mark.parametrize("chat_id, user_ids", [
        ("oc_c93ef2e680ae4417d22271911a15e24c", ["d2e929g7"])
    ])
    def test_remove_chat_group_members(self, chat_group_member, chat_id, user_ids):
        r = chat_group_member.add_members(chat_id, user_ids)
        assert r["code"] == 0

        r = chat_group_member.remove_members(chat_id, user_ids)
        assert r["code"] == 0

        r = chat_group_member.get_members(chat_id)
        members = list(filter(lambda x: x["member_id"] in user_ids, r["data"]["items"]))
        assert len(members) == 0
