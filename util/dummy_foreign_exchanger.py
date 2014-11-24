# -*- coding:utf-8 -*-


class DummyExchanger(object):
    def exchange(self, origin, result, value):
        if origin == result:
            return value

        if origin == "yen" and result == "dollar":
            return value*2.0

        if origin == "dollar" and result == "yen":
            return value*0.5