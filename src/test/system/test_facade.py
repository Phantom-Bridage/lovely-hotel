# coding: utf-8
import unittest
from hamcrest import *

class WhenCreatingHotelSystem(unittest.TestCase):
    def setUp(self):
        self.expected = '1,knskw,knskw@nullnull.com,檸檬根井都武者返市愛宿町4-2-3 エレガンスウェストハイツ999号室,ビジネス,9999,1,ダンボール,みかん,14/11/14/Fri,15,14/11/15/Sat'
        self.actual = self._get_target_instance().packet(1)

    def _get_target_class(self):
        from system.facade import Facade

        return Facade

    def _get_target_instance(self):
        return self._get_target_class()()

    def test_that_should_packet(self):
        assert_that(self.actual,is_(self.expected))
        #self.assertMultiLineEqual(self.actual, self.expected)


if __name__ == "__main__":
    unittest.main()