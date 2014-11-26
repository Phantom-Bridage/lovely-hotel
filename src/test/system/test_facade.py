# coding: utf-8
from hamcrest import *
import unittest


class WhenCreatingFacade(unittest.TestCase):
    def setUp(self):
        self.primary_key = 1
        customer = u'高坂 穂乃果,honoka@lovelive,音ノ木坂学院,'
        plan = u'プラン1,5000,2,シングル,なし,'
        reservation = u'14/11/23,15:00,14/11/24'
        self.expected = str(self.primary_key) + ',' + customer + plan + reservation


    def _get_target_class(self):
        from system.facade import Facade

        return Facade

    def _get_target_instance(self):
        return self._get_target_class()()

    # check 予約番号をもとに、予約情報のパケットを返す
    def test_that_should_be_packet_when_make_an_inquiry_into_reservation_records(self):
        actual = self._get_target_instance().inquiry(1)
        assert_that(actual, is_(self.expected))

    # check 予約番号がint型でない時に型エラーを投げる
    def test_that_should_raise_type_error_when_non_integer_number(self):
        assert_that(calling(self._get_target_instance().inquiry).with_args("1"), TypeError)


if __name__ == "__main__":
    unittest.main()