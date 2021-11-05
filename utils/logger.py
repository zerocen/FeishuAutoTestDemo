import logging
import logging.handlers
import os
from feishu.utils.configurator import config


class Logger:
    logger = logging.getLogger("MY_LOG")

    def __init__(self):
        self.logger.setLevel(logging.DEBUG)

        log_formatter = logging.Formatter("[%(asctime)s]  %(levelname)s  %(filename)s:%(lineno)d:%(funcName)s  -  "
                                          "%(message)s")

        if not os.path.exists(config["data_dir"]["log_dir"]):
            os.makedirs(config["data_dir"]["log_dir"])

        file_handler = logging.handlers.RotatingFileHandler(
            f"{config['data_dir']['log_dir']}/test_log.log", mode="a", backupCount=10, encoding="utf-8")
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        console_handler.setLevel(logging.INFO)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)


logger = Logger().logger
