# -*- coding:utf-8 -*-
import unittest
from dummy_foreign_exchanger import DummyExchanger


class TestDummyExchanger(unittest.TestCase):
    def test_exchange_yen_to_dollar_with_twice(self):
        exchanger = DummyExchanger()
        self.assertEqual(4, exchanger.exchange("yen", "dollar", 2))

    def test_exchange_dollar_to_yen_with_half(self):
        exchanger = DummyExchanger()
        self.assertEqual(1, exchanger.exchange("dollar", "yen", 2))

    def test_do_not_exchange_when_origin_is_result(self):
        exchanger = DummyExchanger()
        self.assertEqual(2, exchanger.exchange("yen", "yen", 2))
        self.assertEqual(2, exchanger.exchange("dollar", "dollar", 2))