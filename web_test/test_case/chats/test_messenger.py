import allure
import pytest
from feishu.utils.configurator import config
from feishu.utils.test_data_loader import TestDataLoader


@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("Messenger")
class TestMessenger:

    test_case_data_file = f"{config['data_dir']['test_case']}/messenger.yml"
    user_name = 'Fresh'

    @allure.story("Create Chat Group")
    @allure.title("Create Chat Group")
    @pytest.mark.parametrize("group_name", TestDataLoader.load_test_case_data(test_case_data_file)["create_chat_group"])
    def test_create_chat_group(self, app, group_name):
        with allure.step("Go to messenger page"):
            messenger_page = app.go_to_messenger_page()

        with allure.step("Create a chat group"):
            messenger_page.create_chat_group(group_name)

        new_group_name = messenger_page.get_current_chat_title_name()
        if not group_name.strip():
            group_name = self.user_name

        assert new_group_name == group_name
