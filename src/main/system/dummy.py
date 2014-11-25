# coding: utf-8
class DummyDateBaseAgent:
    @classmethod
    def insert(cls, reservation_set):
        print reservation_set + "を予約するよ"

    @classmethod
    def update(cls, reservation_number, new_reservation_set):
        print str(reservation_number) + "の予約情報を" + new_reservation_set + "に変更するゾイ"

    @classmethod
    def delete(cls, reservation_number):
        print "予約番号" + str(reservation_number) + "の予約情報を削除します"

    @classmethod
    def check(cls, plan_name):
        rooms = 1
        print plan_name + "の空室状況: "
        return rooms

    """
    get dummy data
    @return tuple :キーの重複を取り除いた状態で返す
    """

    @classmethod
    def query(cls, reservation_number):
        # 予約情報モデル
        check_in = "14/11/14/Fri"
        check_in_time = 15
        check_out = "14/11/15/Sat"
        reservation = (check_in, check_in_time, check_out)

        # 顧客モデル
        name = "knskw"
        mail = "knskw@nullnull.com"
        address = "檸檬根井都武者返市愛宿町4-2-3 エレガンスウェストポーチ999号室"
        customer = (name, mail, address)

        # 宿泊プランモデル
        plan_name = "すこやかパック"
        price = 4500
        rooms = 1
        bed_type = "だんぼーる"
        option = "みかん"
        plan = (plan_name, price, rooms, bed_type, option)

        sql_tuple = (reservation_number,) + customer + plan + reservation
        return sql_tuple

