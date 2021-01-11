import requests

from xj_logger import logger


class BaseRequest(object):
    def __init__(self, verify_ssl=False):
        self.session = requests.Session()
        self.session.verify = verify_ssl
        self.cookies = None

    def get(self, url):
        resp = self.session.get(url, cookies=self.cookies)
        if resp.status_code == 200:
            return resp, True
        return None, False

    def post(self, url, payload=None):
        resp = self.session.post(url, payload, cookies=self.cookies)
        if resp.status_code == 200:
            return resp, True
        return None, False

    def set_cookies(self, cookies):
        self.cookies = cookies


class XinJieAPIS(object):
    def __init__(self, config):
        self.api_config = config["xinjie"]["api"]
        self.base_url = self.api_config["base_url"]
        self.base_request = BaseRequest()

    def login(self):
        url = f"{self.base_url}auth/login"
        payload = {
            "email": self.api_config["email"],
            "passwd": self.api_config["password"]
        }
        resp, is_ok = self.base_request.post(url, payload)
        if not is_ok:
            logger.info("Login Failed!")
            return
        self.base_request.set_cookies(resp.cookies)
        logger.info(f"Login Result: {resp.json()['ret']}, Login message: {resp.json()['msg']}")

    def checkin(self):
        url = f"{self.base_url}user/checkin"
        resp, is_ok = self.base_request.post(url)
        if not is_ok:
            logger.info("Checkin Failed!")
            return False, "Checkin Failed!"
        logger.info(f"Checkin Result: {resp.json()['ret']}, Checkin message: {resp.json()['msg']}")
        return True, resp.json()['msg']

    def logout(self):
        url = f"{self.base_url}user/logout"
        resp, is_ok = self.base_request.get(url)
        if not is_ok:
            logger.info("Logout Failed!")
        logger.info("Logout Successfully!")


class ServerPushAPIs(BaseRequest):
    def __init__(self, config):
        self.api_config = config["serverchan"]["api"]
        self.base_url = self.api_config["base_url"]
        self.base_request = BaseRequest()
        super(ServerPushAPIs, self).__init__()

    def push_to_wechat(self, status, message):
        url = f"{self.base_url}{self.api_config['token']}{self.api_config['request_suffix']}"
        payload = {
            "text": "XJ checkin successfully!" if status else "XJ checkin failed!",
            "desp": message
        }
        import pdb; pdb.set_trace()
        resp = self.base_request.post(url, payload)
        print(resp)
