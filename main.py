import sys
from pathlib import Path

import yaml

from apis import XinJieAPIS, ServerPushAPIs
from xj_logger import logger


def main(api_config):
    logger.info('----------start----------')
    xj_api = XinJieAPIS(api_config)
    xj_api.login()
    is_success, msg = xj_api.checkin()
    server_push_api = ServerPushAPIs(api_config)
    server_push_api.push_to_wechat(is_success, msg)
    xj_api.logout()
    logger.info("----------finish---------")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        config = {
            "xinjie": {
                "api": {
                    'base_url': sys.argv[1],
                    'email': sys.argv[2],
                    'password': sys.argv[3],
                }
            },
            "serverchan": {
                "api": {
                    'base_url': sys.argv[4],
                    'token': sys.argv[5],
                    'request_suffix': sys.argv[6],
                }
            }
        }
    else:
        with open(Path.cwd() / "config.yaml") as config_file:
            config = yaml.safe_load(config_file)

    main(config)
