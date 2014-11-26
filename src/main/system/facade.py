# coding: utf-8

from system.dummy import DummyDateBaseAgent
from system.db_manager import DataBaseManager


class Facade:
    def __init__(self):
        pass

    """
    # 新規予約
    @classmethod
    def reserve(cls, reservation_set):
        DummyDateBaseAgent.insert(reservation_set)

    # 変更
    @classmethod
    def alter(cls, reservation_number, new_reservation_set):
        DummyDateBaseAgent.update(reservation_number, new_reservation_set)

    # 削除
    @classmethod
    def delete(cls, reservation_number):
        DummyDateBaseAgent.delete(reservation_number)

    # 空室の確認
    @classmethod
    def search(cls, plan_name):
        return DummyDateBaseAgent.check(plan_name)
    """
    # 照会
    def inquiry(self, reserve_number):
        if not isinstance(reserve_number, int):
            raise TypeError("arg. should be Integer")

        dbm = DataBaseManager()
        sql = dbm.verify_reservation(reserve_number)
        # sql = DummyDateBaseAgent.query(reserve_number)
        packet = ",".join(map(unicode, sql))
        return packet


if __name__ == "__main__":
    f = Facade()
    print f.inquiry(1)
