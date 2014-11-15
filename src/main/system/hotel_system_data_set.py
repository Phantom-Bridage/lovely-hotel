# coding: utf-8

from system.dummy_DB_set import DummyDateBaseSet
from system.converter import Converter


class HotelSystemDataSet:
    def __init__(self):
        self.__dummy = DummyDateBaseSet()

    def packet(self, reserve_number):
        # データ取得
        __reserve_data = self.__dummy.reserve_result(reserve_number)
        __customer_number = __reserve_data[1]
        __customer_data = self.__dummy.customer_result(__customer_number)
        __plan_number = __reserve_data[2]
        __plan_data = self.__dummy.plan_result(__plan_number)

        # 文字列に変換
        rl = Converter.to_str(__reserve_data)
        cl = Converter.to_str(__customer_data)
        pl = Converter.to_str(__plan_data)

        # 結合時の重複データ(主キーおよび外部キー)削除
        for i in range(3):
            del rl[0]
        del cl[0]
        del pl[0]

        # パケットに変換
        packet = str(reserve_number) + ','
        packet += ','.join(cl) + ','
        packet += ','.join(pl) + ','
        packet += ','.join(rl)

        return packet