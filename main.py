import sys
from pathlib import Path

import yaml

from apis import XinJieAPIS
from xj_logger import logger


def main(api_config):
    logger.info('----------start----------')
    xj_api = XinJieAPIS(api_config)
    xj_api.login()
    xj_api.checkin()
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
            }
        }
    else:
        with open(Path.cwd() / "config.yaml") as config_file:
            config = yaml.safe_load(config_file)

    main(config)
