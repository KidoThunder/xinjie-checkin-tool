from apis import XinJieAPIS
from xj_logger import logger

logger.info('----------start----------')
xj_api = XinJieAPIS()
xj_api.login()
xj_api.checkin()
xj_api.logout()
logger.info("----------finish---------")
