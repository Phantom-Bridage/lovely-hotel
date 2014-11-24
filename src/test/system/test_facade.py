# coding: utf-8
from hamcrest import *
import unittest


class WhenCreatingFacade(unittest.TestCase):
    def setUp(self):
        primary_key = 1
        customer = 'knskw,knskw@nullnull.com,檸檬根井都武者返市愛宿町4-2-3 エレガンスウェストハイツ999号室,'
        plan = 'ビジネス,9999,1,ダンボール,みかん,'
        reservation = '14/11/14/Fri,15,14/11/15/Sat'
        self.expected = str(primary_key) + ',' + customer + plan + reservation
        self.actual = self._get_target_instance().inquiry(primary_key)

    def _get_target_class(self):
        from system.facade import Facade

        return Facade

    def _get_target_instance(self):
        return self._get_target_class()()

    def test_that_should_be_packet_when_make_an_inquiry_into_reservation_records(self):
        assert_that(self.actual, is_(self.expected))


if __name__ == "__main__":
    unittest.main()