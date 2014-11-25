# coding: utf-8
from hamcrest import *
import unittest


class WhenCreatingFacade(unittest.TestCase):
    def setUp(self):
        pass


    def _get_target_class(self):
        from system.facade import Facade

        return Facade

    def _get_target_instance(self):
        return self._get_target_class()()

    def test_that_should_be_packet_when_make_an_inquiry_into_reservation_records(self):
        primary_key = 1
        customer = 'knskw,knskw@nullnull.com,檸檬根井都武者返市愛宿町4-2-3 エレガンスウェストポーチ999号室,'
        plan = 'すこやかパック,4500,1,だんぼーる,みかん,'
        reservation = '14/11/14/Fri,15,14/11/15/Sat'
        expected = str(primary_key) + ',' + customer + plan + reservation
        actual = self._get_target_instance().inquiry(primary_key)
        assert_that(actual, is_(expected))

    def test_that_should_raise_type_error_when_given_non_number(self):
        assert_that(calling(self._get_target_instance().inquiry).with_args("11"), TypeError)


if __name__ == "__main__":
    unittest.main()