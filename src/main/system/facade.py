# coding: utf-8

from system.dummy import DummyDateBaseAgent
import numbers


class Facade:
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

    # 照会
    @classmethod
    def inquiry(cls, reserve_number):
        if not isinstance(reserve_number, numbers.Number):
            raise TypeError

        sql = DummyDateBaseAgent.query(reserve_number)
        packet = ",".join(map(str, sql))
        return packet


if __name__ == "__main__":
    s = Facade.search("BNS")
    Facade.reserve("新規予約情報")
    i = Facade.inquiry(22)
    Facade.alter(22, "変更後の予約情報")
    Facade.delete(22)
    print s
    print i
