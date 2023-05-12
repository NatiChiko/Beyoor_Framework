import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        logger_name = inspect.stack()[0][3]
        log = logging.getLogger(logger_name)
        filehandler = logging.FileHandler("logs.log")
        log.addHandler(filehandler)
        set_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(set_format)
        log.setLevel(logging.INFO)
        # log.debug("Debug statement")
        # log.info("Info statement")
        # log.warning("Warning statement")
        # log.error("Error statement")
        # log.critical("Critical statement")
        return log


