import yaml


class TestDataLoader:

    @classmethod
    def load_test_case_data(cls, data_file):
        with open(data_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data
