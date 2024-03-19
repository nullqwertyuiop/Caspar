import logging
import os
import unittest

from caspar.data_source.tushare_pro.api import TushareProAPI
from tests.util import init_env


class TushareProTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        init_env()
        self.api = TushareProAPI(os.environ["TUSHARE_TOKEN"])

    def test_api(self):
        logging.info(self.api.stock_basic())


if __name__ == "__main__":
    unittest.main()
