import logging
import unittest
from hamcrest import *

from deasciiferlib.deasciifier import Deasciifier
from deasciiferlib.deasciifier import logger as deasciifier_logger

test_logger = logging.getLogger('Deasciifier')

class SimpleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        cls.deasciifier = Deasciifier()


    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        deasciifier_logger.setLevel(logging.INFO)
        test_logger.setLevel(logging.INFO)

    def test_should_deasciifySomeWords(self):
        deasciifier_logger.setLevel(logging.DEBUG)
        assert_that(self.deasciifier.deasciify(u'agac'), equal_to(u'a\u011fac'))
        deasciifier_logger.debug("\n\n\n------------------\n\n\n------------------\n\n\n------------------\n\n\n------------------\n\n\n")
        assert_that(self.deasciifier.deasciify(u'agaclandirma calismalari'), equal_to(u'a\u011fa\xe7land\u0131rma \xe7al\u0131\u015fmalari'))