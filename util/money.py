# -*- coding:utf-8 -*-
import numbers


class Money(object):
    def __init__(self, value, nationality):
        if not isinstance(value, numbers.Real):
            err_msg = "'value' must be Integer or Real"
            raise TypeError(err_msg)
        self.__value = value
        self.__nationality = nationality
        self.__exchanger = None

    @classmethod
    def yen(cls, value):
        return Money(value, "yen")

    @classmethod
    def dollar(cls, value):
        return Money(value, "dollar")

    @property
    def value(self):
        return self.__value

    @property
    def nationality(self):
        return self.__nationality

    def set_exchanger(self, exchanger):
        self.__exchanger = exchanger

    def exchange(self, result):
        if self.__exchanger is None:
            err_msg = "Exchanger has not been set"
            raise AttributeError(err_msg)

        result_value = self.__exchanger.exchange(self.nationality, result, self.value)
        return Money(result_value, result)

    def __eq__(self, other):
        if self.nationality == other.nationality and self.value == other.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, numbers.Real):
            return self.value > other

        self.__instance_is_support_with_operand_of(other, Money, ">")

        if self.nationality == other.nationality:
            return self.value > other.value

        if self.nationality != other.nationality:
            return self.value > self.__exchanger.exchange(other.nationality, self.nationality, other.value)

    def __ge__(self, other):
        if isinstance(other, numbers.Real):
            return self.value >= other

        self.__instance_is_support_with_operand_of(other, Money, ">=")

        if self.nationality == other.nationality:
            return self.value >= other.value

        if self.nationality != other.nationality:
            return self.value >= self.__exchanger.exchange(other.nationality, self.nationality, other.value)

    def __lt__(self, other):
        if isinstance(other, numbers.Real):
            return self.value < other

        self.__instance_is_support_with_operand_of(other, Money, "<")

        if self.nationality == other.nationality:
            return self.value < other.value

        if self.nationality != other.nationality:
            return self.value < self.__exchanger.exchange(other.nationality, self.nationality, other.value)

    def __le__(self, other):
        if isinstance(other, numbers.Real):
            return self.value <= other

        self.__instance_is_support_with_operand_of(other, Money, "<=")

        if self.nationality == other.nationality:
            return self.value <= other.value

        if self.nationality != other.nationality:
            return self.value <= self.__exchanger.exchange(other.nationality, self.nationality, other.value)

    def __add__(self, other):
        self.__instance_is_support_with_operand_of(other, Money, "+")

        if self.nationality == other.nationality:
            return Money(self.value+other.value, self.nationality)

        if self.nationality != other.nationality:
            exchanged_value = self.__exchanger.exchange(other.nationality, self.nationality, other.value)
            return Money(self.value + exchanged_value, self.nationality)

    def __sub__(self, other):
        self.__instance_is_support_with_operand_of(other, Money, "-")

        if self.nationality == other.nationality:
            return Money(self.value-other.value, self.nationality)

        if self.nationality != other.nationality:
            exchanged_value = self.__exchanger.exchange(other.nationality, self.nationality, other.value)
            return Money(self.value - exchanged_value, self.nationality)

    def __mul__(self, other):
        self.__instance_is_support_with_operand_of(other, numbers.Real, "*")

        return Money(self.value*other, self.nationality)

    def __div__(self, other):
        self.__instance_is_support_with_operand_of(other, numbers.Real, "/")

        return Money(self.value / other, self.nationality)

    def __floordiv__(self, other):
        self.__instance_is_support_with_operand_of(other, numbers.Real, "//")

        return Money(self.value // other, self.nationality)

    def __mod__(self, other):
        self.__instance_is_support_with_operand_of(other, numbers.Real, "%%")

        return Money(self.value % other, self.nationality)

    def currency(self):
        if self.nationality == "yen":
            return round(self.value), 0

        if self.nationality == "dollar":
            return int(self.value), int(100*round(self.value - int(self.value), 2))

        return None

    @staticmethod
    def __instance_is_support_with_operand_of(value, _class, operand):
        if not isinstance(value, _class):
            type_of_other = str(type(value))
            err_msg = "unsupported operand type(s) for {}: 'Money' and '{}'".format(operand, type_of_other[7:-2])
            raise TypeError(err_msg)

    def __str__(self):
        return "str:Value={M}, Nationality={N}".format(M=self.__value, N=self.__nationality)

    def __repr__(self):
        return "repr:Value={M}, Nationality={N}".format(M=self.__value, N=self.__nationality)

    def __unicode__(self):
        return u"unicode:Value={M}, Nationality={N}".format(M=self.__value, N=self.__nationality)