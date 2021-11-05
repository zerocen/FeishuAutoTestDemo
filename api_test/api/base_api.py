import requests
from feishu.utils.logger import logger


class BaseApi:

    def __init__(self):
        self.base_url = "https://open.feishu.cn/open-apis"
        self.proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }
        self.session = requests.Session()

        self.access_token = self.get_access_token()
        self.session.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json; charset=utf-8"
        }

    def get_access_token(self):
        path = "/auth/v3/app_access_token/internal/"
        params = {
            "app_id": "cli_a060281d35b8d00d",
            "app_secret": "pEu7r7iaKhHefFuAkczGDh6ksO7xdGIp"
        }
        r = self.send_request("POST", f"{self.base_url}{path}", params=params)
        return r.json()["app_access_token"]

    def send_request(self, *args, **kwargs):
        logger.debug(f"Send HTTP Request: {args}, {kwargs}")
        response = self.session.request(*args, **kwargs)
        logger.debug(f"Response: {response.text}")
        return response
