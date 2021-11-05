import pytest


class Runner:
    web_test_case_dir = "web_test/test_case"
    api_test_case_dir = "api_test/test_case"

    @classmethod
    def run_test(cls, test_case_path):
        pytest.main(["-sv", test_case_path])


if __name__ == '__main__':
    # Runner.run_test(Runner.web_test_case_dir)
    Runner.run_test(Runner.api_test_case_dir)
