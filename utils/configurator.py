import yaml


class Configurator:

    def __init__(self):
        with open("data/config.yml", "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)


config = Configurator().config
