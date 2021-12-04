import logging
from bot.settings import LOG_FILE


class ColorLoggerFilter(logging.Filter):
    COLOR = {
        "DEBUG": "GREEN",
        "INFO": "GREEN",
        "WARNING": "YELLOW",
        "ERROR": "RED",
        "CRITICAL": "RED",
    }

    def filter(self, record):
        record.color = ColorLoggerFilter.COLOR[record.levelname]
        return True


file_log = logging.FileHandler(LOG_FILE)
console_out = logging.StreamHandler()

logging.basicConfig(
    handlers=(file_log, console_out),
    format=u'"%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"',
    level=logging.INFO,
)


logger = logging.getLogger(__name__)
logger.addFilter(ColorLoggerFilter())
