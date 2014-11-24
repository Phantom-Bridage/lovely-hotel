# -*- coding:utf-8 -*-
import unittest
from money import Money
from dummy_foreign_exchanger import DummyExchanger


class TestMoney(unittest.TestCase):
    def test_money_is_yen(self):
        money = Money.yen(0)
        self.assertEqual("yen", money.nationality)

    def test_money_is_dollar(self):
        money = Money.dollar(0)
        self.assertEqual("dollar", money.nationality)

    def test_failed_to_initialize_when_given_except_real_number(self):
        self.check_unexpected_type_as_number(Money.yen)
        self.check_unexpected_type_as_number(Money.dollar)

    def test_money_exchange_yen_to_dollar(self):
        money = Money.yen(10)
        money.set_exchanger(DummyExchanger())

        expected = Money.dollar(20)
        result_money = money.exchange("dollar")

        self.assertTrue(expected == result_money)

    def test_money_recognize_equivalent_money_is_equal(self):
        money_yen1 = Money.yen(10)
        money_yen2 = Money.yen(10)
        self.assertTrue(money_yen1 == money_yen2)

    def test_money_recognize_non_equivalent_money_is_not_equal(self):
        money_yen1 = Money.yen(10)
        money_yen2 = Money.yen(20)
        money_dollar = Money.dollar(10)
        self.assertFalse(money_yen1 == money_yen2)
        self.assertFalse(money_yen1 == money_dollar)

    def test_return_the_sum_of_two_same_nationality_money(self):
        money_yen1 = Money.yen(10)
        money_yen2 = Money.yen(5)

        expected = Money.yen(15)
        money_sum = money_yen1 + money_yen2
        self.assertTrue(expected == money_sum)

    def test_return_the_sum_of_two_different_nationality_money(self):
        money_yen = Money.yen(10)
        money_yen.set_exchanger(DummyExchanger())
        money_dollar = Money.dollar(5)

        expected = Money.yen(12.5)
        money_sum = money_yen + money_dollar
        self.assertTrue(expected == money_sum)

    def test_return_error_which_add_money_and_other_class(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__add__)

    def test_return_the_difference_between_the_two_same_nationality_money(self):
        money_yen1 = Money.yen(20)
        money_yen2 = Money.yen(5)

        expected = Money.yen(15)
        money_diff = money_yen1 - money_yen2
        self.assertTrue(expected == money_diff)

    def test_return_the_difference_between_the_different_nationality_money(self):
        money_yen = Money.yen(10)
        money_yen.set_exchanger(DummyExchanger())
        money_dollar = Money.dollar(2)

        expected = Money.yen(9)
        money_diff = money_yen - money_dollar
        self.assertTrue(expected == money_diff)

    def test_return_error_which_sub_money_and_other_class(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__sub__)

    def test_return_the_product_of_money_and_numbers(self):
        money = Money.yen(10)

        money_prod = money * 2.5
        expected = Money.yen(25)
        self.assertTrue(expected == money_prod)

    def test_return_error_which_product_money_and_except_numbers(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__mul__)

    def test_return_the_quotient_between_the_money_and_numbers(self):
        money = Money.yen(10)

        money_quot = money / 4.
        expected = Money.yen(2.5)
        self.assertTrue(expected == money_quot)

    def test_return_error_which_quotient_between_money_and_except_numbers(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__div__)

    def test_return_the_quotient_of_floordiv_between_the_money_and_numbers(self):
        money = Money.yen(10)

        money_quot = money // 4.
        expected = Money.yen(2.0)
        self.assertTrue(expected == money_quot)

    def test_return_the_remainder_divide_money_by_numbers(self):
        money = Money.yen(10)

        money_remain = money % 3
        expected = Money.yen(1)
        self.assertTrue(expected == money_remain)

    def test_return_error_which_remainder_divide_money_by_except_numbers(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__mod__)

    def test_greater_than_with_two_same_nationality_money(self):
        greatest = Money.yen(11)
        median = Money.yen(10)
        least = Money.yen(9)

        self.check_greater_operator_of_rich_comparison(median.__gt__, greatest, median, least, False)

    def test_greater_than_with_two_different_nationality_money(self):
        greatest = Money.dollar(20.1)
        median = Money.yen(10)
        median.set_exchanger(DummyExchanger())
        least = Money.dollar(19.9)

        self.check_greater_operator_of_rich_comparison(median.__gt__, greatest, median, least, False)

    def test_greater_than_with_money_and_real_number(self):
        greatest = 10.1
        median = Money.yen(10)
        least = 9.9

        self.check_greater_operator_of_rich_comparison(median.__gt__, greatest, median.value, least, False)

    def test_greater_than_with_money_and_except_numbers(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__gt__)

    def test_greater_equal_with_two_same_nationality_money(self):
        greatest = Money.yen(11)
        median = Money.yen(10)
        least = Money.yen(9)

        self.check_greater_operator_of_rich_comparison(median.__ge__, greatest, median, least, True)

    def test_greater_equal_with_two_different_nationality_money(self):
        greatest = Money.dollar(20.1)
        median = Money.yen(10)
        median.set_exchanger(DummyExchanger())
        least = Money.dollar(19.9)

        self.check_greater_operator_of_rich_comparison(median.__ge__, greatest, median, least, True)

    def test_greater_equal_with_money_and_real_number(self):
        greatest = 10.1
        median = Money.yen(10)
        least = 9.9

        self.check_greater_operator_of_rich_comparison(median.__ge__, greatest, median.value, least, True)

    def test_greater_equal_with_money_and_except_numbers(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__ge__)

    def test_less_than_with_two_same_nationality_money(self):
        greatest = Money.yen(11)
        median = Money.yen(10)
        least = Money.yen(9)

        self.check_less_operator_of_rich_comparison(median.__lt__, greatest, median, least, False)

    def test_less_than_with_two_different_nationality_money(self):
        greatest = Money.dollar(20.1)
        median = Money.yen(10)
        median.set_exchanger(DummyExchanger())
        least = Money.dollar(19.9)

        self.check_less_operator_of_rich_comparison(median.__lt__, greatest, median, least, False)

    def test_less_than_with_money_and_real_number(self):
        greatest = 10.1
        median = Money.yen(10)
        least = 9.9

        self.check_less_operator_of_rich_comparison(median.__lt__, greatest, median.value, least, False)

    def test_less_than_with_money_and_except_numbers(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__lt__)

    def test_less_equal_with_two_same_nationality_money(self):
        greatest = Money.yen(11)
        median = Money.yen(10)
        least = Money.yen(9)

        self.check_less_operator_of_rich_comparison(median.__le__, greatest, median, least, True)

    def test_less_equal_with_two_different_nationality_money(self):
        greatest = Money.dollar(20.1)
        median = Money.yen(10)
        median.set_exchanger(DummyExchanger())
        least = Money.dollar(19.9)

        self.check_less_operator_of_rich_comparison(median.__le__, greatest, median, least, True)

    def test_less_equal_with_money_and_real_number(self):
        greatest = 10.1
        median = Money.yen(10)
        least = 9.9

        self.check_less_operator_of_rich_comparison(median.__le__, greatest, median.value, least, True)

    def test_less_equal_with_money_and_except_numbers(self):
        money = Money.yen(10)
        self.check_unexpected_type_as_number(money.__le__)

    def test_return_the_money_that_aligned_the_unit_to_currency_of_each_nationality(self):
        money_yen = Money.yen(10.2)
        expected = (10, 0)
        self.assertTrue(expected == money_yen.currency())

        money_dollar = Money.dollar(10.2)
        expected = (10, 20)
        self.assertTrue(expected == money_dollar.currency())

    def check_unexpected_type_as_number(self, calculation_name):
        self.assertRaises(TypeError, calculation_name, "20")
        self.assertRaises(TypeError, calculation_name, (2, "3"))
        self.assertRaises(TypeError, calculation_name, ["5", 2])

    def check_greater_operator_of_rich_comparison(self, operator_name, greatest, equal, least, when_equal):
        self.assertEqual(operator_name(least), True)
        self.assertEqual(operator_name(equal), when_equal)
        self.assertEqual(operator_name(greatest), False)

    def check_less_operator_of_rich_comparison(self, operator_name, greatest, equal, least, when_equal):
        self.assertEqual(operator_name(greatest), True)
        self.assertEqual(operator_name(equal), when_equal)
        self.assertEqual(operator_name(least), False)


if __name__ == '__main__':
    unittest.main()
